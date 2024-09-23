Database performance
====================

.. include:: ../includes/important_not_revised.rst

Poor query times - looks right, takes ages
------------------------------------------

Normally, the simplest form of the query is the fastest.

Checklist of known problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. subselects, EXISTS, IS IN - these can be useful for optimizing
   particular edge cases, but can degrade performance for the normal
   cases.

2. database views. These used to be useful to keep our code sane, but it
   is now clearer to use Storm to express the view logic from the client
   side. Database views now serve little purpose for us except to hide
   unnecessary joins that will degrade performance.

3. bad query plans generated on the DB server - talk to a team lead to
   get an explain analyze done on staging, or to Stuart or a LOSA to get
   the same done on production (if the staging one looks ok its
   important to check production too).

``   Bad plans can happen due to out of date statistics or corner cases.  Sometimes rewriting the query to be simpler/slightly different can help. Specific things to watch out for are nested joins and unneeded tables (which can dramatically change the lookup).``

4. fat indices - if the explain looks sensible, talk to Stuart about
   this.

5. missing indices - check that the query should be indexable (and if in
   doubt chat to Stuart).


6. using functions in ORDER BY: calling functions on every row of an
   intermediary table - if a sort cannot be answered by iterating an
   index then postgresql will generate an intermediate table containing
   all the rows that match the constraints, and sort that in-memory;
   functions that affect the sort order have to be evaluated before
   doing the sort - and thus before any LIMIT occurs.

7. Querying for unrelated tables. Quite possibly either prejoins, or
   prepopulation of derived attributes. Look for a code path that is
   narrower, or pass down a hint of some sort about the data you need so
   the actual query can be more appropriate. Sometimes more data is
   genuinely needed but still messes up the query: consider using a
   later query rather than prejoining. E.g. using the pre_iter_hook of
   DecoratedResultSet to populate the storm cache.

Many small queries [in a webapp context] -- Late Evaluation
-----------------------------------------------------------

Databases work best when used to work with sets of data, not objects -
but we write in python, which is procedural and we define per-object
code paths.

One particular trip up that can occur is with related and derived data.

Consider:

::

   def get_finished_foos(self):
       return Store.of(self).find(Foo, And(Foo.me == self.id, Foo.finished == True))

This will perform great for one object, but if you use it in a loop
going over even as few as 30 or 40 objects you will cause a large amount
of work - 30 to 40 separate round trips to the database.

Its much better to prepopulate a cache of these finished_foos when you
request the owning object in the first place, when you know that you
will need them.

To do this, use a Tuple Query with Storm, and assign the related objects
to a cached attribute which your method can return. For attributes the

::

   @cachedproperty('_foo_cached')

can be used to do this in combination with a

::

   DecoratedResultSet

Be sure to clear these caches with a Storm invalidation hook, to avoid
test suite fallout. Objects are not reused between requests on the
appservers, so we're generally safe there. (Our storm and SQLBase
classes within the Launchpad tree have these hooks, so you only need to
manually invalidate if you are using storm directly).

A word of warning too - Utilities will often get in the way of
optimising this :)

Diagnosis Tools and Approaches
------------------------------

EXPLAIN ANALYZE on staging and qastaging can be used by LOSAs, the TAs,
and squad leads.

If you want to see how a query is working on a GET page locally, try the
`++oops++ <Debugging#Special%20URLs>`__ and
`++profile++ <Debugging#Profiling%20page%20requests>`__ tools.
++profile++ reportedly works on staging and qastaging now too.

Unfortunately, they sometimes do not work properly for POSTs, and can't
be used in other scenarios. See Bug:641969, for instance.

If you are working on a test and want to see how a query is working, try
one of these tools.

-  Use the built-in Storm debug tracer. If you start with this...

::

      def test_some_storm_code(self):
          < some setup logic >
          < the Storm-using code I'm curious about >
          < more stuff >
    

``...then you can use the debug tracer to see what's going on.  When you run your tests after changing the code to look like the below, stdout will include the queries run, and timestamps for start and finish.``

::

      def test_some_storm_code(self):
          < some setup logic >
          from storm.tracer import debug; debug(True)
          try:
              < the Storm-using code I'm curious about >
          finally:
              debug(False)
          < more stuff >
    

-  StormStatementRecorder, LP_DEBUG_SQL=1, LP_DEBUG_SQL_EXTRA=1,
   QueryCollector. In extremes you can also turn on statement logging in
   postgresql. [Note: please add more detail if you are reading this and
   have the time and knowledge.]
-  Raise an exception at a convenient point, to cause a real OOPS.

Efficient batching of SQL result sets: StormRangeFactory
--------------------------------------------------------

Batched result sets are rendered via the class
canonical.launchpad.webapp.batching.BatchNavigator. (This class is a
thin wrapper around lazr.batchnavigator.BatchNavigator.)

BatchNavigator delegates the retrieval of batches from a result set to
an IRangeFactory (defined in lazr.batchnavigator.interfaces). The
default range factory is lazr.batchnavigator.ListRangeFactory.

This factory uses regular Python slicing to access a batch, which is
mapped by the ORM to a query like

::

       SELECT ... FROM ... OFFSET o LIMIT l;

for a slice operation result_set[o:o + l].

Finding the end of the result set, and skipping to the right offset, can
be very expensive for result sets with large numbers of rows.
StormRangeFactory uses a different approach: Given a query

::

       SELECT * FROM Table ORDER BY Table.column1, Table.column2;

and given a batch where the values of column1, column2 in last row of
the batch are value1, value2, it generates a query for the next batch by
adding a WHERE clause:

::

       SELECT * FROM Table WHERE (column1, column2) > (value1,  value2)
           ORDER BY Table.column1, Table.column2 LIMIT batchsize+1;

Usage
~~~~~

The main change to use StormRangeFactory is simple: Just replace

::

       batchnav = BatchNavigator(resultset, request)

with

::

       from canonical.launchpad.webapp.batching import StormRangeFactory
       batchnav = BatchNavigator(
           resultset, request, range_factory=StormRangeFactory(resultset))

Limitations
~~~~~~~~~~~

StormRangeFactory needs access to the columns used for sorting; it
retrieves the values of the sort columns automatically, using the
resultset.order_by() parameters. This has several consequences:

1. Result sets must be entire model objects:

::

       store.find(Person)
       store.order_by(Person.id)

can be used with StormRangeFactory, but

::

       store.find(Person.id)
       store.order_by(Person.id)

can not be used.

2. The order_by parameters must be Storm Column instances, optionally
wrapped into Desc().

::

       resultset.order_by(Person.id)
       resultset.order_by(Desc(Person.id))

works, but

::

       resultset.order_by('Person.id')

does not work.

3. Obviously, all sort columns must appear in the result set. This means
that

::

       resultset = store.find(
           BugTask, BugTask.product == Product, Product.project == context)
       resultset.order_by(Product.name, BugTask.id)

does not work. Use

::

       resultset = store.find(
           (BugTask, Product), BugTask.product == Product,
           Product.project == context)
       resultset.order_by(Product.name, BugTask.id)

instead and wrap this result set into DecoratedResultSet.

4. StormRangeFactory works only with regular Storm ResultSets and with
DecoratedResultSets, but not with legacy SQLObjectResultSets.

::

       resultset = store.find(Person)
       resultset.order_by(Person.id)

works, but

::

          resultset = Person.select(...)

does not work.

5. The begin of a batch is represented in URLs by the query parameter

For BatchNavigator, this parameter is an arbitrary string.
StormRangeFactory uses a class
DateTimeJSONEncoder(simplejson.JSONEncoder) to represent the sort column
values as a string. This means that only data types supported by
simplejson and datetime instances may be used for sorting the SQL result
set.
