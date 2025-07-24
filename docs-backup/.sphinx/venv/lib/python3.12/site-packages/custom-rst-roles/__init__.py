import re

from docutils import nodes
from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.domains.std import StandardDomain
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import ReferenceRole
from typing import cast
from typing_extensions import override


def spellexception_role(
    name, rawtext, text, lineno, inliner, options=None, content=None
):
    node = nodes.raw(
        text="<spellexception>" + text + "</spellexception>", format="html"
    )
    return [node], []


def none_role(
    name, rawtext, text, lineno, inliner, options=None, content=None
):
    return [], []


class LiteralrefRole(ReferenceRole):
    """Define the literalref role's behavior."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Create a cross-reference with monospaced text."""
        node: nodes.reference | addnodes.pending_xref

        # Create an external reference
        if re.match(r"^(https?:\/\/\S+|\S+\.\S{2,3}\/?)\b", self.target):
            self.target = (
                f"https://{self.target}"
                if "://" not in self.target
                else self.target
            )
            node = nodes.reference("", "", internal=False, refuri=self.target)
        else:  # Create an internal reference
            node = addnodes.pending_xref(
                "",
                refdomain="lrd",  # use custom domain
                reftype="ref",
                reftarget=self.target,
                refexplicit=True,
                refwarning=True,
            )

        #  append the link text
        node.append(nodes.literal(text=self.title))

        return [node], []


class LiteralrefDomain(StandardDomain):
    """Custom domain for the :literalref: role."""

    name: str = "lrd"

    @override
    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: addnodes.pending_xref,
        contnode: nodes.Element,
    ) -> nodes.reference | None:
        """Replace the resolved node's child with the children assigned to
        the pending reference node.

        By default, Sphinx's standard domain
        disregards the type of the pending node's children and places their
        contents into an inline node.
        """
        if node.get("refdomain") != "lrd":
            return None

        resolved_node = super().resolve_xref(
            env, fromdocname, builder, typ, target, node, contnode
        )  # resolve the reference using the standard domain

        if (
            resolved_node
            and hasattr(resolved_node, "children")
            and hasattr(node, "children")
        ):  # replace the child node from ``std`` with the original children
            resolved_node.children = node.children

        return cast(nodes.reference, resolved_node)


def setup(app):
    app.add_domain(LiteralrefDomain)
    app.add_role("spellexception", spellexception_role)
    app.add_role("literalref", LiteralrefRole())
    app.add_role("none", none_role)

    return {"parallel_read_safe": True,
            "parallel_write_safe": True}
