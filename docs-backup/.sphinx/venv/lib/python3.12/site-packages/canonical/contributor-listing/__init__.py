from git import Repo, InvalidGitRepositoryError
from sphinx.util import logging
import os
from . import common

logger = logging.getLogger(__name__)


def setup(app):
    app.connect("html-page-context", setup_func)

    common.add_css(app, "contributors.css")
    common.add_js(app, "contributors.js")

    return {"version": "1.0.0",
            "parallel_read_safe": True,
            "parallel_write_safe": True}


def setup_func(app, pagename, templatename, context, doctree):
    def get_contributors_for_file(pagename, page_source_suffix):

        if (
            "display_contributors" not in context
            or "github_folder" not in context
            or "github_url" not in context
        ):
            return []

        if context["display_contributors"]:
            filename = f"{pagename}{page_source_suffix}"
            paths = context["github_folder"][1:] + filename

            try:
                repo = Repo(".")
            except InvalidGitRepositoryError:
                cwd = os.getcwd()
                ghfolder = context["github_folder"][:-1]
                if ghfolder and cwd.endswith(ghfolder):
                    repo = Repo(cwd.rpartition(ghfolder)[0])
                else:
                    logger.warning(
                        "The local Git repository could not be found."
                    )
                    return

            since = None

            if (
                "display_contributors_since" in context
                and context["display_contributors_since"]
                and context["display_contributors_since"].strip()
            ):
                since = context["display_contributors_since"]

            try:
                commits = repo.iter_commits(paths=paths, since=since)
            except ValueError as e:
                logger.warning(
                    "Failed to iterate through the Git commits: " + str(e)
                )
                return

            contributors_dict = {}
            for commit in commits:
                contributors = [commit.author.name]
                for co_author in commit.co_authors:
                    contributors.append(co_author.name)
                for contributor in contributors:
                    if (
                        contributor not in contributors_dict
                        or commit.committed_date > contributors_dict[contributor]["date"]
                    ):
                        contributors_dict[contributor] = {
                            "date": commit.committed_date,
                            "sha": commit.hexsha,
                        }
            # github_page contains the link to the contributor's latest commit
            contributors_list = [
                (name, f"{context['github_url']}/commit/{data['sha']}")
                for name, data in contributors_dict.items()
            ]

            return sorted(contributors_list)

        else:
            return []

    context["get_contributors_for_file"] = get_contributors_for_file
