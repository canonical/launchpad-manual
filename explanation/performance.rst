About Launchpad performance
===========================

This document provides an overview of techniques and tools that can help
Launchpad developers run Launchpad more efficiently - faster, and using fewer
system resources.

Measure, don't guess
--------------------
In order to ensure highly performant web services, we need to have a look at
numbers.

We conduct regular performance checks with Google's `PageSpeed Insights`_ for
which we currently score an excellent 98 out of 100 for desktop browsers, with
intentions to close the last bits.

.. _PageSpeed Insights: https://pagespeed.web.dev/

We also have `internal monitoring`_ set up with Grafana, where we measure and
monitor various metrics.

.. _internal monitoring: https://grafana.admin.canonical.com/d/oIhMaXhMk/launchpad-dash?orgId=1&refresh=5m

Timeouts
--------
It is important to have sensible timeouts, as otherwise very slow clients could
block resources for too long, and prevent other clients from connecting.

We use a default of 5 seconds for all page views. This value can be tweaked on
a per page level via `feature rules <https://launchpad.net/+feature-rules>`_.

Writing performant Python code
------------------------------
As a general guideline, writing clean and modern Python code usually produces
reasonably fast code.

As a base, you need to `choose the correct data structure`_, depending on
whether you optimize for lookups, appending elements, or similar.

.. _choose the correct data structure: https://wiki.python.org/moin/TimeComplexity

You also should be aware of the `runtime complexity (Big O)`_ of your code.

.. _runtime complexity (Big O): https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7

Another way to ensure high performance is to use caches. Caches are usually
used to avoid repeated expensive calculations and database lookups.
While Launchpad uses caches on various levels, you should be aware of the
``propertycache`` module, which offers a ``cachedproperty`` decorator.
For more information please refer to its `documentation`_.

.. _documentation: https://git.launchpad.net/launchpad/tree/lib/lp/services/doc/propertycache.rst

It is also recommended to run the latest version of a software, as that one is
usually the fastest one.
This applies both to third party Python libraries, and also to the
`Python interpreter`_ itself.

.. _Python interpreter: https://devblogs.microsoft.com/python/python-311-faster-cpython-team/

Debugging and optimizing database issues
----------------------------------------
Many performance issues are typically caused by inefficient database queries.

In order to prevent issues in the first place you should be aware of how to
`write efficient queries`_.

You should also make use of the already mentioned ``cachedproperty`` decorator
in order to avoid querying the database more often then necessary.

When changing code, it can easily happen to increase the query count. You can
avoid this by using a helper to `preserve query count`_.

When you face performance or even timeout issues, you should learn more about
`timeout analysis`_ (internal video).

PostGreSQL comes with a `builtin tool`_ to analyze SQL queries.

.. _timeout analysis: https://drive.google.com/file/d/1hUivL07Msoyej3wd_T4hMAX61EJzfE38/view?usp=drive_link
.. _builtin tool: https://www.postgresql.org/docs/current/sql-explain.html
.. _write efficient queries: https://dev.launchpad.net/Database/Performance
.. _preserve query count:  https://launchpad.readthedocs.io/en/latest/how-to/preserve-query-count.html

Delivering payload
------------------
We leverage various ways to improve performance on the server side.

Apache is configured to make use of the `gzip` compression.

Also static files, such as CSS and JavaScript, are directly served by
`Apache`_, instead of the application server, which reduces CPU load and
enables more effective caching.

.. _Apache: https://git.launchpad.net/launchpad/tree/charm

We also use various helpers to combine and compress JavaScript and CSS files
before delivery. Launchpad's `Makefile`_ is a good place to start
investigating until there is documentation available.

.. _Makefile: https://git.launchpad.net/launchpad/tree/Makefile
