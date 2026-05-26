.. meta::
   :description: Comprehensive guide for Launchpad developers covering setup, 
      bug fixing, feature development, and contributing changes.

.. _launchpad-manual-for-developers:

Launchpad manual for developers
===============================

The Launchpad manual for developers is the most comprehensive resource for
anyone looking to contribute to `Launchpad <https://launchpad.net/>`_. 

We are always working to improve the user experience and other features of
this platform and we rely on contributors like you to make this happen. There  
are different ways to contribute to launchpad as a developer including 
**proposing new features, triaging and fixing bugs, and testing features.** 

This manual shows you how to handle different tasks from downloading the source
code and creating new pages to fixing bugs and contributing changes to 
Launchpad.

In this documentation
---------------------

Setup and first steps
~~~~~~~~~~~~~~~~~~~~~

Get started with Launchpad core development by downloading the source code,
running Launchpad locally, or even deploying Soyuz on your machine for local
builds.

* **Get started**:
  :ref:`Get the Launchpad source code <get-the-source-code>` •
  :ref:`Run Launchpad locally with quick setup <set-up-and-run-launchpad-quickstart>` •
  :ref:`Run Launchpad locally with advanced setup <set-up-and-run-launchpad-advanced>` •
  :ref:`Database setup <database-setup>`
* **Local deployment**:
  :ref:`Deploy Soyuz locally <use-soyuz-locally>` •
  :ref:`Develop with Buildd <develop-with-buildd>` •
  :ref:`Use codehosting locally <use-codehosting-locally>`

Day-to-day development
~~~~~~~~~~~~~~~~~~~~~~

Guidelines and instructions for routine development tasks, from fixing bugs to
submitting database schema changes. Explore common workflows and processes
required to implement and ship changes in Launchpad.

* **Workflows**:
  :ref:`Contribute changes <contributing-changes>` •
  :ref:`Creating a new page in Launchpad <tutorial-creating-page-in-launchpad>` •
  :ref:`About Launchpad branches <about-launchpad-branches>` •
  :ref:`Pre merge reviews <pre-merge-reviews>` •
  :ref:`Journey of a change to production <journey-change-production>`
* **Database changes**:
  :ref:`Database schema changes process <database-schema-changes-process>` •
  :ref:`Apply database schema changes <apply-database-schema-changes>`
* **Common tasks**:
  :ref:`Fix bugs <fixing-bugs>` •
  :ref:`Use an updated dependency <use-updated-dependency>` •
  :ref:`Handle exceptions <handle-exceptions>` •
  :ref:`Handle security policies <handle-security-policies>` •
  :ref:`Datetime usage guide <datetime-usage-guide>` •
  :ref:`Error explanations <error-explanations>` •
  :ref:`Feature flags <feature-flags>`

Operating Launchpad
~~~~~~~~~~~~~~~~~~~

Manage, maintain, and monitor Launchpad services and environments in real time,
including operating the build farm, checking frontend availability, user
management, and utilizing diagnostic CLI tools.

* **Build farm & publishing**:
  :ref:`Get overview of build farm <get-overview-of-build-farm>` •
  :ref:`Create a job to publish an artifact <create_job_to_publish_artifacts>`
* **Environment administration**:
  :ref:`Check availability of frontends <check-availability-of-frontends>` •
  :ref:`Manage users and teams in development environments <manage-users-and-teams-in-development-environments>` •
  :ref:`Build and publish Launchpad development LXD images <build-and-publish-launchpad-development-lxd-images>`
* **Bugs**:
  :ref:`Triage Launchpad project bugs <triaging-launchpad-project-bugs>` •
  :ref:`Tagging bugs about Launchpad <tagging-bugs-about-launchpad>`
* **Diagnostic tools**:
  :ref:`Use lp-shell <how-to-use-lp-shell>` •
  :ref:`Generate Launchpad API docs <launchpad-api-docs-generation>`

Testing, debugging and troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify the quality of your code and resolve issues effectively using
Launchpad's testing and debugging suites. Learn how to execute tests,
troubleshoot breakpoints, and integrate debugging tools into VS Code.

* **Debugging**:
  :ref:`Debug tests with Visual Studio Code <debug-with-visual-studio-code>` •
  :ref:`Debug stories and pagetests <debug-stories-pagetests>` •
  :ref:`Troubleshoot breakpoint issues when running multiple test layers <troubleshoot-breakpoints-tests>`
* **Testing**:
  :ref:`Testing Launchpad changes <testing-launchpad-changes>` •
  :ref:`Update the global configuration for tests <update-global-configuration-for-tests>` •
  :ref:`Test CLI scripts <test-cli-scripts>` •
  :ref:`Tests style guide <tests-style-guide>`

Core concepts and architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Understand the foundational design, vision, and internal architecture that
power Launchpad. Explore the philosophical goals, values, and essential
components that define the framework and its application flow.

* **Vision & values**:
  :ref:`What is Launchpad? <what-is-launchpad>` •
  :ref:`Launchpad values <launchpad-values>` •
  :ref:`Launchpad strategy <launchpad-strategy>` •
  :ref:`About Launchpad security <about-launchpad-security>`
* **Internal components**:
  :ref:`Navigation menus <navigation-menus>` •
  :ref:`URL traversal <url-traversal>` •
  :ref:`Registry <developer-registry>` •
  :ref:`Engineering overview translations <engineering-overview-translations>`
* **Framework & environment**:
  :ref:`Application framework <application-framework>` •
  :ref:`Code concepts <code-concepts>` •
  :ref:`The Launchpad PPA <the-launchpad-ppa>` •
  :ref:`Navigating the tree <navigating-the-tree>` •
  :ref:`Launchpad pip integration <launchpad-pip-integration>` •
  :ref:`Launchpad installation details <launchpad-installation-details>` •
  :ref:`Building live filesystems <building-live-filesystems>`

Database
~~~~~~~~

Explore Launchpad's relational database layer, its performance optimization
strategies, and schema management practices. Understand workflows for executing
database migrations, renaming tables, and maintaining query efficiency.

* **Relational database fundamentals**:
  :ref:`Database overview <database-overview>` •
  :ref:`PostgreSQL and Launchpad <postgresql-and-launchpad>` •
  :ref:`Storm migration guide <storm-migration-guide>` •
  :ref:`Working with db-devel <working-with-db-devel>`
* **Performance & optimization**:
  :ref:`Database performance <database-performance>` •
  :ref:`Live database patching <live-database-patching>` •
  :ref:`Preserve query count <preserve-query-count>`
* **Schema management**:
  :ref:`Rename a database table <rename-database-table>`

Development best practices
~~~~~~~~~~~~~~~~~~~~~~~~~~

Coding style guides, architectural rules, and security policies used to
maintain the quality of the codebase, from use of assertions to preferred
Python conventions.

* **Standards & guidelines**:
  :ref:`Architectural guide <architectural-guide>` •
  :ref:`Python style guide <python-style-guide>` •
  :ref:`XXX policy <xxx-policy>` •
  :ref:`Assertions in Launchpad <assertions-in-launchpad>` •
  :ref:`Launchpad permissions <launchpad-permissions>`
* **Process & infrastructure**:
  :ref:`Bug triage process background <bug-triage-process-background>` •
  :ref:`Charm development <charm-development>` •
  :ref:`Code import in depth <code-import-in-depth>`
* **Testing & UI reuse**:
  :ref:`Page tests <page-tests>` •
  :ref:`About Launchpad performance <about-launchpad-performance>` •
  :ref:`Template reuse <template-reuse>`

Frontend development
~~~~~~~~~~~~~~~~~~~~

Build and test Launchpad's client-side user interface using standard assets and
frameworks. Understand the JavaScript build system, styling standards, and
testing interfaces.

* **JavaScript & testing**:
  :ref:`JavaScript build system <javascript-build-system>` •
  :ref:`Integration testing in JavaScript <integration-testing-in-javascript>` •
  :ref:`Developing with YUI Test <developing-with-yui-test>` •
  :ref:`Use MockIo library <mockio-library>`
* **Static assets & styling**:
  :ref:`Static assets overview <static-assets-overview>` •
  :ref:`CSS <launchpad-css>` •
  :ref:`CSS sprites <use-css-sprites>` •
  :ref:`Favicons <launchpad-favicons>` •
  :ref:`Images <launchpad-images>` •
  :ref:`CSS style guide <css-style-guide>`

Services and components
~~~~~~~~~~~~~~~~~~~~~~~

Background services and standalone modules that support Launchpad including the
build farm, git/code hosting, mail services, and packaging pipelines.

* **Build & package pipelines**:
  :ref:`Build farm <build-farm-reference>` •
  :ref:`Signing service <signing-service>` •
  :ref:`Fetch service <fetch-service>` •
  :ref:`Buildbot <buildbot-reference>` •
  :ref:`Ubuntu package publishing <ubuntu-package-publishing>` •
  :ref:`Ubuntu archive publisher <ubuntu-archive-publisher>`
* **Code & git hosting**:
  :ref:`Git hosting <git-hosting-reference>` •
  :ref:`Code import <code-import-reference>` •
  :ref:`Code <code-hosting>`
* **Infrastructure services**:
  :ref:`Automatic translations tarball exports <automatic-translations-export>` •
  :ref:`Mirror prober <mirror-prober-reference>` •
  :ref:`Ubuntu mirrors index <ubuntu-mirrors-index>` •
  :ref:`Malone <malone>`
* **Mail services**:
  :ref:`Launchpad public mailing lists archives <mailing-lists-archives>` •
  :ref:`Launchpad and email <email-reference>` •
  :ref:`Mail <launchpad-mail>`

How this documentation is organized
-----------------------------------

This documentation uses the
`Diátaxis documentation structure <https://diataxis.fr/>`_.

- The :doc:`Tutorial <tutorials/index>` takes you step-by-step through common
  development tasks in Launchpad.
- :doc:`How-to guides <how-to/index>` assume you have basic familiarity with
  Launchpad. They cover setting up a development environment, contributing
  changes, and operating a Launchpad instance.
- :doc:`Reference <reference/index>` provides specifications of Launchpad services and coding style guides.
- :doc:`Explanation <explanation/index>` includes background on key concepts,
  development best practices, and the deployment process of Launchpad.


.. toctree::
   :hidden:

   tutorials/index
   how-to/index
   reference/index
   explanation/index
