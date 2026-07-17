.. meta::
   :description: Quick guide to profiling performance in Launchpad.

.. _profile-launchpad:

Profile Launchpad performance
==============================

Profiling helps you identify performance bottlenecks in Launchpad by measuring
where your code spends time during execution. Launchpad supports multiple
profiling methods and profilers to suit different debugging needs.

This guide covers web-based profiling using ``++profile++`` URL segments and
inline profiling via Python decorators and context managers. Both approaches
support pstats and PyInstrument profilers.

Prerequisites
-------------

Profiling must be enabled through configuration or a feature flag.

**Configuration-based enablement** (default for development):

Profiling is disabled by default in the schema
(``lib/lp/services/config/schema-lazr.conf``):

.. code:: ini

    [profiling]
    profiling_allowed: False
    profile_dir: .

In development, ``configs/development/launchpad-lazr.conf`` overrides
``profiling_allowed`` to ``True``, so profiling is enabled out of the box.
Profile output is written to ``profile_dir``, which defaults to the current
working directory (``.``).

**Feature flag enablement**:

Alternatively, enable profiling using the ``profiling.enabled`` feature flag.

Web-based profiling with ++profile++
-------------------------------------

The easiest way to profile Launchpad is by adding ``++profile++`` to any URL.
This method profiles the entire request, including traversal, rendering, and
database queries.

Get profiling help
~~~~~~~~~~~~~~~~~~

Navigate to any Launchpad page and append ``/++profile++/`` in the URL:

.. code::

    http://launchpad.test/++profile++/


This leads to a help page, that provides further information and examples. 

Profile with pstats
~~~~~~~~~~~~~~~~~~~

To generate a pstats profile (Python's standard library profiler):

.. code::

    http://launchpad.test/++profile++pstats/

This saves a ``.prof`` file to your configured ``profile_dir``. The filename
includes a timestamp, page ID, OOPS ID, and thread name for easy identification.

To view pstats results in your browser:

.. code::

    http://launchpad.test/++profile++pstats&show/

The browser displays profile statistics sorted by time, cumulative time, and
call counts.

To analyze the profile file from the command line:

.. code:: shell

    python -m pstats 2026-06-02_10:15:30-PageName-OOPS-ID-ThreadName.prof

.. note::

    The profiling files are written to ``profile_dir``, which defaults to the
    current working directory (``.``) in the local development environment.

Type ``help`` at the pstats prompt for available commands.

Profile with PyInstrument
~~~~~~~~~~~~~~~~~~~~~~~~~~

PyInstrument is a modern statistical profiler that provides interactive HTML
reports with flame graphs and call trees. It uses sampling rather than tracing,
resulting in lower overhead and more accurate timing:

.. code::

    http://launchpad.test/++profile++pyinstrument/

This saves an HTML file to your ``profile_dir``. Open the file in a web browser
to view the interactive visualization.

To see both the file output and browser results:

.. code::

    http://launchpad.test/++profile++pyinstrument&show/

Profile SQL queries
~~~~~~~~~~~~~~~~~~~

To profile SQL queries with Python stacktraces:

.. code::

    http://launchpad.test/++profile++sqltrace/

This can be slow on large pages. Filter SQL traces to specific statements:

.. code::

    # Get stacktraces for SQL containing "Product.blueprints_usage"
    http://launchpad.test/++profile++sqltrace:includes Product.blueprints_usage/

    # Get stacktraces for SQL starting with "SELECT Distribution"
    http://launchpad.test/++profile++sqltrace:startswith SELECT Distribution/

    # Get stacktraces for SQL ending with specific WHERE clause
    http://launchpad.test/++profile++sqltrace:endswith WHERE Project.id = 5 LIMIT 1/

    # Combine multiple filters with pipe (|)
    http://launchpad.test/++profile++sqltrace:startswith SELECT | includes Product/

To see only SQL queries without stacktraces:

.. code::

    http://launchpad.test/++profile++sql/

Flexible URL placement
~~~~~~~~~~~~~~~~~~~~~~

The ``++profile++`` segment can appear anywhere in the URL:

.. code:: shell

    http://launchpad.test/++profile++show/
    http://launchpad.test/++profile++show/ubuntu
    http://launchpad.test/ubuntu/++profile++show

Some pages may redirect unexpectedly, so experimentation may be necessary.

Inline profiling via code
--------------------------

For profiling specific code sections without requesting a full page profile,
use inline profiling with context managers or decorators.

Context manager profiling
~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert profiling calls directly in your code:

.. code:: python

    from lp.services.profile import profiling

    def my_view_method(self):
        # This code runs normally
        setup_data()
        
        with profiling():
            # Only this section is profiled
            expensive_operation()
            another_expensive_call()
        
        # This code runs normally
        cleanup()

Multiple profiling blocks within a single request are automatically aggregated.

Choose the profiler type
~~~~~~~~~~~~~~~~~~~~~~~~~

By default, inline profiling uses pstats. To use PyInstrument:

.. code:: python

    from lp.services.profile import profiling
    from lp.services.profile.profile import ProfilerType

    with profiling(ProfilerType.PYINSTRUMENT):
        expensive_operation()

View inline profiling results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After making a request with inline profiling code, view the results:

.. code::

    http://launchpad.test/your-page/++profile++show/

The page displays aggregated profiling data with a notice indicating these are
inline profiling results.

.. Note::
    If you use ``++profile++show`` (or ``pstats`` or ``callgrind`` or 
    ``pyinstrument``) in the URL, it takes precedence over inline profiling. 
    The full request will be profiled and inline calls will be ignored with a 
    warning message.

Using the profiled decorator (for test layers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For test layer profiling, use the ``@profiled`` decorator:

.. code:: python

    from lp.services.testing.profiled import profiled

    class MyTestLayer:
        @profiled
        def setUp(cls):
            # This method's execution time is tracked
            expensive_setup()

This is used primarily for profiling the runtime of Launchpad's test layers.
Layer profiling is enabled only when three or more ``-v`` (verbose) flags are
passed to the test runner:

.. code:: shell

    bin/test -vvvct

When enabled, the test runner prints a profiling report at the end of the run,
listing the number of calls and total time spent in each decorated method.
