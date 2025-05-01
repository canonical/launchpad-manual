=================
Using breakpoints
=================

When you set a breakpoint, e.g. via ``import pdb;pdb.set_trace()``
and run a collection of tests,
you may receive the following message:

.. code-block:: shell-session

    Can't use pdb.set_trace when running a layer as a subprocess!

This happens when you are running a collection of tests which span multiple layers,
and a previous layer could not be safely torn down in-process,
so the testrunner had to spawn a subprocess instead.

The workaround is to run just the one test you are trying to debug.

You can read more about this issue in `zope.testrunner's documentation
<https://zopetestrunner.readthedocs.io/en/latest/testrunner-layers-ntd.html>`_.
