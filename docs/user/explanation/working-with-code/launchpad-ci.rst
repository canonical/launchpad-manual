.. _continuous-integration:

Continuous Integration
======================

.. include:: /includes/important_not_revised_help.rst

Launchpad CI tries to make software development and collaboration
easier.

Use Launchpad CI to catch bugs before they go into main/master, enforce
coding standards by running linters, or make sure your project's
documentation is still building - or all three of them.

How does this work?
-------------------

1. create a ``.launchpad.yaml`` with your desired configuration
2. add it to your repository
3. ``git push`` to Launchpad 

Launchpad will build/test/lint/etc. your project.

After the run Launchpad will report the status of the build in the UI
via a green checkmark or a red cross.

In case of an error you will additionally receive an email.

Documentation
-------------

You can find the syntax for the configuration file at
https://lpci.readthedocs.io/en/latest/configuration.html.

Feature Requests / Known Issues
-------------------------------

Please note that Launchpad CI still has some rough edges.

You can have a look the `currently known
issues <https://bugs.launchpad.net/lpci>`__. Please let us know when you
miss a feature or encounter a bug.

Support
-------

Employees of Canonical can get support at the Launchpad channel on
Mattermost. External users can use the usual :ref:`channels <get-help>`.
