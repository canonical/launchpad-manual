.. _page-tests:

Page tests
==========

Using zope.testbrowser to do page testing is easier to write and understand 
than using http() calls because you get easy access to links and form controls 
in the page. For example, you can check whether a link is present, and click on 
that link to go to some other page. zope.testbrowser can be tricky to use 
sometimes though since you can get weird errors.

In the pagetests, there is already a 'browser' object set up ready to use. The 
object is configured using ``browser.handleErrors = False``, to give you a 
traceback instead of a simple 500 error message if something goes wrong. It 
will also give a traceback for 404 pages and pages you don't have permission to 
view.

How to write testbrowser tests
==============================

Read ``lib/zope/testbrowser/README.txt`` or the `online version <https://zopetestbrowser.readthedocs.io/en/latest/>`_, 
to find out everything you can do with the testbrowser.

Read ``lib/canonical/launchpad/testing/pages.py`` to find out how you can use 
page testing helpers.

Read ``lib/canonical/launchpad/pagetests/README.txt`` to find out how to run 
page tests and the available configured users. These are the highlights.

-   Open a page using browser.open():

    .. code::

        browser.open('http://localhost/')
    
    There are a few ways to make sure that after an open, you are on the right 
    page. It is generally better to show a page title than to print the ``browser.url`` 
    because the latter makes it more difficult to rename URLs.

    .. code::

        browser.title
    
    However many of our current page tests, do print the url. You will also 
    definitely want to do this after a redirect to make sure that you end up on
    the expected page.

    .. code::

        browser.url
            'http://localhost/'
    
    If you want to test that a page is protected by a permission, you have to 
    check for an ``Unauthorized`` exception.

    .. code::

        browser.open('http://localhost/calendar')
            Traceback (most recent call last):
            ...
            Unauthorized...
    
To get a better idea of how a pagetest check should look, check out the the 
pagetest helpers in ``lib/canonical/launchpad/testing/pages.py``.

Using multiple browsers
-----------------------

If you test different sessions -- such as logging in as different people -- in 
the same file, you need to use different Browser() objects. There are three 
available automatically:

-   ``admin_browser`` (a Launchpad administrator)
-   ``user_browser`` (someone with no special privileges)
-   ``anon_browser`` (visiting Launchpad while logged out)

To create another one:

    .. code::

        from zope.testbrowser.testing import Browser
        my_browser = Browser()

Or to test as a particular logged-in person:

    .. code::

        my_browser = setupBrowser(auth='Basic test@canonical.com:test')

Testing the contents of the page
--------------------------------

-   To check the contents of the page, print ``browser.contents``. 
    Unfortunately the expected output can't begin with '...', so we need to 
    include the start of the page.

    .. code::

        print browser.contents
            <!DOCTYPE...
            ...No events in the next two weeks...
    
-   Often we want to make sure something isn't in a page. For this we can use 
    ``foo`` not in ``browser.contents``, but if we want to ensure that a link 
    or form control isn't visible, there's a better way; using ``getLink()``. 
    For example:

    .. code::

        browser.getLink('Remove Event')
            Traceback (most recent call last): 
            ...
            LinkNotFoundError

        add_event = browser.getLink('Add Event')
        add_event is not None
            True

    In some cases it is more appropriate to get the link by its URL, using the 
    ``url=`` parameter. For example:

    .. code::

        add_event = browser.getLink(url='http://launchpad.dev/foo/bar/+addevent')
        add_event is not None
            True

    Now that we have a link we can click on it to go to the linked page.

    .. code::

        add_event.click()
        browser.url
            'http://localhost/calendar/+add'

-   When a page contains a form, we can check what values the form controls contain, and we can also fill them in.
    ``browser.getControl('Name').value``

    .. code::

            ''
        browser.getControl('Name').value = 'New event'
        browser.getControl('Description').value = 'Event description.'
        browser.getControl('Starting date and time').value = '2006-10-10 08:00'
        browser.getControl('Duration').value = '2'
        browser.getControl(name='field.duration.unit').value
            ['h']
        browser.getControl(name='field.duration.unit').displayValue
            ['hours']

Now that we filled all the required fields in we can submit it.

    .. code::

        browser.getControl('Add').click()
        browser.url
            'http://localhost/calendar/2006-W41'

Viewing a page as seen by the testbrowser
-----------------------------------------

When writing or debugging a page test, you may wonder, "What does the page 
really look like in a browser at this point?" You could walk through the entire 
test manually, but there is an easier way.

First, edit your ``config/default/launchpad.conf`` file and change the ``dbname`` 
in your <canonical default> section to be ``launchpad_ftest``.

Next, add a pdb break point at the place in your page test that you want to 
examine:

.. code::

     >>> import pdb; pdb.set_trace() 

Now run the page test as you normally would using bin/test. When you hit the 
break point, go to a different shell and do ``make run``. Because of your ``dbname`` 
change, this will run the site against the testing database, so all the state 
your page test has built up will be available to you. Now poke around in your 
browser all you want.

Once your page test ends (maybe because you've killed it), your browser session 
will be unhappy because the launchpad_ftest database is torn down when bin/test 
exits. Make sure you revert your launchpad.conf changes before you commit. 
(`Barry Warsaw <https://blog.launchpad.net/meet-the-devs/meet-barry-warsaw>`_ 
plans on making this easier when lazr config lands.)

Dealing with old-style page tests
---------------------------------

There's no reason to rewrite existing page tests, but if some test starts to 
fail, it's often easier to rewrite it using zope.testbrowser than to fix the 
existing one. For example, if you have a page test that submits a form, and the 
test is to change a single field in the form, the test might start failing if 
some required field (with a default value) gets added to the form. The 
traditional pagetest would fail since the required field is missing. Rewriting 
it using zope.testbrowser would look something like this:

.. code::

    browser.open(...)
    browser.getControl('Some Field').value = 'foo'
    browser.getControl('Save').click()

That is, it doesn't have to care about the other field values, they will have 
the default values.

Organizing tests into stories
-----------------------------

Prefer standalone tests and short stories rather than long stories.

Unresolved issues
-----------------

There's currently no equivalence to ``makepagetest.py`` in RF for creating 
``zope.testbrowser`` tests, but there is another package, ``zope.testrecorder``, 
which we could pull in.