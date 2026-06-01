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
  :doc:`Get the Launchpad source code <how-to/get-started/get-source-code>` •
  :doc:`Run Launchpad locally with quick setup <how-to/get-started/running-quickstart>` •
  :doc:`Run Launchpad locally with advanced setup <how-to/get-started/running>` •
  :doc:`Database setup <how-to/get-started/database-setup>`
* **Local deployment**:
  :doc:`Deploy Soyuz locally <how-to/get-started/use-soyuz-locally>` •
  :doc:`Develop with Buildd <how-to/get-started/develop-with-buildd>` •
  :doc:`Use codehosting locally <how-to/launchpad-development-tips/codehosting-locally>`

Day-to-day development
~~~~~~~~~~~~~~~~~~~~~~

Guidelines and instructions for routine development tasks, from fixing bugs to
submitting database schema changes. Explore common workflows and processes
required to implement and ship changes in Launchpad.

* **Workflows**:
  :doc:`Contribute changes <how-to/common-development-tasks/contributing-changes>` •
  :doc:`Creating a new page in Launchpad <tutorials/creating-a-page-in-launchpad>` •
  :doc:`About Launchpad branches <explanation/developing-for-launchpad/branches>` •
  :doc:`Pre merge reviews <explanation/developing-for-launchpad/pre-merge-reviews>` •
  :doc:`Journey of a change to production <explanation/developing-for-launchpad/journey-of-a-change-to-production>`
* **Database changes**:
  :doc:`Database schema changes process <how-to/common-development-tasks/database-schema-changes-process>` •
  :doc:`Apply database schema changes <how-to/common-development-tasks/apply-schema-changes>`
* **Common tasks**:
  :doc:`Fix bugs <how-to/common-development-tasks/fixing-bugs>` •
  :doc:`Use an updated dependency <how-to/common-development-tasks/use-updated-dependency>` •
  :doc:`Handle exceptions <how-to/launchpad-development-tips/exceptions>` •
  :doc:`Handle security policies <how-to/launchpad-development-tips/security>` •
  :doc:`Datetime usage guide <explanation/developing-for-launchpad/datetime-usage>` •
  :doc:`Error explanations <explanation/developing-for-launchpad/error-explanations>` •
  :doc:`Feature flags <explanation/developing-for-launchpad/feature-flags>`

Operating Launchpad
~~~~~~~~~~~~~~~~~~~

Manage, maintain, and monitor Launchpad services and environments in real time,
including operating the build farm, checking frontend availability, user
management, and utilizing diagnostic CLI tools.

* **Build farm & publishing**:
  :doc:`Get overview of build farm <how-to/operate-launchpad/getting-overview-of-build-farm>` •
  :doc:`Create a job to publish an artifact <how-to/operate-launchpad/create-job-publish-artifact>`
* **Environment administration**:
  :doc:`Check availability of frontends <how-to/operate-launchpad/checking-availability-of-launchpad-frontends>` •
  :doc:`Manage users and teams in development environments <how-to/operate-launchpad/manage-users>` •
  :doc:`Build and publish Launchpad development LXD images <how-to/operate-launchpad/building-lpdev-images>`
* **Bugs**:
  :doc:`Triage Launchpad project bugs <how-to/operate-launchpad/triage-bugs>` •
  :doc:`Tagging bugs about Launchpad <reference/bug-tags>`
* **Diagnostic tools**:
  :doc:`Use lp-shell <how-to/operate-launchpad/use-lp-shell>` •
  :doc:`Generate Launchpad API docs <how-to/launchpad-development-tips/launchpad-api-docs>`

Testing, debugging and troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify the quality of your code and resolve issues effectively using
Launchpad's testing and debugging suites. Learn how to execute tests,
troubleshoot breakpoints, and integrate debugging tools into VS Code.

* **Debugging**:
  :doc:`Debug tests with Visual Studio Code <how-to/debug/debug-with-visual-studio-code>` •
  :doc:`Debug stories and pagetests <how-to/debug/debugging>` •
  :doc:`Troubleshoot breakpoint issues when running multiple test layers <how-to/debug/troubleshoot-breakpoint-issues-when-running-tests>`
* **Testing**:
  :doc:`Testing Launchpad changes <explanation/core-components-and-set-up/testing>` •
  :doc:`Update the global configuration for tests <how-to/launchpad-development-tips/update-configuration-for-testing>` •
  :doc:`Test CLI scripts <how-to/launchpad-development-tips/testing-scripts>` •
  :doc:`Tests style guide <reference/tests>`

Core concepts and architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Understand the foundational design, vision, and internal architecture that
power Launchpad. Explore the philosophical goals, values, and essential
components that define the framework and its application flow.

* **Vision & values**:
  :doc:`What is Launchpad? <explanation/ideas-behind-launchpad/scope>` •
  :doc:`Launchpad values <explanation/ideas-behind-launchpad/values>` •
  :doc:`Launchpad strategy <explanation/ideas-behind-launchpad/strategy>` •
  :doc:`About Launchpad security <explanation/ideas-behind-launchpad/security>`
* **Internal components**:
  :doc:`Navigation menus <explanation/core-components-and-set-up/parts-of-launchpad/navigation-menus>` •
  :doc:`URL traversal <explanation/core-components-and-set-up/parts-of-launchpad/url-traversal>` •
  :doc:`Registry <explanation/core-components-and-set-up/parts-of-launchpad/registry>` •
  :doc:`Engineering overview translations <explanation/core-components-and-set-up/parts-of-launchpad/engineering-overview-translations>`
* **Framework & environment**:
  :doc:`Application framework <explanation/core-components-and-set-up/framework>` •
  :doc:`Code concepts <explanation/core-components-and-set-up/concepts>` •
  :doc:`The Launchpad PPA <explanation/core-components-and-set-up/launchpad-ppa>` •
  :doc:`Navigating the tree <explanation/core-components-and-set-up/navigating>` •
  :doc:`Launchpad pip integration <explanation/core-components-and-set-up/pip>` •
  :doc:`Launchpad installation details <explanation/core-components-and-set-up/running-details>` •
  :doc:`Building live filesystems <explanation/core-components-and-set-up/building-live-filesystems>`

Database
~~~~~~~~

Explore Launchpad's relational database layer, its performance optimization
strategies, and schema management practices. Understand workflows for executing
database migrations, renaming tables, and maintaining query efficiency.

* **Relational database fundamentals**:
  :doc:`Database overview <explanation/database/index>` •
  :doc:`PostgreSQL and Launchpad <explanation/database/postgresql>` •
  :doc:`Storm migration guide <explanation/database/storm-migration-guide>` •
  :doc:`Working with db-devel <explanation/database/working-with-db-devel>`
* **Performance & optimization**:
  :doc:`Database performance <explanation/database/database-performance>` •
  :doc:`Live database patching <explanation/database/live-patching>` •
  :doc:`Preserve query count <how-to/launchpad-development-tips/preserve-query-count>`
* **Schema management**:
  :doc:`Rename a database table <how-to/launchpad-development-tips/rename-database-table>`

Development best practices
~~~~~~~~~~~~~~~~~~~~~~~~~~

Coding style guides, architectural rules, and security policies used to
maintain the quality of the codebase, from use of assertions to preferred
Python conventions.

* **Standards & guidelines**:
  :doc:`Architectural guide <explanation/development-best-practices/architecture>` •
  :doc:`Python style guide <reference/python>` •
  :doc:`XXX policy <explanation/developing-for-launchpad/xxx-policy>` •
  :doc:`Assertions in Launchpad <explanation/development-best-practices/assertions-in-launchpad>` •
  :doc:`Launchpad permissions <explanation/development-best-practices/security-policy>`
* **Process & infrastructure**:
  :doc:`Bug triage process background <explanation/development-best-practices/bug-triage-process-background>` •
  :doc:`Charm development <explanation/development-best-practices/charms>` •
  :doc:`Code import in depth <explanation/development-best-practices/codeimport>`
* **Testing & UI reuse**:
  :doc:`Page tests <explanation/development-best-practices/page-tests>` •
  :doc:`About Launchpad performance <explanation/development-best-practices/performance>` •
  :doc:`Template reuse <explanation/development-best-practices/template-reuse>`

Frontend development
~~~~~~~~~~~~~~~~~~~~

Build and test Launchpad's client-side user interface using standard assets and
frameworks. Understand the JavaScript build system, styling standards, and
testing interfaces.

* **JavaScript & testing**:
  :doc:`JavaScript build system <explanation/javascript/javascript-buildsystem>` •
  :doc:`Integration testing in JavaScript <explanation/javascript/javascript-integration-testing>` •
  :doc:`Developing with YUI Test <explanation/javascript/javascript-unittesting>` •
  :doc:`Use MockIo library <how-to/launchpad-development-tips/mockio>`
* **Static assets & styling**:
  :doc:`Static assets overview <explanation/static-assets/index>` •
  :doc:`CSS <explanation/static-assets/css>` •
  :doc:`CSS sprites <explanation/static-assets/css-sprites>` •
  :doc:`Favicons <explanation/static-assets/favicon>` •
  :doc:`Images <explanation/static-assets/images>` •
  :doc:`CSS style guide <reference/css>`

Services and components
~~~~~~~~~~~~~~~~~~~~~~~

Background services and standalone modules that support Launchpad including the
build farm, git/code hosting, mail services, and packaging pipelines.

* **Build & package pipelines**:
  :doc:`Build farm <reference/services/build-farm>` •
  :doc:`Signing service <reference/services/signing>` •
  :doc:`Fetch service <reference/services/fetch-service>` •
  :doc:`Buildbot <reference/services/buildbot>` •
  :doc:`Ubuntu package publishing <explanation/core-components-and-set-up/publisher/ubuntu-package-publishing>` •
  :doc:`Ubuntu archive publisher <explanation/core-components-and-set-up/publisher/ubuntu-archive-publisher>`
* **Code & git hosting**:
  :doc:`Git hosting <reference/services/git-hosting>` •
  :doc:`Code import <reference/services/code-import>` •
  :doc:`Code <explanation/core-components-and-set-up/parts-of-launchpad/code>`
* **Infrastructure services**:
  :doc:`Automatic translations tarball exports <reference/services/automatic-translations-export>` •
  :doc:`Mirror prober <reference/services/mirror-prober>` •
  :doc:`Ubuntu mirrors index <reference/services/ubuntu-mirrors-index>` •
  :doc:`Malone <explanation/core-components-and-set-up/parts-of-launchpad/malone>`
* **Mail services**:
  :doc:`Launchpad public mailing lists archives <reference/services/mailing-lists-archives>` •
  :doc:`Launchpad and email <reference/email>` •
  :doc:`Mail <explanation/core-components-and-set-up/parts-of-launchpad/mail>`

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
