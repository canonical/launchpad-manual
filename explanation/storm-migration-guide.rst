Storm Migration Guide
=====================

.. include:: ../includes/important_not_revised.rst

This guide explains how certain SQLObject concepts map to equivalent
Storm concepts. It expects a level of familiarity in how SQLObject works
(or at least how it is used in Launchpad). It is not a full tutorial on
how to use Storm either - see https://storm.canonical.com/Tutorial for
that.

Differences
-----------

Now that we've landed the Storm code, Launchpad is running on top of
Storm's SQLObject compatibility layer. This is not the end of the story
though, since we want to move to using the native Storm API. Due to the
way the compatibility layer is structured it is possible to start using
many of Storm's native APIs right away, so this will be a gradual
process rather than a single big change as with the first stage.

Connections
~~~~~~~~~~~

With SQLObject, each database class has a connection associated with it
which is used for loading objects and performing queries. With Storm,
the equivalent concept is a *Store*. Unlike SQLObject, stores are bound
to instances rather than their classes. This means that a single class
can be used to refer to objects in multiple databases (or to objects in
the same database over different DB connections, as you might want to do
in tests).

There are two main ways to access the main store. One is explicitly via
the ``IStoreSelector`` utility:

::

   #!python
   from lp.services.database.interfaces import (
       DEFAULT_FLAVOR,
       IStoreSelector,
       MAIN_STORE,
       )

   store = getUtility(IStoreSelector).get(MAIN_STORE, DEFAULT_FLAVOR)

Use the master flavor if you need to update the objects. Use the slave
flavor to offload a search to a replica database and don't mind the
search being made on data a few seconds out of date. Use the default
flavor if you don't need to make changes, but need an up to date copy of
the database (e.g. most views, as the object you are viewing might just
have been created) - Launchpad will choose an appropriate flavor.

The other method is from an existing object:

::

   #!python
   from storm.store import Store

   store = Store.of(some_object)

The second form is often more convenient, and is preferred if you don't
need to make updates and want them to play nicely with objects from an
unknown store (e.g. passed in via your method parameters).

Utility methods and Stores
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are writing a utility method like MailingListSet.get, use the
default store. Utility methods can't know whether the caller will be
writing to objects it retrieves. But the default choice makes pretty
good guesses about whether your operation needs the master store. It
uses the master store:

-  If you are in a non-web context, like a batch job
-  If you are doing a POST (which means your overall operation may
   write)
-  If you are doing a GET, but have recently written (which means the
   slaves may not have your latest changes).

So the only times you'll run into trouble are if:

-  a GET operation writes to the database
-  a GET operation relies on data that was written to the database by
   another GET
-  a GET operation relies on data that was written to the database by
   another browser instance.

We plan to address these issues better once we're using Python 2.5 and
its support for **with** statements / context management.

Adding Objects
~~~~~~~~~~~~~~

/!\\ **Note:** this section applies to classes that are not defined
using the compatibility layer. Classes using the compatibility layer
continue to provide the SQLObject behaviour.

With SQLObject, a default constructor is added to database classes that
inserts a new row in the database that takes column values as keyword
arguments. Storm does not provide a default constructor, so classes will
need to add one.

Furthermore, Storm does not add the object to the database on
instantiation: that must be done separately. There are two ways that an
object can be added to a store. It can be added directly:

::

   #!python
   store.add(object)

Or you can link it to an existing object, which will add it to that
object's store:

::

   #!python
   owner = getUtility(IPersonSet).getByEmail('test@canonical.com')
   product = Product(owner=owner) # product added to owner's store

Removing Objects
~~~~~~~~~~~~~~~~

Objects can be removed from the database using the \`Store.remove\`
method. To remove an object from its store, you can use:

::

   #!python
   from storm.store import Store

   Store.of(some_object).remove(some_object)

Getting Objects by ID
~~~~~~~~~~~~~~~~~~~~~

The equivalent of SQLObject's \`Class.get()\` method is \`Store.get`. It
takes the class and the primary key of the object as arguments:

::

   #!python
   store = getUtility(IZStorm).get('main')
   person = store.get(Person, 42)

Querying Objects
~~~~~~~~~~~~~~~~

The equivalent of SQLObject's ``select``, ``selectBy``, ``selectOne``,
``selectOneBy``, ``selectFirst`` and ``selectFirstBy`` methods is
``Store.find()``. It acts quite similar to the equivalent SQLObject
methods, and the following are equivalent:

::

   #!python
   result = store.find(Person, displayname='Some guy')
   result = store.find(Person, Person.displayname == 'Some guy')
   result = store.find(Person, "person.displayname = 'Some guy'")

Note that the "`.q.`" bit is not required in the second example. The
first two versions are preferred to direct SQL since they allow Storm to
determine which tables are being used in the query automatically. As
with SQLObject, no query is issued when executing ``find()``: that is
delayed until you try to access the result set.

The behaviour of ``selectOne`` and ``selectFirst`` are covered by the
``one`` and ``first`` methods on the result set. You can chain them with
the ``find`` call if it is appropriate:

::

   #!python
   # Raises NotOneError if there is more than one item in the result set
   person = store.find(Person, displayname='Some guy').one()

   # Raises UnorderedError if the result set has no order
   person = store.find(Person, displayname='Some guy').first()

   # Like first() but doesn't complain about unordered result sets
   person = store.find(Person, displayname='Some guy').any()

Result sets can be indexed, sliced and iterated over as with SQLObject.
An ordering can be applied to the result set with the \`order_by\`
method:

::

   #!python
   result.order_by(Person.name, Person.id)

Unlike SQLObject, the ordering is applied to the result set rather than
creating another one. The method does return the result set though, to
make it possible to chain the calls when constructing a result set.
Similar to SQLObject, a table can specify the default ordering for
results with the ``__storm_order__`` class attribute.

See the ``storm.store.ResultSet`` doc strings and the Storm tutorial for
more details on what is possible.

Defining Tables
~~~~~~~~~~~~~~~

Some of the primary differences between SQLObject and Storm database
class definitions are:

-  Subclass from ``lp.services.database.stormbase.StormBase`` instead of
   ``lp.services.database.sqlbase.SQLBase``. (Subclassing
   ``storm.base.Storm`` also works in most cases, but ``StormBase`` adds
   a ``storm_invalidate`` hook for cached properties.)
-  Use the ``__storm_table__`` attribute to set the table name instead
   of ``_table``.
-  The primary key must be defined explicitly. This will usually look
   like:

.. raw:: html

   <!-- end list -->

::

   #!python
   id = Int(primary=True)

-  The class should have a constructor if appropriate (some classes like
   ``BugSubscription`` may not need one). Note that the constructor
   should not usually add the object to a store -- leave that for a
   ``FooSet.new()`` method, or let it be inferred by a relation.
   **Barry Warsaw: what if there is no ``FooSet`` or relation? See
   question below.**
-  Default result set ordering should be set using the
   ``__storm_order__`` property rather than ``_defaultOrder``.
-  Use the column definition classes are found in \`storm.properties`,
   and do not use the ``Col`` suffix. In general, they will follow
   Python's type naming conventions rather than SQL's (e.g. TimeDelta
   rather than Interval).
-  There is no equivalent of ``alternateID=True``. The ``Store.find()``
   method provides equivalent functionality to the ``byColumnName``
   methods generated by this argument.
-  To specify that a column can not contain NULLs, use
   ``allow_none=False`` rather than ``notNull=True``. Note that if NULLs
   are found in such columns, ``NoneError`` will be raised.
-  If no ``default`` is specified for a column, the database default
   will be used. So ``default=DEFAULT`` or similar can be removed.
-  Be sure your table has a ``PRIMARY KEY`` constraint defined,
   otherwise your ``id`` column will not get set automatically and you
   will get an ``IntegrityError`` from PostgreSQL.

Foreign Key References
^^^^^^^^^^^^^^^^^^^^^^

The equivalent of SQLObject's ``ForeignKey`` class is ``Reference``. A
Storm ``Reference`` property creates a relationship between a local
column and a remote column. Unlike ``ForeignKey``, it does not implicitly
create the FK column. So the following definitions are equivalent:

::

   #!python
   # SQLObject
   owner = ForeignKey(foreignKey='Person', dbName='owner')

   # Storm
   ownerID = Int('owner')
   owner = Reference(ownerID, 'Person.id')

The columns can be passed directly to Reference(), or can be passed as
strings that are looked up on first use.

The ``Reference`` class is also used to replace SQLObject's
``SingleJoin`` class:

::

   #!python
   # SQLObject
   import_job = SingleJoin('CodeImportJob', joinColumn='code_importID')

   # Storm
   import_job = Reference(id, 'CodeImportJob.code_importID', on_remote=True)

Reference Sets
^^^^^^^^^^^^^^

The ``SQLMultipleJoin`` and ``SQLRelatedJoin`` classes are replaced by
Storm's ``ReferenceSet``:

::

   #!python
   # SQLObject
   subscriptions = SQLMultipleJoin('QuestionSubscription', joinColumn='question')
   subscribers = SQLRelatedJoin('Person',
       joinColumn='question', otherColumn='person',
       intermediateTable='QuestionSubscription', orderBy='name')

   # Storm
   subscriptions = ReferenceSet(id, QuestionSubscription.questionID)
   subscribers = ReferenceSet(id, QuestionSubscription.questionID,
                              QuestionSubscription.personID, Person.id,
                              order_by=Person.name)

While the SQLObject properties return plain result sets, the Storm
properties return ``BoundReferenceSet`` objects. Some differences
include:

-  ``add(obj)`` and ``remove(obj)`` methods are provided for adding and
   removing objects from the set. These are roughly equivalent to the
   automatic ``addFoo()`` and ``removeFoo()`` methods that SQLObject
   generates. For reference sets that join through a third table, Storm
   will take care of inserting and deleting rows as needed.
-  A ``find()`` method is provided for searching for objects within the
   reference set. This behaves a lot like ``Store.find()`` without the
   first argument.

Property Setters / Validators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SQLObject provided two ways of controlling how variables were set:

1. magic ``_set_columnName()`` methods.
2. the validator argument on column definitions.

Storm does not support magic methods but does have validators (albeit in
a simpler form than SQLObject). A validator is a function that takes
``(object, attr_name, new_value)`` as arguments and returns the value
that should be set. This allows validation to be performed on the new
value (by raising an exception on bad values), and transformation of the
value if appropriate (by returning something other than ``new_value``).

A validator can be set for a column with the ``validator`` argument in
the column definition.

You may notice some uses of ``storm_validator`` in code using the
compatibility layer. As the compatibility layer does not implement the
either of the SQLObject validation APIs, this was done to allow use of
Storm validators without completely rewriting the definitions.

Prejoins
^^^^^^^^

Storm's equivalent of prejoins is tuple finds. To select all products
that are part of ``launchpad-project`` and their owners, we can do:

::

   #!python
   launchpad_project = store.find(Project, name='launchpad-project')
   result = store.find((Product, Person),
                       Product.project == launchpad_project,
                       Product.owner == Person.id)

Iterating over this result will give us (product, person) tuples. The
above case performs an inner join, so is not appropriate for cases where
the foreign key linking the tables can be NULL. In those cases, a
slightly different syntax is needed:

::

   #!python
   from storm.expr import LeftJoin

   result = store.using(LeftJoin(Product, Project, Product.project == Project.id)).find(
       (Product, Project))

This result set will return (product, project) tuples, with project set
to None where appropriate.

If you need to select a table multiple times, it is necessary to alias
it. For example:

::

   #!python
   from storm.info import ClassAlias

   Driver = ClassAlias(Person, 'driver')
   result = store.using(LeftJoin(Product, Driver, Product.driverID == Driver.id), Person).find(
       (Product, Person, Driver), Product.owner == Person.id)

This result set will return (product, owner, driver) tuples.

Direct SQL Queries
~~~~~~~~~~~~~~~~~~

To perform direct SQL queries, we previously used the ``cursor()``
function from ``lp.services.database.sqlbase`` to get a cursor on the
connection being used by SQLObject. These uses should be converted to
use ``Store.execute()``, which will make sure pending changes have been
flushed to the database first in order to stay consistent.

This method returns a result object with ``get_one`` and ``get_all``
methods that act like a cursor's ``fetchone`` and ``fetchall`` methods.
It also supports iteration.

::

   #!python
   result = store.execute("SELECT name FROM person ORDER BY name")
   names = result.get_all()

Migration Plan
--------------

A good order to migrate code is:

1. Convert column properties to use the Storm syntax. This should be a
   no-op change, and not affect external code.
2. Convert ``ForeignKey()`` definitions to an appropriate pair of
   ``Int()`` and ``Reference()`` definitions.
3. Convert ``sync()``, ``syncUpdate()``, ``destroySelf()``, etc calls to
   Storm equivalents.
4. Convert uses of ``Class.select*()`` to use ``find()``. Note that you
   lose prejoins support here, so use tuple finds as appropriate. Change
   queries to use Storm expressions rather than sqlbuilder expressions.
5. Convert ``SQLMultipleJoin`` and ``SQLRelatedJoin`` to
   ``ReferenceSet()``. As this changes the API of the class a bit, it
   will probably require changes external to the class.
6. Change the class to derive from
   ``lp.services.database.stormbase.StormBase`` instead of ``SQLBase``.

This list is roughly ordered based on the locality of changes and based
on dependencies between changes.

For new code, consider using native Storm API from the start, rather
than continuing to use the compatibility layer.

Tips on Converting Tests
------------------------

From "Tips in converting tests to Storm", May 30, 2008,

::

   Below are some tips on writing Storm code for Launchpad.  I won't go
   too deep into the Storm API, and instead concentrate on some of the
   differences between SQLObject and Storm's SQLObject compatibility
   layer.

   1. Storm is stricter with respect to the types it accepts in various
   situations.  Most of the cases where this has caused problems in tests
   have indicated problems in Launchpad or its tests.  Below are a number
   of the common problems I've encountered:

   (a) The SQLObject EnumCol accepts values other than enumeration values
   on the Python side.  With the upgrade to Storm, things are a bit
   stricter, and the correct enumeration values need to be passed in.

   I found a few cases where some code had an enumeration value and then
   passed in item.value.  In a few tests, the numeric constants were
   being used.

   This affects both creating/updating objects and building queries.

   (b) When assigning to a foreign key attribute, you need to assign an
   object of the right type.  It seems that SQLObject would accept any
   class for such assignments.  And provided a row from the correct table
   existed with the same ID existed you'd get no complaints from the
   database.  There were a few tests that had bugs like this.

   (c) SQLObject lets you assign a result set to a foreign key reference
   when creating or updating an object, while Storm does not.

   This might sound like a missing feature, except for the fact that
   SQLObject seems to treat result sets as NULLs when generating SQL.  So
   any new errors caused by this are genuine errors.

   2. Storm flushes changes to the database implicitly before various
   operations.  In general, this is good since you don't need to remember
   to flush changes before running select().  That said, we have a number
   of cases where we have code that relies on changes not being flushed
   to disk.  Some examples include:

   * the code to warn about assigning bugs to non developers transitioned
   to the new assignee and then checked to see if the new assignee had
   any bugs assigned to them.  As Storm flushed the change in assignee,
   it always looked like the user had assigned bugs.  Switching the order
   of these two operations fixed the bugs.

   * Some of the PPA tests would set a PPA to private and then set the
   buildd password.  Database constraints require that private PPAs have
   a password, so in some tests where a flush occurred between the two
   operations an IntegrityError was raised.  Reordering the two
   statements fixed the problem.

   Of course, there are cases where it is useful to have implicit flushes
   turned off.  There is an API to block implicit flushes, and I've made
   use of it for our security policy (which could otherwise introduce
   flushes to almost any attribute access) and most event subscribers.
   I've done this in most cases with the
   lp.services.database.sqlbase.block_implicit_flushes function decorator.

   3. Storm flushes some changes later than SQLObject.  Namely inserts or
   deletes to the database.  Furthermore, the order that objects are
   added in a single flush is not defined.  This exhibits itself in two
   ways:

   * If inserting a row would cause an integrity error, that error will
   occur at flush time rather than object construction time.  Tests for
   such failures need to explicitly flush the object.

   * Some tests would create a number of objects in a single flush group
   and expect them to have IDs in the same order.  Such tests need to
   either take this into account or add explicit flushes to preserve the
   ordering.

   * In cases where objects are created that reference each other in a
   loop, a manual flush will be needed before closing the loop.
   Otherwise Storm won't know what order to insert them in.

   4. sqlbuilder expressions do not yield SQL from str().  Storm uses
   quite a different method to convert sql expression objects to SQL
   statements, and this is a result of that.  There were a few cases of
   code that took a builder expression and substituted it into a string
   to form a larger query.  I've generally fixed cases like this by
   converting the string expression to builder objects.

   Constant expressions (e.g. UTC_NOW) will still work with sqlvalues(),
   but not when substituted directly.


   James.

Questions
---------

12-Aug-2008

-  Some of our ForeignKey columns had ``notNull=True`` but Storm's Reference
   class does not accept ``allow_none=False`` keyword argument. 

   -  Put the ``allow_none=False`` on the ``Int`` rather than on the
      ``Reference``.

.. raw:: html

   <!-- end list -->

-  How to actually convert a UtcDateTimeCol to a DateTime? For now, I'm
   using a DateTime with ``tzinfo=pytz.timezone('UTC')`` keyword argument. 
   Also, does ``default=UTC_NOW`` still work?

   - Use ``default_factory=datetime.utcnow`` instead.

.. raw:: html

   <!-- end list -->

-  Can I still use EnumCol, or is there a better way to hook up with our DBEnums?

   -  Try ``lp.services.database.enumcol.DBEnum``.

.. raw:: html

   <!-- end list -->
   
03-Oct-2008

-  I'm still confused about the right way to add an object to a store. 
   If I'm using native Storm APIs (as all new code should, right?) should 
   I add a ``Store.add()`` call my database object's ``__init__()``? 
   That seems to be the most straightforward translation of the SQLObject compatibility layer. 
   And if the answer is "yes", then how do I get the Store to use?
   I could use ``Store.of(someobj).add(self)`` but ``someobj`` might not be in the right store. 
   I could use the ``getUtility()`` trick, but it seems wrong that a database 
   module should be importing an interface from ``webapp``.
