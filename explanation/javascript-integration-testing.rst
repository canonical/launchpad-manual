Integration Testing in JavaScript
=================================

Launchpad's JavaScript testing is built around YUI 3's ``yuitest`` library.
We use the Graded Browser Support chart to determine which browser's code should
be regularly tested in.

Every JavaScript component should be tested first and foremost using
:doc:`unit testing <javascript-unittesting>`.

We have infrastructure to write tests centred on the integration
between the JavaScript component and the app server (regular API or
view/++model++ page api.)

These are still written using the ``yuitest`` library, but they are
loaded and can access a "real" appserver (the one started by the
AppServerLayer).

The testing framework also allows testing integration of the component on
the page itself (answering the question: Is it hooked up properly?)
through loading a page through an iframe for inspection. XXX: Give more
information on how to do this.

Creating the tests
------------------

- Use ``standard_yuixhr_test_template.js`` and
  ``standard_yuixhr_test_template.py`` in the root of the Launchpad tree as
  templates. Copy and rename both files to the same directory.
  You can put them in the usual ``javascript/tests`` subdirectory.

-  The ``.js`` file contains the tests using the standard ``yuitest`` library.
-  The ``.py`` file contains fixtures that will operate within the app server.
   They should create content through the standard LaunchpadObjectFactory that
   will be accessed by the test. The database is automatically reset
   after every test.

Running the tests
-----------------

-  We have tests discoverer that will make these tests run
   automatically as part of the test suite.
-  To run manually, start the test-appserver using ``make run-testapp``.
-  Visit in your browser
   ``https://launchpad.dev:8085/+yuitest/path-to-test-basename-from-root``
   So for example, if you copied the templates to 
   ``lib/lp/bugs/javascript/tests/test_some_xhr.js``, you can run the tests by
   accessing ``https://launchapd.dev:8085/+yuitest/lib/lp/bugs/javascript/tests/test_some_xhr``.


Gotchas
-------

-  When loading ``https://launchpad.dev:8085/+yuitest`` if you see
   "cannot import Python fixture file" it may be due to not having
   ``__init__.py`` files in the directory and parent directories where
   you've put your new ``.py`` test fixture.
