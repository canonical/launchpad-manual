Developing with YUI.Test
========================

Or putting the fun back into JavaScript

This is a short primer to introduce you to YUI.Test. As you might have
noticed, hacking in JavaScript, né LiveScript, ceased to be fun when
Internet Explore implemented JScript, a freak cross bread of the
JavaScript syntax and VBScript. Other browser makers entered into the
cross-breading competition and I left for a job that let me put all the
logic in the server.

I spent two days creating the milestone_table script that allows users
to create milestones and add them to the table. This involved a
refactoring of the milestoneoverlay script and adding what appeared to
be a few lines to call the existing view that renders a milestone table
row.

Day one was horrible, there was a lot of shouting, words were said that
may have hurt my computer's feelings. There were two problems. The first
was that my extraction of the milestoneoverlay script had failed. This
was not true as I learned. The Windmill test broke weeks before I
started my branch because the page layout changed. The second
problem was the complexity of corner-cases led to unpredictable
behaviours.

Day two was a fun roller coaster ride refactoring my script from first
principles using unit tests. YUI.Test made me write a library, structure
my code to have simple contracts to do simple things, and let me
refactor safely. After a few hours, I was able to bring predictable
behaviour to the script and I believe the code was much easier to read.

You can see the milestone_table script library and its tests at
``lib/lp/registry/javascript``.

What is YUI.Test
----------------

You can read the summary and API of YUI.Test at

-  http://yuilibrary.com/yui/docs/test/
-  http://yuilibrary.com/yui/docs/api/modules/test.html

It is not as solid as other xUnit frameworks.

JavaScript does not support imports which can be used to provide stubs and
mocks. The Y.Mock tools can test params and methods, but not callables; you
will need to monkey patch a callable when you need to verify that your script
passed the expected arguments to a YUI method.

It is automated, but the best way to run tests interactively is in your
browser.

It is better than anything else we have used. It is fast to develop,
easy to maintain, and allows good designs to emerge. Since the test
harness is a page, you can develop a library/widget in many small
branches before you decide it is ready to include in the zpt.

The Harness and Runner
~~~~~~~~~~~~~~~~~~~~~~

JS testing involves two parts. One is an html file that will bootstrap
the environment and load the required code needed to test. There are
sample templates to help bootstrap your tests in the application root.

Copy them from:

- standard_test_template.html
- standard_test_template.js

The first step is to setup the html file. You'll need to adjust the
paths of the various script files included. All code not under direct
test should be pulled from the build/js directory. Replace ${LIBRARY}
with the name of your module you're testing.

For instance if you're working on adding tests to app.widget you'd:

.. code::

    %s/${LIBRARY}/app.widget

The test runner picks up the modules that need to be run based on the ``<li>``
items in ``<ul id="suites">``.

If you did the replace above you'll find that the test module is setup for you.

.. code:: html

    <li>lp.app.widget.test</li>

The second step is to prep the JS file that runs the tests themselves.
The demo files is setup for the same find and replace of ${LIBRARY}. It
will complete the name of the module for you. It's setup to add a .test
to the end of the module you're testing.

The default template has an initial test that will check that it can
load the module you're looking to test. After that find and replace, you
should be able to open the html file and get a single passing test. If
you get any errors, correct them now before moving on to add more tests.
Potential errors include missing dependency modules, typos in the names
of the module, or the paths to the build directory being off.

Running Tests
~~~~~~~~~~~~~

In a browser
^^^^^^^^^^^^

To run the tests interactively simply load the html file into your
browser. A successful run, with ``fetchCSS:true``, looks like:

.. XXX: missing image

Command line
^^^^^^^^^^^^

The YUI unit tests can be run from the command line.

::

   bin/with-xvfb bin/test -x -cvv --layer=YUITestLayer

Or you can run a single test file (you can abbreviate the \`-t\` option
in any of the usual ways, use regular expressions, etc.):

::

   bin/with-xvfb bin/test -cvv -t lib/lp/registry/javascript/tests/test_milestone_table.html

Unfortunately you may not run a single test.

Considerations for Tests
~~~~~~~~~~~~~~~~~~~~~~~~

Use the get/set wrappers to access innerHTML to reset the HTML DOM for a
test. clone was not reliable as I thought it would be.

The Y.Node.create() methods expects a single root node in the raw
markup. I had to strip whitespace to ensure the node was created in my
library, so I tested that in the library tests.

Mocking XHR Calls
~~~~~~~~~~~~~~~~~

Tests will often have a requirement that you want to see that the DOM is
correctly updated as a result of a user initiated action such as a
button click. Sometimes, in production, such a user action may result in
an XHR call where the response data is used to update the DOM. In such
cases, you still want to be able to test the interaction within a YUI
test without having to resort to using an :doc:`integration
test <javascript-integration-testing>`. To make this easy we have the 
:ref:`MockIo class <mockio-library>` in Launchpad.
