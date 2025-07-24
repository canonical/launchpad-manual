from collections import defaultdict
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util import logging
from . import common

logger = logging.getLogger(__name__)


# Parse rST inside an option (":something:")
def parseOption(obj, option):
    newNode = nodes.inline()
    parseNode = ViewList()
    parseNode.append(option, "parsing", 1)
    obj.state.nested_parse(parseNode, 0, newNode)
    return newNode


class ConfigOption(ObjectDescription):

    optional_fields = {
        "type": "Type",
        "default": "Default",
        "defaultdesc": "Default",
        "initialvaluedesc": "Initial value",
        "liveupdate": "Live update",
        "condition": "Condition",
        "readonly": "Read-only",
        "resource": "Resource",
        "managed": "Managed",
        "required": "Required",
        "scope": "Scope",
    }

    required_arguments = 1
    optional_arguments = 1
    has_content = True
    option_spec = {
        "shortdesc": directives.unchanged_required
    }
    for field in optional_fields:
        option_spec[field] = directives.unchanged

    def run(self):

        # Create a targetID and target

        scope = "server"
        if len(self.arguments) > 1:
            scope = self.arguments[1]
        targetID = scope + ":" + self.arguments[0]
        targetNode = nodes.target("", "", ids=[targetID])

        # Generate the output

        key = nodes.inline()
        key += nodes.literal(text=self.arguments[0])
        key["classes"].append("key")

        if "shortdesc" not in self.options:
            logger.warning(
                "The option fields for the "
                + self.arguments[0]
                + " option could not be parsed. "
                + "No output was generated."
            )
            return []

        shortDesc = parseOption(self, self.options["shortdesc"])
        shortDesc["classes"].append("shortdesc")

        anchor = nodes.inline()
        anchor["classes"].append("anchor")
        refnode = nodes.reference("", refuri="#" + targetID)
        refnode += nodes.raw(
            text='<i class="icon"><svg>'
            + '<use href="#svg-arrow-right"></use></svg></i>',
            format="html",
        )
        anchor += refnode

        firstLine = nodes.container()
        firstLine["classes"].append("basicinfo")
        firstLine += key
        firstLine += shortDesc
        firstLine += anchor

        details = nodes.container()
        details["classes"].append("details")
        fields = nodes.table()
        fields["classes"].append("fields")
        tgroup = nodes.tgroup(cols=2)
        fields += tgroup
        tgroup += nodes.colspec(colwidth=1)
        tgroup += nodes.colspec(colwidth=3)
        rows = []
        # Add the key name again
        row_node = nodes.row()
        desc_entry = nodes.entry()
        desc_entry += nodes.strong(text="Key: ")
        val_entry = nodes.entry()
        val_entry += nodes.literal(text=self.arguments[0])
        row_node += desc_entry
        row_node += val_entry
        rows.append(row_node)
        # Add the other fields
        for field in self.optional_fields:
            if field in self.options:
                row_node = nodes.row()
                desc_entry = nodes.entry()
                desc_entry += nodes.strong(text=self.optional_fields[field]
                                           + ": ")
                parsedOption = parseOption(self, self.options[field])
                parsedOption["classes"].append("ignoreP")
                val_entry = nodes.entry()
                val_entry += parsedOption
                row_node += desc_entry
                row_node += val_entry
                rows.append(row_node)
        tbody = nodes.tbody()
        tbody.extend(rows)
        tgroup += tbody
        details += fields
        self.state.nested_parse(self.content, self.content_offset, details)

        # Create a new container node with the content

        newNode = nodes.container()
        newNode["classes"].append("configoption")
        newNode += firstLine
        newNode += details

        # Register the target with the domain

        configDomain = self.env.get_domain("config")
        configDomain.add_option(self.arguments[0], scope)

        # Return the content and target node

        return [targetNode, newNode]


class ConfigIndex(Index):

    # To link to the index: {ref}`config-options`
    name = "options"
    localname = "Configuration options"

    def generate(self, docnames=None):
        content = defaultdict(list)

        options = self.domain.get_objects()
        # sort by key name
        options = sorted(options, key=lambda option: (option[1], option[4]))

        dispnames = []
        duplicates = []
        for _name, dispname, _typ, _docname, anchor, _priority in options:
            fullname = anchor.partition(":")[0].partition("-")[0] \
                + "-" + dispname
            if fullname in dispnames:
                duplicates.append(fullname)
            else:
                dispnames.append(fullname)

        for _name, dispname, typ, docname, anchor, _priority in options:

            scope = anchor.partition(":")[0].partition("-")

            # if the key exists more than once within the scope, add
            # the title of the document as extra context
            if scope[0] + "-" + dispname in duplicates:
                extra = str(self.domain.env.titles[docname])
                # need some tweaking to work with our CSS
                extra = extra.replace("<title>", "")
                extra = extra.replace("</title>", "")
                extra = extra.replace("<literal>", '<code class="literal">')
                extra = extra.replace("</literal>", "</code>")
                # add the anchor for full information
                extra += ': <code class="literal">' + scope[2] + "</code>"
            else:
                extra = ""

            # group by the first part of the scope
            # ("XXX" if the scope is "XXX-YYY")
            content[scope[0]].append(
                (dispname, 0, docname, anchor, extra, "", "")
            )

        content = sorted(content.items())

        return content, True


class ConfigDomain(Domain):

    name = "config"
    label = "Configuration Options"
    roles = {"option": XRefRole()}
    directives = {"option": ConfigOption}
    indices = {ConfigIndex}
    initial_data = {"config_options": []}

    def get_objects(self):
        yield from self.data["config_options"]

    # Find the node that is being referenced
    def resolve_xref(self, env, fromdocname, builder, typ, target,
                     node, contnode):

        # If the scope isn't specified, default to "server"
        if ":" not in target:
            target = "server:" + target

        match = [
            (key, docname, anchor)
            for key, sig, typ, docname, anchor, prio in self.get_objects()
            if anchor == target and typ == "option"
        ]

        if len(match) > 0:
            title = match[0][0]
            todocname = match[0][1]
            targ = match[0][2]

            refNode = make_refnode(
                builder, fromdocname, todocname, targ,
                child=nodes.literal(text=title)
            )
            refNode["classes"].append("configref")
            return refNode

        else:
            logger.warning(
                "Could not find target " + target + " in " + fromdocname
            )
            return []

    # We don't want to link with "any" role, but only with "config:option"
    def resolve_any_xref(self, env, fromdocname, builder, target, node,
                         contnode):
        return []

    # Store the option
    def add_option(self, key, scope):

        self.data["config_options"].append(
            (key, key, "option", self.env.docname, scope + ":" + key, 0)
        )

    def merge_domaindata(self, docnames, otherdata):

        for option in otherdata["config_options"]:
            if option not in self.data["config_options"]:
                self.data["config_options"].append(option)


def setup(app):
    app.add_domain(ConfigDomain)

    common.add_css(app, "config-options.css")
    common.add_js(app, "config-options.js")

    return {"version": "0.1", "parallel_read_safe": True,
            "parallel_write_safe": True}
