.. meta::
   :description: Explanation documentation covering Launchpad ideas, setup, 
      framework, parts, best practices, and deployment processes.

Explanation
===========

Launchpad is a large project developed over many years. The explanation 
documentation take you through the ideas behind its development, the different 
parts that make up the platform, how typical Launchpad developers approach 
their roles, and more.

The ideas behind Launchpad
---------------------------

Explore these pages for an overview of the concepts and motivations behind the 
Launchpad project. 

- :ref:`What is Launchpad? <what-is-launchpad>`
- :ref:`About Launchpad security <about-launchpad-security>`
- :ref:`Launchpad strategy <launchpad-strategy>`
- :ref:`Launchpad values <launchpad-values>`


Understand the Launchpad set up and components
----------------------------------------------

To make meaningful contributions to the project, you'll need to understand how 
Launchpad is installed and configured, how to navigate the codebase and test 
your changes. You should also understand the different components that make up
the application.

- :ref:`Parts of Launchpad <parts-of-launchpad>`
- :ref:`Publisher <explanation-publisher>`
- :ref:`Application framework <application-framework>`
- :ref:`Code concepts <code-concepts>`
- :ref:`The Launchpad PPA <the-launchpad-ppa>`
- :ref:`Navigating the tree <navigating-the-tree>`
- :ref:`Launchpad pip integration <launchpad-pip-integration>`
- :ref:`Launchpad installation details <launchpad-installation-details>`
- :ref:`Testing <testing-launchpad-changes>`
- :ref:`Building live filesystems <building-live-filesystems>`


Database
--------

This section gives an overview of how Launchpad interacts with the PostgreSQL 
database.

- :ref:`Database performance <database-performance>`
- :ref:`Live database patching <live-database-patching>`
- :ref:`PostgreSQL and Launchpad <postgresql-and-launchpad>`
- :ref:`Storm migration guide <storm-migration-guide>`
- :ref:`Working with db-devel <working-with-db-devel>`

Developing for the Launchpad project
------------------------------------

These pages help explain important aspects of the developer experience when 
you start contributing to Launchpad.

- :ref:`About Launchpad branches <about-launchpad-branches>`
- :ref:`Datetime usage guide <datetime-usage-guide>`
- :ref:`Error explanations <error-explanations>`
- :ref:`Feature flags <feature-flags>`
- :ref:`Hacking <hacking-guide>`
- :ref:`Journey of a change to production <journey-change-production>`
- :ref:`Pre merge reviews <pre-merge-reviews>`
- :ref:`XXX policy <xxx-policy>`

Best practices for development
-------------------------------

By using these principled approaches to development, you can improve Launchpad 
in a way that is sustainable and maintainable.

- :ref:`Architectural guide <architectural-guide>`
- :ref:`Assertions in Launchpad <assertions-in-launchpad>`
- :ref:`Bug triage process background <bug-triage-process-background>`
- :ref:`Charm development <charm-development>`
- :ref:`Code import in depth <code-import-in-depth>`
- :ref:`Page tests <page-tests>`
- :ref:`About Launchpad performance <about-launchpad-performance>`
- :ref:`Launchpad permissions <launchpad-permissions>`
- :ref:`Template reuse <template-reuse>`


JavaScript
----------

These pages explain how to develop, test, and build using the YUI Test 
framework.

- :ref:`JavaScript build system <javascript-build-system>`
- :ref:`Integration testing in JavaScript <integration-testing-in-javascript>`
- :ref:`Developing with YUI Test <developing-with-yui-test>`


Static assets
-------------

Launchpad's visual style is controlled by CSS and images that you set up and 
build.

- :ref:`CSS <launchpad-css>`
- :ref:`CSS sprites <use-css-sprites>`
- :ref:`Favicons <launchpad-favicons>`
- :ref:`Images <launchpad-images>`


.. toctree::
   :hidden:

   ideas-behind-launchpad/index
   core-components-and-set-up/index
   database/index
   developing-for-launchpad/index
   development-best-practices/index
   javascript/index
   static-assets/index
