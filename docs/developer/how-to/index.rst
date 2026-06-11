.. meta::
   :description: Comprehensive how-to guides for Launchpad development covering 
      setup, common tasks, development tips, and operational procedures.

How-to guides
=============

Instructions to take you through common processes for Launchpad developers, from
creating a local setup and contributing changes, to operating and debugging the
platform. 

Get started
-----------

To get started with Launchpad development, you'll need to get the source code
and run a local Launchpad instance. You can also set up buildd and Soyuz to
enable local builds.

- :ref:`Get the Launchpad source code <get-the-source-code>`
- :ref:`Run Launchpad locally with quick set up <set-up-and-run-launchpad-quickstart>`
- :ref:`Run Launchpad locally with advanced set up <set-up-and-run-launchpad-advanced>`
- :ref:`Set up the database <database-setup>`
- :ref:`Deploy Soyuz locally <use-soyuz-locally>`
- :ref:`Develop with Buildd <develop-with-buildd>`

Operate Launchpad
-----------------

Managing a running Launchpad instance involves monitoring the build farm,
checking frontend availability, triaging bugs, administering users, and
shipping changes to production.

- :ref:`Get overview of build farm <get-overview-of-build-farm>`
- :ref:`Check availability of frontends <check-availability-of-frontends>`
- :ref:`Manage users and teams in development environments <manage-users-and-teams-in-development-environments>`
- :ref:`Create job to publish artifact <create_job_to_publish_artifacts>`
- :ref:`Triage Launchpad project bugs <triaging-launchpad-project-bugs>`
- :ref:`Land updates for Loggerhead <land-updates-loggerhead>`
- :ref:`Build and publish Launchpad development LXD images <build-and-publish-launchpad-development-lxd-images>`
- :ref:`Use lp-shell <how-to-use-lp-shell>`

Common development tasks
------------------------

The Launchpad development cycle involves fixing bugs, contributing and
reviewing changes, updating dependencies, and keeping the database schema
current.

- :ref:`Fix bugs <fixing-bugs>`
- :ref:`Contribute changes <contributing-changes>`
- :ref:`Use an updated dependency <use-updated-dependency>`
- :ref:`Database schema changes process <database-schema-changes-process>`
- :ref:`Apply database schema changes <apply-database-schema-changes>`
- :ref:`Import an Ubuntu package <import-ubuntu-package>`

Launchpad development tips
--------------------------

This section covers a range of helpful techniques for Launchpad development:
writing and configuring tests, handling exceptions and security policies,
running codehosting locally, generating API docs, and working with the
database.

- :ref:`Update the global configuration for tests <update-global-configuration-for-tests>`
- :ref:`Handle security policies <handle-security-policies>`
- :ref:`Test CLI scripts <test-cli-scripts>`
- :ref:`Handle exceptions <handle-exceptions>`
- :ref:`Preserve query count <preserve-query-count>`
- :ref:`Run Launchpad with Chameleon template engine <run-launchpad-with-chameleon-template-engine>`
- :ref:`Generate Launchpad API docs <launchpad-api-docs-generation>`
- :ref:`Use codehosting locally <use-codehosting-locally>`
- :ref:`Rename a database table <rename-database-table>`
- :ref:`Use MockIo library <mockio-library>`

Debug
-----

Launchpad's layered architecture means bugs can surface far from their origin.
Visual Studio Code has features that can be useful when debugging. Using ``pdb``
breakpoints to debug pagetests can make your development experience easier.
However, you can also run into some issues when using breakpoints to
troubleshoot across multiple test layers.

- :ref:`Debug tests with Visual Studio Code <debug-with-visual-studio-code>`
- :ref:`Debug stories and pagetests <debug-stories-pagetests>`
- :ref:`Troubleshoot breakpoint issues when running multiple test layers <troubleshoot-breakpoints-tests>`

.. toctree::
   :hidden:

   get-started/index
   operate-launchpad/index
   common-development-tasks/index
   launchpad-development-tips/index
   debug/index
