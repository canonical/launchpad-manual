import re
from sphinx.directives.other import TocTree


def setup(app):
    app.add_config_value("toc_filter_exclude", [], "html")
    app.add_directive("filtered-toctree", FilteredTocTree)
    return {"version": "1.0.0",
            "parallel_read_safe": True,
            "parallel_write_safe": True}


class FilteredTocTree(TocTree):

    findFilter = re.compile(r"^\s*:(.+?):.+$|^.*<:(.+?):.+>$")

    # Go through all toctree entries and check if they should be included.
    # If they should be included, remove the filter (":something:").
    def filter_entries(self, entries):
        excl = self.state.document.settings.env.config.toc_filter_exclude
        filtered = []
        for e in entries:
            m = self.findFilter.match(e)

            if m is not None:
                # The filter is in different matches depending on whether
                # we override the title and where we put the filter
                if e.startswith(":"):
                    filt = m.groups()[0]
                elif e.endswith(">"):
                    filt = m.groups()[1]
                else:
                    filt = m.groups()[0]

                # Keep the entries that are not supposed to be excluded
                if filt not in excl:
                    filtered.append(e.replace(":" + filt + ":", ""))
            else:
                filtered.append(e)
        return filtered

    def run(self):
        # Remove all TOC entries that should not be included
        self.content = self.filter_entries(self.content)
        return super().run()
