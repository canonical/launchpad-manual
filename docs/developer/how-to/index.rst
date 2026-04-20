.. meta::
   :description: Comprehensive how-to guides for Launchpad development covering 
      setup, common tasks, development tips, and operational procedures.

How-to guides
=============

These how-to guides take you through common processes for Launchpad developers, 
from creating a local setup and contributing changes, to operating and 
debugging the platform. 

Get started
-----------

To get started with Launchpad, you'll need to get the source code and run a 
local development instance. You can also set up buildd and Soyuz to enable 
building using your local Launchpad instance.

- :ref:`Get the Launchpad source code <get-the-source-code>`
- :ref:`Run Launchpad locally with quick set up <set-up-and-run-launchpad-quickstart>`
- :ref:`Run Launchpad locally with advanced set up <set-up-and-run-launchpad-advanced>`
- :ref:`Database set up <database-setup>`
- :ref:`Deploy Soyuz locally <use-soyuz-locally>`
- :ref:`Develop with Buildd <develop-with-buildd>`

Operate Launchpad
-----------------

Once you have your own instance of Launchpad up and running, there are some 
common tasks you may need to undertake such as observing the build farm, 
checking the availability of frontends, triaging bugs, deploying changes to 
production, etc.

- :ref:`Get overview of build farm <get-overview-of-build-farm>`
- :ref:`Check availability of frontends <check-availability-of-frontends>`
- :ref:`Manage users and teams in development environments <manage-users-and-teams-in-development-environments>`
- :ref:`Create job to publish artifact <create_job_to_publish_artifacts>`
- :ref:`Triage Launchpad project bugs <triaging-launchpad-project-bugs>`
- :ref:`Land updates for Loggerhead <land-updates-loggerhead>`
- :ref:`Transfer ownership of a project <transfer-ownership-of-a-project>`
- :ref:`Port builders to newer Ubuntu versions <port-builders-to-newer-ubuntu-versions>`
- :ref:`Build and publish Launchpad development LXD images <build-and-publish-launchpad-development-lxd-images>`
- :ref:`Use lp-shell <how-to-use-lp-shell>`

Common development tasks
------------------------

As a Launchpad developer, there is plenty you can do to contribute to the teams
development efforts including fixing bugs and contributing features changes. 
You may also need to import Ubuntu packages and applying database schema 
changes.

- :ref:`Fix bugs <fixing-bugs>`
- :ref:`Contribute changes <contributing-changes>`
- :ref:`Use an updated dependency <use-updated-dependency>`
- :ref:`Database schema changes process <database-schema-changes-process>`
- :ref:`Apply database schema changes <apply-database-schema-changes>`
- :ref:`Import an Ubuntu package <import-ubuntu-package>`

Launchpad development tips
--------------------------

Developing for Launchpad can be challenging, but there are different ways you
can make things easier such as understanding how to debug and using specific 
tools for this, understanding how to test Launchpad scripts, using breakpoints, 
etc.

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
Launchpad has many moving parts and identifying the source of an error isn't 
always straightforward. There are a some ways to simplify debugging efforts.

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
