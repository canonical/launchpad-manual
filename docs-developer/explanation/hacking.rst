Hacking
=======

.. include:: ../includes/important_not_revised.rst

.. note::

    Want to navigate the source tree? Look at :doc:`Navigating <navigating>`.

Python programming
------------------

Which version of Python should I target?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, Launchpad requires Python 3.5.

How should I format my docstrings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, thank you for writing docstrings. They make the code much easier
to follow for the people that didn't originally write it.
To answer the question, you have the following options.

- A single short sentence.
- A single short sentence, blank line, further explanation.
- A single short sentence, blank line, rst-style explanation of arguments and
  return value.
- A single short sentence, blank line, further explanation with rst-style
  explanation of arguments and return value.

You may include a short doctest in the further explanation.
See the examples in the `Epydoc documentation`_.
We're using the **rst** or **ReStructuredText** format, and not using the
**Javadoc** or **Epytext** formats.

.. _Epydoc documentation: http://epydoc.sourceforge.net/fields.html

See also: `PEP-8, Style Guide for Python Code`_ and `Docstring Conventions`_.

Note that we're not using the full expressiveness of `ReStructuredText`, so [[http://python.org/peps/pep-0287.html|PEP-287]] doesn't apply.

.. _PEP-8, Style Guide for Python Code: http://python.org/peps/pep-0008.html
.. _Docstring Conventions: http://python.org/peps/pep-0257.html

How should I use assertions in Launchpad code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  See XXX AssertionsInLaunchpad.

What exceptions am I allowed to catch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See XXX ExceptionGuidelines.

What exception should I raise when something passed into an API isn't quite right?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In short, never raise ``ValueError``, ``NameError`` or ``TypeError``, and avoid
subclassing these exceptions as well. The full instructions are at
XXX ExceptionGuidelines.

In the case of ``NotFoundError``, if you are going to catch this specific error
in some other code, and then take some corrective action or some logging
action, then seriously consider creating your own subclass.
This allows your code to handle exactly the situation that you expect, and not
be tricked into handling ``NotFoundErrors`` raised by code several levels in.

When writing docstrings, always think whether it makes things clearer to say
which exceptions will be raised due to inappropriate values being passed in.

I have a self-posting form which doesn't display the updated values after it's submitted. What's wrong?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For now, all self-posting forms have to call
``lp.services.database.sqlbase.flush_database_updates()`` after processing the
form.

.. "Is that still relevant today? In particular, is that still relevant with
   LaunchpadFormView?" -- DavidAllouche <<DateTime(2007-11-14T16:27:42Z)>>

I need to define a database class that includes a column of dbschema values. How do I do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use an XXX EnumCol.

I have received a security proxied list from some API. I need to sort it, but the ``sort()`` method is forbidden. What do I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you get a list from a security proxied object, that list is protected
against being altered. This is important, because you don't know who else might
have a reference to that list.

When programming in Python generally, it is a good idea to make a copy of a
list you get from somewhere before altering it.
The security proxies just enforce this good practice.

You can make a copy of the list by using the ``list`` constructor.
Here is an example, using the launchpad API.

.. code-block:: python

    members = getUtility(ITeamParticipationSet).getAllMembers()
    members = list(members)  # Get a mutable list.
    members.sort()


You can also use the ``sorted`` builtin to do this.

.. code-block:: python

    members = sorted(getUtility(ITeamParticipationSet).getAllMembers())

SQL Result Set Ordering
~~~~~~~~~~~~~~~~~~~~~~~

If the ordering of an SQL result set is not fully constrained, then your tests
should not be dependent on the natural ordering of results in the sample data.

If Launchpad does not depend on the ordering of a particular result set, then
that result set should be sorted within the test so that it will pass for any
ordering.

As a general rule, the result sets whose order we want to test are the ones
that are displayed to the user.  These should use an ordering that makes sense
to the user, and the tests should ensure that happens.

How do I use a PostgreSQL stored procedure/expression as the order_by in Storm?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have to wrap it in ``SQL()``:

.. code-block:: python

    from storm.expr import Desc, SQL

    store.find(Person).order_by(SQL("person_sort_key(displayname, name)"))

    store.find(Question, SQL("fti @@ ftq('firefox')")).order_by(
        Desc(SQL("rank(fti, ftq('firefox'))"))

How do I generate SQL commands safely?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The safest way is to let Storm's query compiler do it:

.. code-block:: python

    results = list(
        store.find((Person.id, Person.name), Person.display_name == 'Stuart Bishop'))

If you can't do that, perhaps because you're doing something too complicated
for the query compiler to manage, then the next safest way is to ensure that
all data is passed in as parameters, the way the DB-API intended it:

.. code-block:: python

    results = list(store.execute(
        "SELECT id, name FROM Person WHERE displayname = %s",
        params=('Stuart Bishop',)))

If you need to embed your data in the SQL query itself, there is only one rule
you need to remember - quote your data. Failing to do this opens up the system
to an SQL injection attack, one of the more common and widely known security
holes and also one of the more destructive. Don't attempt to write your own
quote method - you will probably get it wrong. The only two formats you can use
are %d and %s, and %s should always be escaped, *no exceptions!*

.. code-block:: python

    from lp.services.database.sqlbase import quote
    results = list(store.execute(
        "SELECT id, name FROM Person WHERE displayname = %s" % quote("Stuart Bishop")))

    store.execute("SELECT * FROM Person WHERE name = %s" % quote(
        "'; drop table person cascade; insert into person(name) values ('hahaloser')"))


The second command in the previous example demonstrates a simple argument that
might be passed in by an attacker.

What date and time related types should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See XXX DatetimeUsageGuide for information on what types to use, and how the
Python ``datetime`` types relate to database types through Storm.

Python segfaulted. What should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python programs should never segfault, but it can happen if you trigger a bug
in an extension module or the Python core itself.
Since a segfault won't give you a Python traceback, it can be a bit daunting
trying to debug these sort of problems.
If you run into this sort of problem, tell the list.

See XXX DebuggingWithGdb for some tips on how to narrow down where a segfault
bug like this is occurring. In some cases you can even get a Python stack
trace for this sort of problem.

I want an object to support ``__getitem__``, what's the best style?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many Launchpad objects support ``__getitem__``. For example, if you have a
``Foo``, and want to support ``Foo()['bar']``, you will implement
``__getitem__`` for class ``Foo``.
Often, this is used along with ``GetitemNavigation`` in your browser code to
ensure smooth traversal.

The ``__getitem__`` code itself should not, however, contain the magic that
fetches whatever needs to be fetched.
It should instead call another method that does so, explicitly saying what it
is getting. So for example:

.. code-block:: python

    @implementer(IFoo)
    class FooContentClass:

        def __getitem__(self, name):
            """See IFoo."""
            return self.getVersion(name)

        def getVersion(self, name):
            """See IFoo."""
            # blah blah blah
            return version

Note that generally, a ``__getitem__`` method should give access to just one
kind of thing. In the example above, it gives you access to versions with the
given name. If your traversal needs to get two kinds of things, for example
versions or changesets, then this is better put in the traversal code in the
``FooNavigation`` class than in the ``__getitem__`` code of the database class.

Properties
~~~~~~~~~~

Properties should be cheap. Using a property can make accessing fields or
calculated results easier, but programmers expect properties to be usable
without consideration of the internal code in the property. As such, a property
that calls expensive routines such as disk resources, examining database joins
or the like will violate this expectation. This can lead to hard to analyze
performance problems because its not clear what is going on unless you are very
familiar with the code.

  Our code routinely contradicts this guideline. I remember I had issues in the
  past with TALES traversal when trying to use methods, and had to use
  properties instead. We have decorators such as ``@cachedproperty`` to help
  with   the performance issues. Someone who knows what he talks about should
  update this FAQ to match reality. -- DavidAllouche 
  <<DateTime(2007-11-14T16:50:06Z)>>

Properties should always be used instead of ``__call__()`` semantics in TALES
expressions. The rule is that in view classes, we don't do this:

.. code-block:: python

    def foo(self):
        ...

We always do this:

.. code-block:: python

    @property
    def foo(self):
        ...

Storm
-----

Questions about Storm usage.

XXX StormMigrationGuide document is highly recommended.

How to retrieve a store?
~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways of retrieving a storm 'store', before issuing a query
using native syntax.

The first format retrieves the Store being used by another object. Use this
method when you don't need to make changes, but want your objects to interact
nicely with objects from an unknown Store (such as a methods parameters):

.. code-block:: python

    from storm.store import Store

    store = Store.of(object)
    result = store.find(Person, Person.name == 'zeca')

You can also explicitly specify what Store you want to use. You get to choose
the realm (Launchpad main, auth database) and the flavor (master or slave).
If you are retrieving objects that will need to be updated, you need to use
the master. If you are doing a search and we don't mind querying data a few
seconds out of date, you should use the slave.

.. code-block:: python

    from lp.services.webapp.interfaces import (
        IStoreSelector, MAIN_STORE, AUTH_STORE,
        MASTER_FLAVOR, SLAVE_FLAVOR)

    master_store = getUtility(IStoreSelector).get(MAIN_STORE, MASTER_FLAVOR)
    master_obj = store.find(Person, Person.name == 'zeca')
    slave_store = getUtility(IStoreSelector).get(MAIN_STORE, SLAVE_FLAVOR)
    slave_obj = store.find(Person, Person.name == 'zeca')


If you don't need to update, but require up-to-date data, you should use
the default flavor. (e.g. most views - the object you are viewing might just
have been created). This will retrieve the master unless the load balancer
is sure all changes made by the current client have propagated to the
replica databases.

.. code-block:: python

    from lp.services.webapp.interfaces import (
        IStoreSelector, MAIN_STORE, AUTH_STORE, DEFAULT_FLAVOR)

    store = getUtility(IStoreSelector).get(MAIN_STORE, DEFAULT_FLAVOR)
    result = store.find(Person, Person.name == 'zeca')

Security, authentication
------------------------

See XXX LaunchpadAuthentication

How can I do get the current user in a database class?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to pass it in one of the parameter's method.
You **shouldn't** use the ``ILaunchBag`` for this. In fact, you shouldn't use
the ``ILaunchBag`` in any database class.

The principle is that the database code must not rely on implicit state,
and by that is meant state not present in the database object's data nor
in the arguments passed to the method call.
Using ``ILaunchBag`` or ``check_permission`` would use this kind of implicit
state.

How can I protect a method based on one of its parameter?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can't! Only attribute access can be protected and only the attribute name
and the current user is available when that check is made.

But there is a common pattern you can use: call in that method another method
on the object passed as parameter.
That method can be appropriately protected using the current security
infrastructure.
Since this auxiliary method is part of an object-collaboration scenario, it's
usually a good idea to start these methods with the **notify** verb.
The method is notifying the other object that a collaboration is taking place.

This will often happen with methods that needs to operate on bugs - since you
usually don't want the operation to be allowed if it's a private bug that the
user doesn't have access to.

Example:

.. code-block:: python

    def linkBug(self, bug):
    # If this is a private bug that the user doesn't have access, it
    # will raise an Unauthorized error.
    bug.notifyLinkBug(self)

Email Notifications
-------------------

When I need to send a notification for a person/team, how do I know what email address(es) I have to send the notification to?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As you know, persons and teams are meant to be interchangeable in Launchpad,
but when it comes to mail notification the rules differ a bit, see XXX
TeamEmail for more information. In order to mask these rules, there's a helper
function called ``get_contact_email_addresses()`` in
``lib/lp/services/mail/helpers.py`` that you should always use to get the
contact address of a given person/team.
Please note that this function will always return a set of email addresses,
which is perfectly suitable to be passed in to ``simple_sendmail()``.

Web UI
------

How do I perform an action after an autogenerated edit form has been successfully submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to write a view's class for this form, if you don't have one already.
In your view's class, add a method ``changed()``.

.. code-block:: python

    def changed(self):
        # This method is called after changes have been made.

You can use this hook to add a redirect, or to execute some logging, for
example.

How do I perform an action after an autogenerated add form has been successfully submitted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to write a view's class for this form, if you don't  have one already.
In your view's class, add a method ``createAndAdd()``.

.. code-block:: python

    def createAndAdd(self, data):
        # This method is called with the data from the form.


You can use this hook to create new objects based on the input from the user.

How can I redirect a user to a new object just created from an autogenerated add form?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to write a view's class for this form, if you don't  have one already.
In your view's class, add a method ``nextURL()``.

.. code-block:: python

    def nextURL(self):
        # This method returns the URL where the user should be redirected.


How do I format dates and times in page templates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's use some object's ``datecreated`` attribute as an example.

To format a date, use ``tal:content="context/datecreated/fmt:date``.

To format a time, use ``tal:content="context/datecreated/fmt:time``.

To format a date and time, use ``tal:content="context/datecreated/fmt:datetime``.


How should I generate notices like "Added Bug #1234" to the top of the page?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    response.addInfoNotification('Added <b>Bug #%(bug_id)d</d>', bug_id=bug.id)

There are other notification levels (Debug, Info, Notice, Warning, Error), as
per XXX BrowserNotificationMessages.

Launchpad API
-------------

How do I add a new celebrity?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See XXX AddingLaunchpadCelebrity.

Global Configuration
--------------------

How do I add items to launchpad-lazr.conf?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is done by changing the file ``lib/lp/services/config/schema-lazr.conf``.

- Items should be created with the following syntax:

  .. code-block::

    # Comment describing the item.
    key_name: default_value


  ``key_name`` must be a valid Python identifier.

- Subsections should be created with the following syntax:

  .. code-block::
  
    [section_name]
    key_name: ...
    
  ``section_name`` must be a valid Python identifier.

How are these default values changed for specific environments?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default configuration values are overridden in
``/configs/<environment>/launchpad-lazr.conf``.
Notable environments include:
- ``production`` — the production environment; launchpad.net.
- ``staging`` — the staging environment; staging.launchpad.net.
- ``development`` — local development environment, used with ``make run`` and ``make run_all``; launchpad.test.
- ``testrunner`` — the environment used when running tests.

The syntax for overriding configuration values is the same as the syntax for
defining them.

How do I use the items listed in launchpad-lazr.conf?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once your items are added to the ``launchpad-lazr.conf`` file, you may use them
as follows:

.. code-block:: python

    >>> from lp.services.config import config
    >>> # We grab dbname from the default section
    >>> dbname = config.dbname
    >>> # We grab the dbuser from the gina subsection
    >>> dbuser = config.gina.dbuser


How can I temporarily override configuration variables in tests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``lp.testing.TestCase.pushConfig``.

Testing
-------

What kind of tests should we use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the XXX TestsStyleGuide for the complete answer.

Short answer is that we favour the use of doctest in ``lib/lp/*/doc`` for API
documentation and XXX PageTests for use-cases documentation. We use doctests and regular python unittest to complete the coverage.

How do I run just one doctest file, e.g. ``lib/lp/*/doc/mytest.txt``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``--test`` argument to name it:

.. code-block::

    bin/test --test=mytest.txt

What about running just one pagetest story, e.g. ``lib/lp/*/stories/initial-bug-contacts``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    bin/test --test=stories/initial-bug-contacts

What about running a standalone pagetest, e.g. ``xx-bug-index.txt``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Like this:

.. code-block::

    bin/test --test=xx-bug-index

And if I want to execute all tests except one?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    bin/test '!test_to_ignore'

How can I examine my test output with PDB?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``bin/test``'s ``-D`` argument is **everyone's** friend.

If your test raises any exceptions or failures, then the following will open a
pdb shell right where the failure occurred:

.. code-block::

    bin/test -D -vvt my.test.name

Where can I get help on running tests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try this:

.. code-block::

    bin/test --help

How can I check test coverage?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The bin/test script has a ``--coverage option`` that will report on code
coverage.

How can I run only the tests for the page test layer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    bin/test --layer=PageTestLayer

Where should I put my tests: in a ``test_foo.py`` module, or a ``foo.txt`` doctest file?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should prefer doctests.  A good rule of thumb is that ``test_*.py`` modules
are best for tests that aren't useful for documentation, but instead for
increasing test coverage to obscure or hard-to-reach code paths.

It is very easy to write test code that says "check foo does bar", without
explaining why. Doctests tend to trick the author into explaining why.

However resist the temptation to insert tests into the system doctests
(``lib/lp/*/doc/*.txt``) that reduce their usefulness as documentation.
Tests which confuse rather than clarify do not belong here.
To a lesser extent, this also applies to other doctests too.

How to I setup my tests namespace so I can remove unwanted import statements and other noise?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For XXX DocFileSuite tests, such as the system documentation tests, you can
pass in ``setUp`` and ``tearDown`` methods. You can stuff values into the
namespace using the ``setUp`` method.


.. code-block:: python

    from zope.component import getUtility

    def setUp(test):
        test.globs['getUtility'] = getUtility


Why is my page test failing mysteriously?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is often due to a bug in the doctest code that means that ellipses
(``...``) don't match blank lines (``<BLANKLINE>``).
Inserting blank lines in the right parts of the page test should fix it.

If you are running a single test and getting odd database failures, chances are
you haven't run make schema. When running a single test the database setup step
is skipped, and you need to make sure you've done it before.

I'm writing a pagetest in the standalone directory that changes some objects. Will my changes be visible to other pagetests in this directory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. The database is reset between each standalone pagetest.

Why is my page test not failing when adding extra whitespace chars inside a textarea?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because by default, the page test ignores them so you don't need to take care
of the indentation. Sometimes, the indentation matters, e.g. inside ``<pre>``
and ``<textarea>`` tags, and if you want to test those, you will need to append
to the test ``#doctest: -NORMALIZE_WHITESPACE``, for instance:

.. code-block:: python

    >>> print(line)  #doctest: -NORMALIZE_WHITESPACE<<BR>>
    foo

What does the number in square brackets after a doctest name mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you get a warning or an error from a doctest, or you see it in a
traceback, you'll see the name written with a number in square brackets,
like this:

.. code-block:: python

    <doctest gpg-encryption.txt[16]>

The number in the text above is "16", which is the index of the "doctest
example" in that file. What this means is that the first ``>>>`` in the file is
example zero. The next ``>>>`` is example one, and so on. So ``[16]`` refers to
the seventeenth line starting with ``>>>`` in the doctest file
``gpg-encrpytion.txt``.

How do I find a backtrace?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Backtraces are kept on chinstrap in the `/srv/gangotri-logs` directory.

Should I rely on the order of os.listdir?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. The order in which results are returned by ``os.listdir`` is not defined.
Wrap your calls with ``sorted()`` if the order is important to passing the test.

How do I find the tests that cover the code I've changed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although you've written the tests first before changing code, a lot of code is
also exercised by many other tests and it's not immediately obvious which those
might be without running the whole test suite. There is an **experimental**
tool to help with this at XXX TestsFromChanges.

Sample Data
-----------

Sampledata should be innocuous, such that if it is viewed by people outside
Canonical, it will not be embarrassing or reveal company-confidential
information.

Where can I find a list of the sample users?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an aid to testing, the sample database provides a set of sample users with
differing memberships and authorization levels.

How to I make changes to the sample Launchpad database?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are making a schema change, see XXX
PolicyAndProcess/DatabaseSchemaChangesProcess.

You shouldn't make changes to sample data unless you are submitting your
changes to ``db-devel``. You can save the state of the development site's
database and replace the ``current-dev.sql`` so that everyone can see a working
site.

- ``make schema`` to create a clean db.
- Do one of these next two.
    * If you have a patch, say ``database/schema/patch-2208-99-0.sql``, apply the patch to ``launchpad_ftest_playground`` and ``launchpad_dev``.
        # ``psql -f database/schema/patch-2208-99-0.sql launchpad_ftest_playground``
        # ``psql -f database/schema/patch-2208-99-0.sql launchpad_dev``
    * Or, if you just want to change some sample data, using your browser or ``make harness``
        # make the minimum changes needs to correct or add data to create the expected state.
        # If you you can undo you mistakes using the UI and harness for many actions, but sometimes you need to start over.
- ``make newsampledata``
    * This creates ``database/sampledata/newsampledata.sql`` and ``database/sampledata/newsampledata-dev.sql``.
- Review the changes and delete any additions to the karma table or backdate them to 2005 so that the site does not change as the data ages.
    * ``diff database/sampledata/current.sql database/sampledata/newsampledata.sql``
    * ``diff database/sampledata/current-dev.sql database/sampledata/newsampledata-dev.sql``
- Move the new files into the right places.
    * ``mv database/sampledata/newsampledata.sql database/sampledata/current.sql``
    * ``mv database/sampledata/newsampledata-dev.sql database/sampledata/current-dev.sql``
- ``make schema`` again.
- Review the web site to verify your changes are correct.
- ``git commit``

Note that as a side effect of the sampledata being automatically generated, you
will often get difficult to resolve conflicts if you have modified the sample
data and attempt to merge in another branch that has also modified it.
To work around this, it is recommended that your sampledata changes are always
maintained as list of statements in a ``.sql`` file so that you can easily
reset your ``current.sql`` to the launchpad trunk and replay your changes
against it (``psql -d launchpad_dev -f mysampledatachanges.sql``).

I've only made minor changes to the sample data, but the diff is huge!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This often happens when you have modified the schema.
Don't worry - if the tests pass, then the modified sample data is good.

How do I set up connection multiplexing for my SSH session?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See XXX SshConnectionMultiplexing for details on how you might do this.

Rollouts
--------

See XXX ReleaseCycles for more information.

When will my code changes end up on production?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PQM is frozen sometime on, or shortly after, Friday of week 3.
Authorized Release Critical changes are then processed until Wednesday
afternoon when the roll-out usually happens.

Bug fixes discovered in this release on the staging server may be cherry picked
into the release. Further discussion can be found on the XXX StagingServer page.

I have an urgent bug fix
~~~~~~~~~~~~~~~~~~~~~~~~

Get it reviewed and committed to rocketfuel as normal.
If it's during Week 4, contact the release manager (usually kiko).
Otherwise, follow the PolicyandProcess/EChangePolicy

What is the staging server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The staging server is rebuilt daily using a copy of the production database and
the HEAD of launchpad. It lets you see if your code changes actually work on
the production system and performance is good.
It lives at https://staging.launchpad.net/.

Changing the launchpad dependency debs
--------------------------------------

The launchpad deb dependencies are in the ``~launchpad`` PPA:
https://launchpad.net/~launchpad/+archive/ppa.

To change them, follow the instructions on the XXX
LaunchpadPpa#launchpad-dependencies (Launchpad PPA page).

How do I run scripts with the Python environment of Launchpad?
--------------------------------------------------------------

Use ``bin/py`` in your trunk, or whatever other branch you want to use.
You might also want to use ``bin/ipy``, if you like IPython.

Pip
---

We use virtualenv and pip for our build system.

Where can I read about it?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Also see the :doc:`explanation about our pip setup <pip>`.

You can read more general information on https://pip.pypa.io/en/stable/.

How can I find out what we are using via pip?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For direct dependencies, look in ``setup.py`` in the top directory of
Launchpad.
If it is in the ``install_requires`` argument, then we are getting it from pip.

For direct and indirect dependencies, look in ``constraints.txt`` in the top
directory of Launchpad.
Note that this constrains more packages than we actually use.

How can I find out what we are using via sourcecode?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The canonical answer is to recursively find all symlinks in ``lib/`` and
``brzplugins/``.

Here's a ``find`` incantation that will list the results:

.. code-block::

    find lib brzplugins -lname '*/sourcecode/*' -ls

You should also be able to look at ``utilities/sourcedeps.conf``.
This controls what is updated when sources are updated, for instance, via
``rocketfuel-get``.

However, it is maintained manually, so it could be behind the times if someone
makes a mistake.

You do NOT answer this question by looking in the sourcecode directory.
The sourcecode directory is typically a shared resource for all your branches,
so it does not necessarily reflect what the current branch is using.
It is also not cleaned out by any of our scripts.

Is the ultimate goal to completely get rid of sourcecode, so that all packages come from pip?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

That was our original goal. We still want to shrink it to a very small size.

How do we make custom distributions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See ``doc/pip.txt``, mentioned above.  Also see XXX PolicyForDocumentingCustomDistributions.

Working with our open-source components (lazr.*)
------------------------------------------------

See XXX HackingLazrLibraries.

Where to go for other help?
---------------------------

If you have encountered a problem, maybe someone else has and has already
documented it on the XXX SolutionsLog.
Go have a look! If have a problem and you find a solution, document it there!
