.. meta::
   :description: Learn how to test different Launchpad changes locally.

.. _testing-launchpad-changes:

Testing
=======

.. include:: ../../../includes/important_not_revised.rst

Testing your Launchpad changes
------------------------------

The normal pattern for testing your changes is to run the tests you *think*
will be affected locally, but fundamentally we rely on post-merge testing by
`buildbot <https://buildbot.net/>`__.

For how to run the test suite locally — including selecting specific tests and
layers, speeding up runs, and running browser tests headless — see
:ref:`running-tests`.

Testing Launchpad translations
------------------------------

-  Rosetta admin user - translations-deity@example.com
-  Pagetest browser setup for Rosetta Administrators
   rosetta_admin_browser = setupRosettaExpertBrowser()
-  Pagetest browser setup for Ubuntu Translation Administrators
   ubuntu_admin_browser = setupDTCBrowser()

Performance and stress tests
----------------------------

Populate the DB
~~~~~~~~~~~~~~~

To add object into the database you can use:

::

   & env LP_DBNAME="launchpad_dev" make iharness
   from canonical.lp import initZopeless
   zl = initZopeless()
   #
   # use the factory here
   #
   zl.commit()

Writing tests
-------------

For each part of an application there are 2 level of testing:

-  unit testing

   -  comprehensive testing, including cornerstone cases
   -  written in python files (try to avoid doctest)

-  smoke/functional/integration testing

   -  testing normal use cases
   -  written using doctest format

Model
~~~~~

1. Unit testing

   -  Files locate in lib/lp//scripts/tests

2. Integration testing

   -  Files locate in lib/lp//doc

View
----

1. Unit/integration testing

   -  Files locate in lib/lp//browser/tests
   -  More details: ViewTests

2. Smoke testing

   -  Files locate in lib/lp//stories
   -  More details: PageTests

JavaScript
----------

1. Unit testing

   More details: TestingJavaScript JavascriptUnitTesting

2. XHR integration testing

   -  Use sparingly.
   -  We use YUI tests with a full appserver behind it.
   -  See standard_yuixhr_test_template.js and
      standard_yuixhr_test_template.py in the root of the Launchpad
      tree.

Scripts
-------

-  Files locate in lib/lp//scripts/tests

API
---

-  Files located in lib/lp//stories/webservices
-  More details: TestingWebServices
