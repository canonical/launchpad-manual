from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives
from . import common
import sphinx
from sphinx.application import Sphinx


copybutton_classes = "div.terminal.copybutton > div.container > code.command, div:not(.terminal-code, .no-copybutton) > div.highlight > pre"


def parse_contents(contents):
    command_output = []
    out = []

    for line in contents:
        if line.startswith(":input: "):
            out.append(command_output)
            out.append([line])
            command_output = []
        else:
            command_output.append(line)

    out.append(command_output)
    return out


class TerminalOutput(SphinxDirective):

    required_arguments = 0
    optional_arguments = 0
    has_content = True
    option_spec = {
        "class": directives.class_option,
        "input": directives.unchanged,
        "user": directives.unchanged,
        "host": directives.unchanged,
        "dir": directives.unchanged,
        "scroll": directives.unchanged,
        "copy": directives.unchanged,
    }

    @staticmethod
    def input_line(prompt_text, command):

        inpline = nodes.container()
        inpline["classes"].append("input")

        # To let the prompt be styled separately in LaTeX, it needs to be
        # wrapped in a container. This adds an extra div to the HTML output,
        # but what's a few bytes between friends?
        prompt_container = nodes.container()
        prompt_container["classes"].append("prompt")
        prompt = nodes.literal(text=prompt_text)
        prompt_container.append(prompt)

        inpline.append(prompt_container)
        inp = nodes.literal(text=command)
        inp["classes"].append("command")
        inpline.append(inp)
        # inpline.append(nodes.paragraph())
        return inpline

    def run(self):
        # if :user: or :host: are provided, replace those in the prompt

        classes = self.options.get("class", "")
        command = self.options.get("input", "")
        user = self.options.get("user", "user")
        host = self.options.get("host", "host")
        dir = self.options.get("dir", "~")
        user_symbol = "#" if user == "root" else "$"
        if user and host:
            prompt_text = f"{user}@{host}:{dir}{user_symbol} "
        elif user and not host:
            # Only the user is supplied
            prompt_text = f"{user}:{dir}{user_symbol} "
        else:
            # Omit both user and host, just showing the host
            # doesn't really make sense
            prompt_text = f"{dir}{user_symbol} "

        out = nodes.container()
        out["classes"].append("terminal")
        if "copy" in self.options:
            out["classes"].append("copybutton")
        for item in classes:
            out["classes"].append(item)
        # The super-large value for linenothreshold is a major hack since I
        # can't figure out how to disable line numbering and the
        # linenothreshold kwarg seems to be required.
        out.append(
            sphinx.addnodes.highlightlang(
                lang="text", force=False, linenothreshold=10000
            )
        )
        if "scroll" in self.options:
            out["classes"].append("scroll")

        # Add the original prompt and input

        out.append(self.input_line(prompt_text, command))
        # breakpoint()

        # Go through the content and append all lines as output
        # except for the ones that start with ":input: " - those get
        # a prompt

        parsed_content = parse_contents(self.content)

        for blob in filter(None, parsed_content):
            if blob[0].startswith(":input: "):
                out.append(self.input_line(prompt_text, blob[0][len(":input: "):]))
            else:
                output = nodes.literal_block(text="\n".join(blob))
                output["classes"].append("terminal-code")
                out.append(output)
        return [out]


def setup(app: Sphinx):
    app.add_directive("terminal", TerminalOutput)

    common.add_css(app, "terminal-output.css")
    if "copybutton_selector" not in app.config._raw_config:
        app.config._raw_config.setdefault("copybutton_selector", copybutton_classes)
    if app.config._raw_config["copybutton_selector"] == "div.highlight pre":
        app.config._raw_config["copybutton_selector"] = copybutton_classes

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
