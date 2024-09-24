=================
Tests style guide
=================

This page documents conventions for our Launchpad tests.  Reviewers make
sure that code merged is documented and covered by tests.  Following the
principles outlined in this document will minimize comments related to test
style from reviewers.

Reviewers will block merge of code that is under-documented or under-tested.
We have two primary means of documentation:

#. System documentation in ``doc`` directories such as ``lib/lp/<app>/doc``.
#. Page tests in ``lib/lp/<app>/stories``.
#. View tests in ``lib/lp/<app>/browser/tests``.

While these two types of documentation use the doctest format, which means
that they contain testable examples, they are documentation first.  So they
are not the best place to test many corner cases or various similar
possibilities.  This is best done in other unit tests or functional tests,
which have ensuring complete test coverage as their main objective.

Testable Documentation
======================

Testable documentation includes system documentation doctests and page
tests.

What do we mean by "testable documentation"?  One rule of thumb is the
narrative should be similar to what you'd see in an API reference manual.
Another trick to ensure the narrative is appropriately detailed is to
mentally remove all of the code snippets and see if the narrative stands by
itself.

System Documentation
--------------------

These are doctests located under ``lib/lp/<app>/doc``.  They are used to
document the APIs and other internal objects.  The documentation should
explain to a developer how to use these objects and what purpose they serve.

Each modification to ``lp.<app>.interfaces`` should be documented in one of
these files.

(Each file in that directory is automatically added to the test suite.  If
you need to configure the test layer in which the test will be run or need
to customize the test fixture, you can add special instructions for the file
in the system documentation harness in ``lib/lp/<app>/tests/test_doc.py``.)

Use Cases Documentation: Page Tests
-----------------------------------

We use page tests to document all the use cases that Launchpad satisfies.
The narrative in these files should document the use case.  That is, they
should explain what the user's objective is and how he accomplishes it.

The examples in these files uses ``zope.testbrowser`` to show how the user
would navigate the workflow relevant to the use case.

So each addition to the UI should be covered by an appropriate section in a
page test.

The page tests do not need to document and demonstrate each and every
possible way to navigate the workflow.  This can usually be done in a more
direct manner by testing the view object directly. 

Browser View Tests
------------------

View objects are usually documented that way along other system objects in
files named ``*-pages.rst`` or in
``lib/lp/<app>/browser/tests/*-views.rst``.

The browser tests directory contains both doctest files for documenting the
use of browser view classes and unit tests (e.g. ``test_*.py``) for
performing unit tests, including covering corner cases.  Currently some
apps, registry for example, have a large number of doctests in this location
that are not strictly testable documentation.  Over time these
non-documentation doctest files should be converted to unit tests. 

**All new browser tests that are not testable documentation should be
written as unit tests.**

Common Conventions
------------------

The basic conventions for testable documentation are:

* Example code is wrapped at 78 columns, follows the regular :doc:`Python
  style guide <python>`, and is indented 4 spaces.
* Narrative text may be wrapped at either 72 or 78 columns.
* You can use regular Python comments for explanations related to the code
  and not to the documentation.
* Doctests use Restructured Text (or "ReST", see
  https://docutils.sourceforge.net/docs/user/rst/quickref.html).

  * We use ReST because it's what the Python community have standardized on
    and because it makes setting up Sphinx to browse all the doctests
    simpler.

* The file should have a first-level title element.  An expansion of the
  filename is usually a good start.  For example, the file
  ``bugcomment.rst`` could have this title:

.. code-block:: rst

    Bug Comments
    ============

* Two blank lines are used to separate the start of a new section (a header).

.. code-block:: rst

    An Example
    ----------

    Launchpad tracks foo and bar elements using the IFooBarSet utility.

        >>> from lp.foo.interfaces.bar import IBar, IFoo, IFooBarSet
        >>> from lp.testing import verifyObject
        >>> foobarset = getUtility(IFooBarSet)

        >>> verifyObject(IFooBarSet, foobarset)
        True

    You use the getFoo() method to obtain an IFoo instance by id:

        >>> foo = foobarset.getFoo("aFoo")
        >>> verifyObject(IFoo, foo)
        True

    Similarly, you use the getBar() method to retrieve an IBar instance by
    id:

        >>> bar = foobarset.getBar("aBar")
        >>> verifyObject(IBar, bar)
        True

Each individual test should be of the form:

.. code-block:: pycon

     >>> do_something()
     expected output

This means that something like this isn't considered a test, but test setup
(since it doesn't produce any output):

.. code-block:: pycon

    >>> do_something()

For the reason above, the assert statement shouldn't be used in doctests.

Comparing Results
-----------------

When writing doctests, make sure that if the test fails, the failure message
will be helpful to debug the problem.  Avoid constructs like:

.. code-block:: pycon

    >>> "Test" in foo.getText()
    True

The failure message for this test will be:

.. code-block:: pycon

    - True
    + False

which isn't helpful at all in understanding what went wrong. This
example is a lot more helpful when it fails:

.. code-block:: pycon

    >>> foo.getText()
    '...Test...'

For page tests where the page contains a lot of elements, you should zoom in
to the relevant part.  You can use the ``find_main_content()``,
``find_tags_by_class()``, ``find_tag_by_id()``, and ``find_portlet()``
helper methods.  They return ``BeautifulSoup`` instances, which makes it
easy to access specific elements in the tree.

.. code-block:: rst

    The new status is displayed in the portlet.

        >>> details_portlet = find_portlet(browser.contents, "Question details")
        >>> print(details_portlet.find("b", text="Status:").next.strip())
        Needs information

There is also an ``extract_text()`` helper that only renders the HTML text:

.. code-block:: pycon

    >>> print(
    ...     extract_text(find_tag_by_id(browser.contents, "branchtable"))
    ... )
    main         60 New           firefox
    klingon      30 Experimental  gnome-terminal
    junk.contrib 60 New 2005-10-31 12:03:57 ... weeks ago

Read `Page tests <https://dev.launchpad.net/PageTests>`_ for other tips on
writing page tests.

When to print and when to return values
---------------------------------------

Doctests mimic the Python interactive interpreter, so generally it's
preferred to simply return values and expect to see their string
representation.  In a few cases though, it's better to ``print`` the results
instead of just returning them.

The two most common cases of this are ``None`` and strings.  The interactive
interpreter suppresses ``None`` return values, so relying on these means the
doctest makes less sense.  You could compare against ``None``, but the
``True`` or ``False`` output isn't explicit, so it's almost always better to
print values you expect to be ``None``.

Instead of:

.. code-block:: pycon

    >>> should_be_none()
    >>> do_something_else()

Use:

.. code-block:: pycon

    >>> print(should_be_none())
    None
    >>> do_something_else()

For a different reason, it's also usually better to print string results
rather than just returning them.  Returning the string causes the quotes to
be included in the output, while printing the string does not.  Those extra
quotes are usually noise.

Instead of:

.. code-block:: pycon

    >>> get_some_text()
    'foo'
    >>> get_some_string()
    "Don't care"

Use:

.. code-block:: pycon

    >>> print(get_some_text())
    foo
    >>> print(get_some_string())
    Don't care

Dictionaries and sets
---------------------

You can't just print the value of a dictionary or a set when that collection
has more than one element in it, e.g.

.. code-block:: pycon

    >>> print(my_dict)
    {'a': 1, 'b': 2}

The reason is that Python does not guarantee the order of its elements in a
dictionary or set, so the printed representation of a dictionary is
indeterminate.  In page tests, there's a ``pretty()`` global which is
basically exposing Python's pretty printer, and you can use it safely:

.. code-block:: pycon

    >>> pretty(my_dict)
    {'a': 1, 'b': 2}

Though it's a bit uglier, you can also print the sorted items of a
dictionary:

.. code-block:: pycon

    >>> sorted(my_dict.items())
    [('a', 1), ('b', 2)]

Global State
------------

Be especially careful of test code that changes global state.  For example,
we were recently bitten by code in a test that did this:

.. code-block:: python

    socket.setdefaulttimeout(1)

While that may be necessary for the specific test, it's important to
understand that this code changes global state and thus can adversely affect
all of our other tests.  In fact, this code caused intermittent and very
difficult-to-debug failures that mucked up buildbot for many unrelated
branches.

The guideline then is this: if code changes global state (for example, by
monkey-patching a module's globals) then the test **must** be sure to
restore the previous state, either in a ``try``-``finally`` clause, or at
the end of the doctest, or in the test's ``tearDown`` hook.

Style to Avoid
--------------

A very important consideration is that documentation tests are really
**documentation** that happens to be testable.  So, the writing style should
be appropriate for documentation.  It should be affirmative and descriptive.
There shouldn't be any phrases like: 

* Test that...
* Check that...
* Verify that...
* This test...

While these constructs may help the reader understand what is happening,
they only have indirect value as documentation.  They can usually be
replaced by simply stating what the result is.

For example:

.. code-block:: rst

    Test that the bar was added to the foo's related_bars:

        >>> bar in foo.related_bars
        True

Can be replaced by:

.. code-block:: rst

    After being linked, the bar is available in the foo's
    related_bars attribute:

        >>> bar in foo.related_bars
        True

Also, use of "should" or "will" can usually be replaced by the present tense
to make the style affirmative.

For example:

.. code-block:: rst

    The bar not_a_foo attribute should now be set:

        >>> bar.not_a_foo
        True

Can be replaced by:

.. code-block:: rst

    The bar not_a_foo attribute is set after this operation:

        >>> bar.not_a_foo
        True

A good rule of thumb to know whether the narrative style works as
documentation is to read the narrative as if the code examples were not
there.  If the text style makes sense, the style is probably good.

Using Sample Data
-----------------

If possible, avoid using the existing sample data in tests, apart from some
basic objects, like users.  Sample data is good for demonstrating the UI,
but it can make tests harder to understand, since it requires knowledge of
the properties of the used sample data.  Using sample data in tests also
makes it harder to modify the data.

If you do use sample data in the test, assert your expectations to avoid
subtle errors if someone modifies it.  For example:

.. code-block:: rst

    Anonymous users can't see a private bug's description.

        >>> private_bug = getUtility(IBugSet).get(5)
        >>> private_bug.private
        True

        >>> login(ANONYMOUS)
        >>> private_bug.description
        Traceback (most recent call last):
        ...
        Unauthorized:...

When using fake domains and **especially** fake email addresses, wherever
possible use the ``example.{com,org,net}`` domains, e.g.
``aperson@example.com``.  These are guaranteed by Internet standard never to
exist, so it can't be possible to accidentally spam them if something goes
wrong on our end.

Fixtures and Helpers
--------------------

Sometimes a lot of code is needed to set up a test, or to extract the
relevant information in the examples.  It is usually a good idea to factor
this code into functions that can be documented in the file itself (when the
function will only be used in that file), or even better, moved into a test
helper module from which you can import.

These helpers currently live in ``lib/lp/testing``.  New helpers should go
there, unless they're very specific to a particular corner of the
application; in such cases you can use something like ``lp.foo.testing``.

Functional and Unit Tests
=========================

Complete test coverage without impairing documentation often requires
dedicated functional or unit tests.  In Launchpad, Python test cases are
used for these types of tests.  You may encounter legacy code that uses
doctests for functional testing.  If you do, please consider converting it
to a Python test case.

Functional tests are found in the ``tests`` subdirectory of each directory
containing code under test.

Python Test Cases
-----------------

Although Python test cases are not documentation they must still be
human-readable.  So:

* Keep the test short and concise.
* Stick to the "setup, exercise, assert" pattern, especially avoid
  "exercise, assert, exercise some more, assert".
* Put into the docstring of each test case what is being tested.  As a
  special case for test methods, a comment block at the beginning of the
  method is considered an acceptable substitute to a docstring.  Please
  observe "Style to avoid", as explained above.
* Organize related test cases in the same class.  Explain test objectives in
  the class docstring.
* When asserting for equality use the form ``assertEqual(expected_results,
  actual_results, "...")`` (the third argument is optional, for use if
  failure messages would otherwise be particularly unclear).
* Make sure that each assert fails with an appropriate error message
  explaining what is expected.  ``lp.testing.TestCase`` and
  ``TestCaseWithFactory`` are derived from ``testtools.TestCase`` and
  therefore produce good error messages.  Only some cases may warrant an
  explicit error message.  For example, this:

.. code-block:: python

    self.assertTrue("aString" in result)

could be replaced by:

.. code-block:: python

    self.assertIn("aString", result)

* Consider using testtools matchers where reasonable.  These can often
  improve failure messages so that they show more information in one go,
  which can be useful when debugging mysterious failures.  For example,
  instead of this:

.. code-block:: python

    self.assertEqual("expected", obj.foo)
    self.assertEqual("more expected", obj.bar)

prefer this:

.. code-block:: python

    self.assertThat(obj, MatchesStructure.byEquality(
        foo="expected",
        bar="more expected"))

In general, you should follow Launchpad coding conventions (see :doc:`Python
style guide <python>`), however when naming test methods:

* Use PEP 8 names, e.g. ``test_for_my_feature()``
* When testing a specific Launchpad method, a mix of PEP 8 and camel case is
  used, e.g. ``test_fooBarBaz()``
* When testing alternatives for a LP method, use this style:
  ``test_fooBarBaz_with_first_alternative()``,
  ``test_fooBarBaz_with_second_alternative()``, etc.

How To Use the Correct Test URL
===============================

When tests run, and need to connect to the application server instance under
test, you need to ensure that a URL with the correct port for that test
instance is used.  Here's how to do that.

The config instance has an API which allows the correct URL to be
determined.  The API is defined in ``LaunchpadConfig`` and as a convenience
is available as a class method on ``BaseLayer``.

.. code-block:: python

    def appserver_root_url(self, facet="mainsite", ensureSlash=False):
        """Return the correct app server root url for the given facet."""

Code snippets for a number of scenarios are as follows.

**Doc Tests**

.. code-block:: pycon

    >>> from lp.testing.layers import BaseLayer
    >>> root_url = BaseLayer.appserver_root_url()
    >>> browser.open(root_url)

**Unit Tests**

.. code-block:: python

    class TestOpenIDReplayAttack(TestCaseWithFactory):
        layer = AppServerLayer

        def test_replay_attacks_do_not_succeed(self):
            browser = Browser(mech_browser=MyMechanizeBrowser())
            browser.open("%s/+login" % self.layer.appserver_root_url())
