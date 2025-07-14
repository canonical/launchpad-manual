# Custom configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# The file is included in the common conf.py configuration file.
# You can modify any of the settings below or add any configuration that
# is not covered by the common conf.py file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

############################################################
### Project information
############################################################

# Product name
project = "Launchpad Manual"
author = "Canonical Group Ltd"

# Uncomment if your product uses release numbers
# release = '1.0'

# The default value uses the current year as the copyright year.
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = "2023, %s" % author

## Open Graph configuration - defines what is displayed in the website preview
# The URL of the documentation output
ogp_site_url = "https://canonical-launchpad-manual.readthedocs-hosted.com/"
# The documentation website name (usually the same as the product name)
ogp_site_name = project
# An image or logo that is used in the preview
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

# Update with the favicon for your product (default is the circle of friends)
html_favicon = ".sphinx/_static/favicon.png"

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {
    # Change to the link to your product website (without "https://")
    "product_page": "launchpad.net",
    # Add your product tag to ".sphinx/_static" and change the path
    # here (start with "_static"), default is the circle of friends
    # XXX 2023-09-29: jugmac00 - currently using the Canonical default image
    "product_tag": "_static/tag.png",
    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    "discourse": "",
    # Change to the GitHub info for your project
    "github_url": "https://github.com/canonical/launchpad-manual",
    # Change to the branch for this version of the documentation
    "github_version": "main",
    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    "github_folder": "/",
    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    "github_issues": "enabled",
    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "none",
}

# Here we can configure custom theme options.
html_theme_options = {
    # `sidebar_hide_name`deactivates the repetitive heading in the side bar.
    # This configuration option will change soon, see
    # https://github.com/canonical/sphinx-docs-starter-pack/issues/103.
    "sidebar_hide_name": True,
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug = ""

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

redirects = {}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links

linkcheck_ignore = [
    r"http://www.gnu\.org/.*",
    r"http://www.fsf\.org/.*",
    "http://127.0.0.1:8000",
    r"https://app\.diagrams\.net.*",  # ignore, as works in browser, but link checker has some issues
    "https://archive.ph/CAqQm",  # ignore, as works in browser, but link checker has some issues
    r"http://bazaar\.launchpad\.net/.*", #bazaar is in the process of being shutdown
    "https://bazaar.launchpad.net/lp-production-config",  # private
    "https://bazaar.staging.launchpad.net",  # broken, unclear why XXX 2023-10-14: jugmac00- check with team
    r"https://www\.breezy-vcs\.org/.*",  # broken, returns "Connection refused" on port 443
    r"http://doc\.bazaar-vcs\.org\.*", #broken, bazaar being shut down
    "http://bazaar-vcs.org",  #broken, bazaar being shut down
    "http://www.bazaar-vcs.org/" #broken, bazaar being shut down
    "https://bugs.launchpad.net/charm-launchpad-buildd-image-modifier",  # private
    "https://bugs.launchpad.net/launchpad-vbuilder-manage",  # private
    "http://example.com/.*",  # ignore, example links
    "https://launchpad.net/canonical-mojo-specs",  # private
    r"https://launchpad\.test.*",  # ignore, local test setup
    r"http://code\.beta\.launchpad\.net/.*",
    "http://diacritice.svn.sourceforge.net/viewvc/diacritice/trunk/", # ignore, as works in browser, but link checker has some issues
    "http://epydoc.sourceforge.net/fields.html", # ignore, as works in browser, but link checker has some issues
    "http://api.staging.launchpad.net/people/+me", #ignore, as works in browser, but link checker has some issues
    "http://i18n.ro/Ghidul_traducatorului_de_software", #broken
    r"http://sourceforge\.net/.*",
    "Trunk/Glue",  # needs update
    "/Background",
    "/Concepts",  # needs update
    "JavascriptUnitTesting/MockIo",  # needs update
    "https://git.launchpad.net/launchpad-mojo-specs/tree/mojo-lp-git/services",  # private
    "https://deployable.ols.canonical.com/project/launchpad-db",  # private
    "irc.libera.chat",  # this is not an HTTP link
    r"https://github\.com/canonical/fetch-service*",  # private
    r"https://github\.com/canonical/fetch-operator*",  # private
    "https://git.launchpad.net/charm-launchpad-buildd-image-modifier/tree/files/scripts/setup-ppa-buildd",  # private
    "https://git.zx2c4.com/cgit/",  # unfortunately very flaky
    "https://wiki.canonical.com/InformationInfrastructure/OSA/RequestLogging/LP/Cowboys",  # private
    "https://staging.launchpad.net",  # ignore, staging launchpad
    r"https://wiki\.canonical\.com/.*",  # private
    r"https://www\.nongnu\.org/.*",
    r"https://www\.gnu\.org/.*",
    r"https://www\.socialtext\.net/.*",
    r"https://translations\.launchpad\.net/.*",
    r"http://localhost.*",
    "http://www.ubuntu.com/community/ubuntustory/licensing", # works in browser, linkchecker issue
    #Uncertain Dead - May not be replaceable
    "/Estonian",
    "/Georgian",
    "/Indonesian",
    "/Italian",
    "/Korean",
    "/Russian",
    "../Vietnamese",
    #Replaceable Dead - Can probably be replaced by an equivalent
    "/../POTemplates", # - https://docs.lokalise.com/en/articles/1400767-gettext-po-pot
    "API",

    #Incorrect or non-existent file reference - Referenced file moved, deleted, or renamed
    "/../YourProject/ImportingTemplates",
    "Answer syntax parsing <Comments>",


]

# Pages on which to ignore anchors
# (This list will be appended to linkcheck_anchors_ignore_for_url)

custom_linkcheck_anchors_ignore_for_url = []

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.

# Add extensions
custom_extensions = []

# Add files or directories that should be excluded from processing.
custom_excludes = [
    "doc-cheat-sheet*",
    "readme.rst",
]

# Add CSS files (located in .sphinx/_static/)
custom_html_css_files = []

# Add JavaScript files (located in .sphinx/_static/)
custom_html_js_files = []

## The following settings override the default configuration.

# Specify a reST string that is included at the end of each file.
# If commented out, use the default (which pulls the reuse/links.txt
# file into each reST file).
# custom_rst_epilog = ''

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

############################################################
### Additional configuration
############################################################

## Add any configuration that is not covered by the common conf.py file.
