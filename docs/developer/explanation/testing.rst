Testing
=======

.. include:: ../../includes/important_not_revised.rst

Testing Your Launchpad Changes
------------------------------

General usage
~~~~~~~~~~~~~

The normal pattern for testing your changes is to run the tests you
*think* will be affected locally, but fundamentally we rely on
post-merge testing by `buildbot <http://lpbuildbot.canonical.com/>`__.

Iterating with testrepository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   apt-get install testrepository
   #cd $yourlaunchpaddevdir
   testr init

Don't worry about creating a .testr.conf file; the defaults created for
you works fine.

To run all the tests:

::

   testr run

To run an individual test using the \`-t PATTERN\` option:

::

   testr run -- -t foo

To see the current known failures:

::

   testr failing

To run just the known failing tests:

::

   testr run --failing

To re-run the tests:

::

   testr run --failing

To see the current failing tests

::

   testr failing

testr is moving and bug reports and patches are accepted :).

Running old school
~~~~~~~~~~~~~~~~~~

To run the tests, you run the

::

   ./bin/test

script, which is produced by

::

   make build

You can see all the options you have by running

::

   ./bin/test --help

Usually you will run

::

   ./bin/test -vvct PATTERN

where

::

   PATTERN

is a regular expression that is used to filter the tests that will be
run.

You can use '!PATTERN' to match all expression not matching that patter.
Ex, to run all test, except the one at Windmill layer you can use:

::

   ./bin/test -vvc --layer '!Windmill'

Speed up the tests
~~~~~~~~~~~~~~~~~~

Since Librarian and MemCache does not change often and they take a long
time to be started and shutdown, ./bin/test can leave them started by
using this command:

::

    
   LP_PERSISTENT_TEST_SERVICES=1 ./bin/test PATTERN 

You can kill them using

::

    ./bin/kill-test-services 

When running tests written in python files, and you only want to test a
file, you can speed up the test by specifying the full path to the
python file:

::

   LP_PERSISTENT_TEST_SERVICES=1 ./bin/test PATH/TO/PYTHON/TEST/FILE.py

See `this
mail <https://web.archive.org/web/20210620040705/https://lists.launchpad.net/launchpad-dev/msg02780.html>`__ 
for more.

Headless tests
~~~~~~~~~~~~~~

-  If you are running browser tests on a machine without an X server,
   you can use xvfb-run:

::

   xvfb-run -s '-screen 0 1024x768x24' bin/test YOUR_TEST_ARGUMENTS

Testing Launchpad Translations
------------------------------

-  Rosetta admin user - translations-deity@example.com
-  Pagetest browser setup for Rosetta Administrators
   rosetta_admin_browser = setupRosettaExpertBrowser()
-  Pagetest browser setup for Ubuntu Translation Administrators
   ubuntu_admin_browser = setupDTCBrowser()

Performance and stress tests
----------------------------

Populate the db
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

Javascript
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
