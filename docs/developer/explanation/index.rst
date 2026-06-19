.. meta::
   :description: Documentation covering Launchpad ideas, setup, 
      framework, parts, best practices, and deployment processes.

Explanation
===========

Launchpad is a large platform built over many years. These pages explain the
ideas behind the project, its components, and the best practices its developers
follow.

The ideas behind Launchpad
--------------------------

Launchpad connects the people who make software with users and other developers,
and offers the resources they need to make their software available.
Understanding why Launchpad exists, whom it serves, and the values that guide
it provides the context for everything else.

- :ref:`What is Launchpad? <what-is-launchpad>`
- :ref:`About Launchpad security <about-launchpad-security>`
- :ref:`Launchpad strategy <launchpad-strategy>`
- :ref:`Launchpad values <launchpad-values>`


Core components and setup
-------------------------

Launchpad is made up of many components. Knowing how these pieces fit together
helps you navigate the codebase, and design and test your changes.

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

Launchpad uses PostgreSQL and depends on PostgreSQL-specific features. Its
schema is patched on a live system and managed by Storm, the ORM Launchpad uses.

- :ref:`Database performance <database-performance>`
- :ref:`Live database patching <live-database-patching>`
- :ref:`PostgreSQL and Launchpad <postgresql-and-launchpad>`
- :ref:`Storm migration guide <storm-migration-guide>`
- :ref:`Working with db-devel <working-with-db-devel>`

Developing for the Launchpad project
------------------------------------

Contributing to Launchpad means working across several branches, guarding new
behaviour behind feature flags, and guiding each change through review and
into production. This day-to-day development is expected to follow specific
processes and conventions.

- :ref:`About Launchpad branches <about-launchpad-branches>`
- :ref:`Datetime usage guide <datetime-usage-guide>`
- :ref:`Error explanations <error-explanations>`
- :ref:`Feature flags <feature-flags>`
- :ref:`Hacking <hacking-guide>`
- :ref:`Journey of a change to production <journey-change-production>`
- :ref:`Pre merge reviews <pre-merge-reviews>`
- :ref:`XXX policy <xxx-policy>`

Best practices for development
------------------------------

Launchpad aims to be fast and always available. It should also be safe to
change parts of it with a low risk of breaking other parts of the system. These
principles inform how its code is structured, how performance and permissions
are handled, and how its templates and tests are written.

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

Launchpad's front end is written in JavaScript built on the YUI library, with
its own build system and both unit and integration test frameworks.

- :ref:`JavaScript build system <javascript-build-system>`
- :ref:`Integration testing in JavaScript <integration-testing-in-javascript>`
- :ref:`Developing with YUI Test <developing-with-yui-test>`


Static assets
-------------

Launchpad's visual style comes from CSS and images that are compiled and
optimized as part of the build using CSS sprites.

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
