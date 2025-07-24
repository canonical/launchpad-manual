from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from . import common
import requests
from bs4 import BeautifulSoup

cache = {}


class YouTubeLink(Directive):

    required_arguments = 1
    optional_arguments = 0
    has_content = False
    option_spec = {"title": directives.unchanged}

    def run(self):

        title = ""

        if "title" in self.options:
            title = self.options["title"]
        elif self.arguments[0] in cache:
            title = cache[self.arguments[0]]
        else:
            try:
                r = requests.get(self.arguments[0])
                r.raise_for_status()
                soup = BeautifulSoup(r.text, "html.parser")
                title = soup.title.get_text()
                cache[self.arguments[0]] = title
            except requests.HTTPError as err:
                print(err)

        fragment = (
            ' \
        <p class="youtube_link"> \
          <a href="'
            + self.arguments[0]
            + '" target="_blank"> \
            <span title="'
            + title
            + '" class="play_icon">▶</span> \
            <span title="'
            + title
            + '">Watch on YouTube</span> \
          </a> \
        </p>'
        )
        raw = nodes.raw(text=fragment, format="html")

        return [raw]


def setup(app):
    app.add_directive("youtube", YouTubeLink)

    common.add_css(app, "youtube.css")

    return {"version": "0.1", "parallel_read_safe": True,
            "parallel_write_safe": True}
