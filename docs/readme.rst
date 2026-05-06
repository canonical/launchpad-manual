.. meta::
   :description: Get started with Launchpad's documentation for users and 
       developers. Set up the repository, edit and build docs locally, and more.

Launchpad Manual
================

Welcome to the official Launchpad Manual. This manual is designed to help users,
developers, and contributors understand and utilize the extensive features of
Launchpad effectively. It covers a wide range of topics, from basic navigation 
within Launchpad to advanced features such as bug tracking, and using the API. 

The documentation is separated into a user and a developer section. The former 
covers standard use cases to help you make use of Launchpad features, while the
latter offers an in-depth look at the inner workings of the platform for those 
interested in contributing to feature development and bug fixing.

The Launchpad Admin Manual is an accompanying set of internal docs containing 
non-public information used by Launchpad and other internal teams to run the 
platform and address user issues.

You can access the latest version of the documentation at
`https://documentation.ubuntu.com/launchpad/ <https://documentation.ubuntu.com/launchpad/>`_.

Build the documentation
-----------------------

The launchpad manual uses `Canonical's sphinx documentation starter pack <https://github.com/canonical/sphinx-docs-starter-pack>`_ 
to build the docs, and Read the Docs (RTD) to publish them. You can build the 
docs locally by following these steps:

#.  Clone this repository::

      git clone https://github.com/canonical/launchpad-manual.git

#. Navigate to the ``/docs`` directory::

      cd docs 

#. Install the prerequisities::

      make install 

#. Build and serve the documentation::

      make run 

The documentation will be served at ``http://127.0.0.1:8000`` by default. After
the first build, you can skip the first and third steps when rebuilding the 
documentation in the future.

Edit the documentation
----------------------
The Launchpad Manual docs are written in reStructuredText (RST) only. To make 
changes to this documentation, you'll need to clone the repository and update 
the relevant rst file(s) and/or add new ones.

It's a good idea to ensure that the documentation builds locally with no errors 
or warnings before proposing to merge your changes. Changes that fail CI checks 
due to avoidable errors will not be approved for merging. 

**TIP**: Some parts of the build, e.g., the HTML output and the document 
structure are cached. Therefore, your changes may not show in subsequent builds. 
Use the ``make clean`` command to clear the cache before building.

Submit a pull request
---------------------
You can't create a new branch in this repository. To create a pull request, 
your changes must be in a fork of this repository.

CI checks
~~~~~~~~~
Pull requests are subjected to multiple CI checks before they can be merged. 
These include checks for:

- Spelling
- Inclusive language 
- Deleted or moved files 
- Broken or timing out links 
- Signing of `Canonical's contributor licensing agreement <https://canonical.com/legal/contributors/agreement?type=individual>`_
- Ability to build with no errors or warnings 

If your pull request fails a CI check due to avoidable issues in your changes, 
you will be required to make the necessary changes to ensure your PR passes the 
relevant CI check.

It is considered good practice to run the checks locally to catch any errors
before submitting your PR and asking for a review. The commands you can use to
run checks locally include:

- ``make spelling``: Catch spelling errors or unrecognized words 
- ``make linkcheck-discrete``: Identify broken or timing out links 
- ``make woke``: Check for non-inclusive language 

Read more about the CI checks in the 
`upstream Starter pack documentation <https://canonical-starter-pack.readthedocs-hosted.com/stable/reference/automatic_checks/>`_.

Redirects
~~~~~~~~~

This documentation uses rediraffe to handle redirects. If your changes include 
moving, deleting, or renaming a file, add a redirect by adding the old and new 
paths in ``redirects.txt``. If a redirect is not added, the pull request will 
fail at least one CI check.

Review and approval
~~~~~~~~~~~~~~~~~~~
Pull requests can only be merged after being reviewed and approved by a user 
with  by a reviewer with write access. Currently, this means they must be a 
member of the Launchpad team.

Your PR may not be reviewed immediately after submission depending on certain 
factors, but the Launchpad team remains eager to collaborate with the community
and will try to address all issues and pull requests as soon as possible.

(Optional - Launchpad team only) Synchronise GitHub issues to Jira
------------------------------------------------------------------

If you wish to sync issues from your documentation repository on GitHub to your
Jira board, configure the `GitHub/Jira sync bot
<https://github.com/canonical/gh-jira-sync-bot>`_ by editing the
``.github/workflows/.jira_sync_config.yaml`` file appropriately. In addition to
updating this file, you must also apply server configuration for this feature to
work. For more information, see `server configuration details
<https://github.com/canonical/gh-jira-sync-bot#server-configuration>`_ for the
GitHub/Jira sync bot.

The ``.jira_sync_config.yaml`` file that is included in the starter pack
contains configuration for syncing issues from the starter pack repository to
its documentation Jira board. Therefore, it does not work out of the box for
other repositories in GitHub, and you must update it if you want to use the
synchronisation feature.
