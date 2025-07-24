from os import path
from sphinx.util.fileutil import copy_asset_file


def copy_custom_files(app, exc, filename):
    if not exc:
        if app.builder.format == "html":
            staticfile = path.join(app.builder.outdir, "_static", filename)
            cssfile = path.join(path.dirname(__file__), "_static", filename)
            copy_asset_file(cssfile, staticfile)


def add_css(app, filename):
    app.connect(
        "build-finished", lambda app, exc: copy_custom_files(app, exc, filename)
    )
    app.add_css_file(filename)


def add_js(app, filename):
    app.connect(
        "build-finished", lambda app, exc: copy_custom_files(app, exc, filename)
    )
    app.add_js_file(filename)
