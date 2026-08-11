"""Minimální podpora direktiv používaných v dokumentaci CPythonu.

Projekt zachovává původní RST direktivy, ale nepotřebuje celý sestavovací
řetězec oficiální dokumentace CPythonu.
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.domains.changeset import VersionChange, versionlabel_classes, versionlabels
from sphinx.domains.python import PyFunction
from sphinx.util.docutils import SphinxDirective


class AwaitableFunction(PyFunction):
    """Funkce vracející awaitable objekt."""

    def handle_signature(self, sig, signode):
        result = super().handle_signature(sig, signode)
        signode.insert(0, addnodes.desc_annotation("awaitable ", "awaitable "))
        return result


class CpythonAdmonition(SphinxDirective):
    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True

    css_class = "cpython-note"
    title = "Poznámka"

    def build_admonition(self):
        admonition = nodes.admonition(classes=[self.css_class])
        admonition += nodes.title(text=self.title)
        return admonition


class ImplementationDetail(CpythonAdmonition):
    css_class = "impl-detail"
    title = "Implementační detail CPythonu"

    def run(self):
        admonition = self.build_admonition()
        if self.arguments:
            admonition += nodes.paragraph(text=self.arguments[0])
        self.state.nested_parse(self.content, self.content_offset, admonition)
        return [admonition]


class DeprecatedRemoved(VersionChange):
    required_arguments = 2

    def run(self):
        deprecated_version = self.arguments[0]
        removed_version = self.arguments.pop(1)
        self.arguments[0] = (deprecated_version, removed_version)
        versionlabels[self.name] = (
            "Zastaralé od verze %s, odstraněno ve verzi %s"
        )
        versionlabel_classes[self.name] = "deprecated"
        try:
            return super().run()
        finally:
            versionlabels[self.name] = ""
            versionlabel_classes[self.name] = ""


class AuditEvent(CpythonAdmonition):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    css_class = "audit-event"
    title = "Auditní událost"

    def run(self):
        event, _, remainder = self.arguments[0].partition(" ")
        arguments, _, _anchor = remainder.rpartition(" ")
        admonition = self.build_admonition()
        if self.content:
            self.state.nested_parse(self.content, self.content_offset, admonition)
        else:
            paragraph = nodes.paragraph()
            paragraph += nodes.Text("Vyvolá auditní událost ")
            paragraph += nodes.literal(text=event)
            if arguments:
                paragraph += nodes.Text(" s argumenty ")
                paragraph += nodes.literal(text=arguments)
            paragraph += nodes.Text(".")
            admonition += paragraph
        return [admonition]


def setup(app):
    app.add_directive("awaitablefunction", AwaitableFunction)
    app.add_directive("audit-event", AuditEvent)
    app.add_directive("deprecated-removed", DeprecatedRemoved)
    app.add_directive("impl-detail", ImplementationDetail)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
