Error explanations
==================

This page is to aid debugging unhelpful error messages.

``AttributeError: 'NoneType' object has no attribute 'poll'``
-------------------------------------------------------------

.. code:: pytb

   Running canonical.testing.layers.TwistedAppServerLayer tests:
     Set up canonical.testing.layers.ZopelessLayer in 3.350 seconds.
     Set up canonical.testing.layers.DatabaseLayer in 0.457 seconds.
     Set up canonical.testing.layers.LibrarianLayer in 4.786 seconds.
     Set up canonical.testing.layers.LaunchpadLayer in 0.000 seconds.
     Set up canonical.testing.layers.LaunchpadScriptLayer in 0.001 seconds.
     Set up canonical.testing.layers.LaunchpadZopelessLayer in 0.000 seconds.
     Set up canonical.testing.layers.TwistedLaunchpadZopelessLayer in 0.000 seconds.
     Set up canonical.testing.layers.TwistedAppServerLayer in 31.229 seconds.
     Running:
       test_lock_with_magic_id (canonical.codehosting.puller.tests.test_scheduler.TestPullerMasterIntegration)Traceback (most recent call last):
     File "./test.py", line 190, in ?
       result = testrunner.run(defaults)
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 238, in run
       failed = not run_with_options(options)
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 403, in run_with_options
       setup_layers, failures, errors)
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 585, in run_layer
       return run_tests(options, tests, layer_name, failures, errors)
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 513, in run_tests
       test(result)
     File "/home/mwh/canonical/checkouts/trunk/lib/twisted/trial/unittest.py", line 632, in __call__
       return self.run(*args, **kwargs)
     File "/home/mwh/canonical/checkouts/init-stack-pull/lib/canonical/codehosting/puller/tests/test_scheduler.py", line 681, in run
       return TrialTestCase.run(self, result)
     File "/home/mwh/canonical/checkouts/trunk/lib/twisted/trial/unittest.py", line 961, in run
       result.stopTest(self)
     File "/home/mwh/canonical/checkouts/trunk/lib/twisted/trial/unittest.py", line 1158, in stopTest
       self.original.stopTest(method)
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 871, in stopTest
       self.testTearDown()
     File "/home/mwh/canonical/checkouts/trunk/lib/zope/testing/testrunner.py", line 755, in testTearDown
       layer.testTearDown()
     File "/home/mwh/canonical/checkouts/init-stack-pull/lib/canonical/testing/profiled.py", line 28, in profiled_func
       return func(cls, *args, **kw)
     File "/home/mwh/canonical/checkouts/init-stack-pull/lib/canonical/testing/layers.py", line 1535, in testTearDown
       LayerProcessController.postTestInvariants()
     File "/home/mwh/canonical/checkouts/init-stack-pull/lib/canonical/testing/profiled.py", line 28, in profiled_func
       return func(cls, *args, **kw)
     File "/home/mwh/canonical/checkouts/init-stack-pull/lib/canonical/testing/layers.py", line 1389, in postTestInvariants
       if cls.appserver.poll() is not None:
   AttributeError: 'NoneType' object has no attribute 'poll'

Solution
~~~~~~~~

Probably one of "make build", "make schema" or "killing left over librarians".

``AttributeError: 'thread._local' object has no attribute 'interaction'``
-------------------------------------------------------------------------

Example:

.. code:: pytb

    Error in test lp.registry.tests.test_distroseries.TestDistroSeriesGetQueueItems.test_get_queue_items
    Traceback (most recent call last):
      File "/home/cjwatson/src/canonical/launchpad/lp-branches/queue-filter-source-bug-33700/lib/lp/testing/__init__.py", line 322, in run
        testMethod()
      File "/home/cjwatson/src/canonical/launchpad/lp-branches/queue-filter-source-bug-33700/lib/lp/registry/tests/test_distroseries.py", line 261, in test_get_queue_items
        pub_source = self.getPubSource(sourcename='alsa-utils')
      File "/home/cjwatson/src/canonical/launchpad/lp-branches/queue-filter-source-bug-33700/lib/lp/soyuz/tests/test_publishing.py", line 159, in getPubSource
        spn = getUtility(ISourcePackageNameSet).getOrCreateByName(sourcename)
    AttributeError: 'thread._local' object has no attribute 'interaction'


Solution
~~~~~~~~

Call ``login()``. This error often happens when trying to
use core Launchpad objects when not logged in.

Most of the time ``login(ANONYMOUS)`` is good enough. ``login\`` &
``ANONYMOUS`` should be imported from ``lp.testing``.

If you get this error when trying to use the ``LaunchpadObjectFactory``,
you should consider making your test a subclass of
``TestCaseWithFactory``.
