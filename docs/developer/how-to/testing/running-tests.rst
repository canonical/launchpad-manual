.. meta::
   :description: How to run Launchpad's test suite locally, including running
      the whole suite, selecting specific tests and layers, and speeding up
      runs.

.. _running-tests:

=============
Running tests
=============

Launchpad has a large test suite. The normal pattern when developing is to run
locally the tests you *think* your change affects, and rely on post-merge
testing by `buildbot <https://buildbot.net/>`__ for full coverage.

There are two ways to run the tests:

- ``bin/test`` — the standard test runner, used by most of the team. Start
  here.
- ``testr`` (testrepository) — an alternative wrapper that some people prefer
  for iterating on failing tests.

.. note::

   Before you can run the tests, build the test runner once with ``make
   build``. This creates the ``bin/test`` script. See
   :ref:`set-up-and-run-launchpad-advanced` if you have not set up Launchpad
   yet.

.. tab-set::

   .. tab-item:: bin/test (recommended)

      .. rubric:: Run the whole suite

      From the top of the Launchpad tree:

      .. code-block:: bash

         xvfb-run bin/test -vvc

      The complete suite can take hours, depending on your machine, so you will
      usually want to narrow it down (see below).

      The ``-vvc`` options give verbose, coloured output. Run ``bin/test
      --help`` to see everything the runner accepts.

      .. rubric:: Run specific tests

      Use the ``-t`` option to select tests by pattern. The pattern is a regular
      expression matched against test names, and you can pass ``-t`` several
      times:

      .. code-block:: bash

         bin/test -vvc -t test-pattern-1 -t dotted.path.to.file

      You can also point the runner directly at a test file, which is the
      fastest way to iterate on a single module:

      .. code-block:: bash

         bin/test -vvc lib/lp/path/to/test_file.py

      .. rubric:: Select test layers

      Tests are grouped into *layers*. Use ``--layer`` to run only a given
      layer, and prefix a layer name with ``!`` to run everything *except* that
      layer:

      .. code-block:: bash

         # Run only the tests in LAYER.
         bin/test -vvc --layer 'LAYER'

         # Run everything except the tests in LAYER.
         bin/test -vvc --layer '!LAYER'

      .. rubric:: Speed up repeated runs

      The Librarian and memcached services are slow to start and stop and rarely
      change between runs. Set ``LP_PERSISTENT_TEST_SERVICES=1`` to leave them
      running between test runs:

      .. code-block:: bash

         LP_PERSISTENT_TEST_SERVICES=1 bin/test <test arguments>

      When you are done, stop the persistent services with:

      .. code-block:: bash

         bin/kill-test-services

      .. rubric:: Run browser tests without a display

      Some tests drive a browser and need an X server. On a machine without a
      display, run them under ``xvfb-run``:

      .. code-block:: bash

         xvfb-run -s '-screen 0 1024x768x24' bin/test <test arguments>

   .. tab-item:: testr (testrepository)

      ``testr`` is an alternative runner that some developers prefer for
      working through failing tests. You do not need to create a
      ``.testr.conf`` file; the defaults work.

      Install and initialise it once:

      .. code-block:: bash

         sudo apt-get install testrepository
         testr init

      Run the tests:

      .. code-block:: bash

         # Run all the tests.
         testr run

         # Run tests matching a pattern.
         testr run -- -t foo

         # Re-run only the tests that are currently failing.
         testr run --failing

      Inspect failures:

      .. code-block:: bash

         # List the currently known failures.
         testr failing
