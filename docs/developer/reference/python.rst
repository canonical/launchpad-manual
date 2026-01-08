==================
Python style guide
==================

This document describes expected practices when writing Python code.  There
are occasions when you can break these rules, but be prepared to justify
doing so when your code gets reviewed.

Existing Conventions
====================

There are well-established conventions in the Python community, and in
general we should follow these.  General Python conventions, and required
reading:

* `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_: Style Guide for
  Python Code
* `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_: Docstring
  Conventions
* The Zen of Python: ``python3 -c "import this"``

Note that our standards differ slightly from PEP-8 in some cases.

Coding standards other projects use:

* `Twisted Coding Standard
  <https://docs.twistedmatrix.com/en/stable/development/coding-standard.html>`_
* `Zope developer guidelines
  <https://www.zope.org/developer/guidelines.html>`_

Related Documents
=================

* `Exception guidelines <https://dev.launchpad.net/ExceptionGuidelines>`_
* :ref:`Assertions <assertions-in-launchpad>`
* `Launchpad hacking FAQ <https://dev.launchpad.net/LaunchpadHackingFAQ>`_
* :doc:`Tests style guide <tests>`

Formatting
==========

We delegate most formatting decisions to `black
<https://github.com/psf/black>`_.  All Python code (except for a few files
specifically excluded in ``.pre-commit-config.yaml``) must be formatted
using it.  You should be using Launchpad's default :ref:`pre-commit
<pre-commit>` setup, which automatically formats your code using ``black``
and ``isort`` before you commit.

Naming
======

Consistency with existing code is the top priority.  We follow PEP-8 with
the following exceptions:

* ``CamelCase``: classes, interfaces (beginning with ``I``)
* ``initialCamelCase``: methods
* ``lowercase_underscores``: functions, non-method attributes, properties,
  local variables
* ``ALL_CAPS``: constants

Private names are private
-------------------------

You should never call a non-public attribute or method from another class.
In other words, if class A has a method ``_foo()``, don't call it from
anywhere outside class A.

Docstrings
==========

* If you haven't already, read `PEP 257
  <https://www.python.org/dev/peps/pep-0257/>`_.
* In general, everything that can have a docstring should: modules, classes,
  methods, functions.
* Docstrings should always be enclosed in triple double quotes: ``"""Like
  this."""``
* When a class or a method implements an interface, the docstring should say
  ``"""See `IFoo`."""``

Docstrings should be valid `reStructuredText
<https://docutils.sourceforge.io/rst.html>`_ (with all the painful
indentation rules that implies) so that tools such as `pydoctor
<https://pypi.org/project/pydoctor/>`_ can be used to automatically generate
API documentation.

You should use field names as defined in the `epydoc
<https://epydoc.sourceforge.net/fields.html>`_ documentation but with reST
syntax.

Using \`name\` outputs a link to the documentation of the named object, if
pydoctor can figure out what it is.

Here is a comprehensive example.  Parameter descriptions are a good idea but
not mandatory.  Describe in as much or as little detail as necessary.

.. code-block:: python

    def example2(a, b):
        """Perform some calculation.

        It is a **very** complicated calculation.

        :param a: The number of gadget you think this
                  function should frobnozzle.
        :type a: ``int``
        :param b: The name of the thing.
        :type b: ``str``
        :return: The answer!
        :rtype: ``str``.
        :raise ZeroDivisionError: when ``a`` is 0.
        """

Modules
=======

Each module should look like this:

.. code-block:: python

    # Copyright 2009-2011 Canonical Ltd.  All rights reserved.

    """Module docstring goes here."""

    __all__ = [
        ...
    ]

The file ``standard_template.py`` has most of this already, so save yourself
time by copying that when starting a new module.  The "..." should be filled
in with a list of public names in the module.

PEP-8 says to put any relevant ``__all__`` specifications after the module
docstring but before any import statements (except for ``__future__``
imports, which in most cases we no longer use).  This makes it easy to see
what a module contains and exports, and avoids the problem that differing
amounts of imports among files means that the ``__all__`` list is in a
different place each time.

.. _imports:

Imports
=======

Restrictions
------------

There are restrictions on which imports can happen in Launchpad.  Namely:

* View code cannot import code from ``lp.*.model``.
* ``import *`` cannot be used if the module being imported from does not
  have an ``__all__``.
* Database code may not import ``zope.exceptions.NotFoundError`` -- it must
  instead use ``lp.app.errors.NotFoundError``.

These restrictions are enforced by the Import Pedant, which will cause your
tests not to pass if you don't abide by the rules.

Use absolute imports (``from foo.bar import Bar``), not relative imports
(``from .bar import Bar``).

Import scope
------------

We encourage importing names from the location they are defined in.  This
seems to work better with large complex components.

Circular imports
----------------

With the increased use of native Storm APIs, you may encounter more circular
import situations.  For example, a ``MailingList`` method may need a
reference to the ``EmailAddress`` class for a query, and vice versa.  The
classic way to solve this is to put one of the imports inside a method
instead of at module global scope (a "nested import").

Short of adopting something like Zope's lazy imports (which has issues of
its own), you can't avoid this, so here are some tips to make it less
painful.

* Do the nested import in the least common case.  For example, if 5 methods
  in ``model/mailinglist.py`` need access to ``EmailAddress`` but only one
  method in ``model/emailaddress.py`` needs access to ``MailingList``, put
  the import inside the ``emailaddress.py`` method, so you have fewer
  overall nested imports.
* Clearly comment that the nested import is for avoiding a circular import,
  using the example below.
* Put the nested import at the top of the method.

.. code-block:: python

    def doFooWithBar(self, ...):
        # Import this here to avoid circular imports.
        from lp.registry.model.bar import Bar
        # ...
        return store.find((Foo, Bar), ...)

Circular imports and webservice exports
---------------------------------------

One of the largest sources of pain from circular imports is caused when you
need to export an interface on the webservice.  Generally, the only way
around this is to specify generic types (like the plain old ``Interface``)
at declaration time and then later patch the webservice's data structures at
the bottom of the interface file.

Fortunately there are some helper functions to make this less painful, in
``lib/lp/services/webservice/apihelpers.py``.  These are simple functions
where you can give some info about your exported class/method/parameters and
they do the rest for you.

For example:

.. code-block:: python

    from lp.services.webservice.apihelpers import (
        patch_entry_return_type,
        patch_collection_return_type,
    )
    patch_collection_return_type(
        IArchive, "getComponentsForQueueAdmin", IArchivePermission
    )
    patch_entry_return_type(IArchive, "newPackageUploader", IArchivePermission)

Properties
==========

Properties are expected to be cheap operations.  It is surprising if a
property is not a cheap operation.  For expensive operations use a method,
usually named ``getFoo()``.  Using ``cachedproperty`` provides a work-around
but it should not be overused.

Truth conditionals
==================

Remember that False, None, [], and 0 are not the same although they all
evaluate to False in a boolean context.  If this matters in your code, be
sure to check explicitly for either of them.

Also, checking the length may be an expensive operation.  Casting to bool
may avoid this if the object specializes by implementing ``__bool__``.

Chaining method calls
=====================

Since in some cases (e.g. class methods and other objects that rely on
descriptor ``__get__()`` behaviour) it's not possible to use the old style
of chaining method calls (``SuperClass.method(self, ...))``, we should
always use the ``super()`` builtin when we want that. 

.. note::

    The exception to this rule is when we have class hierarchies outside of
    our control that are known not to use ``super()`` and that we want to
    use for diamond-shaped inheritance.

Use of lambda, and operator.attrgetter
======================================

Prefer `operator.attrgetter
<https://docs.python.org/3/library/operator.html#operator.attrgetter>`_ to
``lambda``.  Remember that giving functions names makes the code that calls,
passes and returns them easier to debug.

Database-related
================

ORM
---

We are using the `Storm <https://storm-orm.readthedocs.io/en/latest/index.html>`_ ORM.

Field attributes
----------------

When you need to add ID attributes to your database class, use ``field_id``
as the attribute name instead of ``fieldID``.

Multi-line SQL
--------------

SQL doesn't care about whitespace, so use triple quotes for large SQL
queries or fragments, e.g.:

.. code-block:: python

    query = """
        SELECT TeamParticipation.team, Person.name, Person.displayname
        FROM TeamParticipation
        INNER JOIN Person ON TeamParticipation.team = Person.id
        WHERE TeamParticipation.person = %s
    """ % sqlvalues(person_id)

This is also easy to cut-and-paste into ``psql`` for interactive testing,
unlike if you use several lines of single quoted strings.

Creating temporary files
========================

We should use the most convenient method of the ``tempfile`` module.  Never
taint ``/tmp/`` or any other "supposed to be there" path.

Despite being developed and deployed on Ubuntu systems, turning it into a
restriction might not be a good idea.

When using ``tempfile.mkstemp`` remember it returns an open file descriptor
which has to be closed or bound to the open file, otherwise they will leak
and eventually hit the default Linux limit (1024).

There are two good variations according to the scope of the temporary file.

.. code-block:: python

    fd, filename = mkstemp()
    os.close(fd)
    ...
    act_on_filename(filename)

Or:

.. code-block:: python

    fd, filename = mkstemp()
    with os.fdopen(fd, "w") as temp_file:
        ...
        temp_file.write("foo")

**Never** use:

.. code-block:: python

    fd, filename = mkstemp()
    with open(filename) as temp_file:
        temp_file.write("foo")
    # BOOM! 'fd' leaked.

In tests, you should use the ``TempDir`` fixture instead, which cleans
itself up automatically:

.. code-block:: python

    from fixtures import TempDir

    class TestFoo(TestCase):
    ...
        def test_foo(self):
            tempdir = self.useFixture(TempDir).path
            ...
            do_something(os.path.join(tempdir, "test.log"))
            ...

Configuration hints
===================

Vim
---

To make wrapping and tabs fit the above standard, you can add the following
to your ``.vimrc``:

.. code-block:: vim

    autocmd BufNewFile,BufRead *.py set tw=78 ts=4 sts=4 sw=4 et

To make trailing whitespace visible:

.. code-block:: vim

    set list
    set listchars=tab:>.,trail:-

This will also make it obvious if you accidentally introduce a tab.

To make long lines show up:

.. code-block:: vim

    match Error /\%>79v.\+/

For an even more in-depth Vim configuration, have a look at
`VIM and Python <https://realpython.com/vim-and-python-a-match-made-in-heaven/>`_.

Emacs
-----

There are actually two Emacs Python modes.  Emacs comes with ``python.el``
which has some quirks and does not seem to be as popular among hardcore
Python programmers.  `python-mode.el <https://launchpad.net/python-mode>`_
comes with XEmacs and is supported by a group of hardcore Python
programmers.  Even though it's an add-on, it works with Emacs just fine.
