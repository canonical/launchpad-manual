.. meta::
   :description: How to measure Launchpad test coverage locally, including
      running the tests under coverage.py and reading the reports.

.. _measure-test-coverage:

Measuring test coverage
=======================

Coverage tells you which lines of the code under test your run actually
exercised. Launchpad measures it with coverage.py, through ``bin/test
--coverage-py``, which gives you branch coverage, terminal and HTML reports,
and per-module filtering.

Run the tests under coverage
----------------------------

Add ``--coverage-py`` to any ``bin/test`` command:

.. code-block:: bash

   bin/test --coverage-py -vvc -t <test-pattern>

The run leaves one ``.coverage.*`` data file per process at the top of the
tree.

Set ``COVERAGE_FILE`` to an absolute path if you would rather keep them
somewhere else:

.. code-block:: bash

   COVERAGE_FILE=/tmp/lpcov/.coverage bin/test --coverage-py -vvc -t <pattern>

Read the report
---------------

Merge the per-process data files, then generate a report. Run these from the top
of the tree:

.. code-block:: bash

   # Merge the .coverage.* files into a single .coverage.
   env/bin/coverage combine

   # Terminal table; -m lists the line numbers that were missed.
   env/bin/coverage report -m --include='lib/lp/*'

   # Browsable report in htmlcov/index.html.
   env/bin/coverage html --include='lib/lp/*'

Narrow ``--include`` to the code your change touches. A report over all of
``lib/lp`` is dominated by modules that were merely imported, which makes the
percentages meaningless.

``coverage combine`` adds to data that is already in ``.coverage``, so delete it
first if you do not want to accumulate several runs into one report:

.. code-block:: bash

   rm -f .coverage .coverage.*

.. warning::

   Coverage numbers only describe the tests you selected with ``-t``. A line
   reported as missed may well be covered by a test elsewhere in the suite, so
   read these reports as "did *my* tests reach this code", not as a claim about
   dead code.
