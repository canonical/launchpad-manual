Datetime Usage Guide
====================

.. include:: ../includes/important_not_revised.rst

There are a number of places in Launchpad where ``datetime`` types are used:

-  Python code
-  in the database as table columns
-  Storm wrappers for database tables, which act as an adapter between
   the above two
-  TALES fmt:date , fmt:time and fmt:datetime formatters.

Furthermore, there are two main ``datetime`` types in use:

-  timestamps, which identify a particular point in time
-  time deltas, which identify an interval in time

Data Types
----------

Python
~~~~~~

We use the standard ``datetime`` module to represent time stamps and time
deltas -- the ``datetime.datetime`` type for timestamps, and the
``datetime.timedelta`` type for time deltas.

To make matters a little bit more complicated, there are actually two
types of ``datetime.datetime`` objects:

1. naïve datetime objects
2. timezone aware datetime objects

While both objects share the same Python type, they can not be compared
with each other. Where possible, we use timezone aware ``datetime`` objects.

A timezone aware ``datetime`` can be created with the following code:

.. code:: python

   import datetime
   import pytz

   UTC = pytz.timezone('UTC')
   dt = datetime.datetime(2005, 1, 1, 8, 0, 0, tzinfo=UTC)

The ``pytz.timezone()`` function can be used to retrieve tzinfo objects for any
of the named Olsen time zones. A ``datetime`` value can be converted to another
time zone as follows:

.. code:: python

   perth_tz = pytz.timezone('Australia/Perth')
   perth_time = dt.astimezone(perth_tz)

PostgreSQL
~~~~~~~~~~

In PostgreSQL, the ``TIMESTAMP WITHOUT TIME ZONE`` should be used to represent
timestamps, and ``INTERVAL`` should be used to represent time deltas.
All timestamp columns in the database should store the time in UTC.

While PostgreSQL has a ``TIMESTAMP WITH TIME ZONE`` type, it should not be used.
The difference between the two column types is that the value of a
``TIMESTAMP WITH TIME ZONE`` column will be converted to local time when being
read, and the reverse occurs when being written.
It does **not** actually store a time zone with the timestamp.

Storm
~~~~~

To wrap a timestamp database column, use the ``storm.properties.DateTime``

type. To wrap an interval database column, use the
`storm.properties.TimeDelta`` type:

.. code:: python

   import pytz
   from storm.properties import (
       DateTime,
       TimeDelta,
       )

   from lp.services.database.stormbase import StormBase

   class TableName(StormBase):
       timestamp = DateTime(name='timestamp', tzinfo=pytz.UTC)
       interval = TimeDelta(name='interval')

Page Templates
~~~~~~~~~~~~~~

Inside page templates, use the following TALES formatters to present
timestamp objects:

-  ``fmt:date``
-  ``fmt:time``
-  ``fmt:datetime``
-  ``fmt:approximatedate``

The preferred method of presenting datetime is:

.. code:: xml

   <tal:created
     replace="structure context/datecreated/fmt:approximatedatetitle" />

When in doubt, use this presentation.

If the timestamp has a time zone attached, these formatters will convert
the date to the user's local time before display.

For time interval objects, use the following formatters:

-  ``fmt:exactduration``
-  ``fmt:approximateduration``

Two Concepts of "Now"
---------------------

When working with the database, there are two distinct concepts of "now"
to work with:

1. the time when the code is running (e.g. returned by datetime.now() ).
2. the database transaction time (when the transaction is committed, all
   the changes will appear to have happened atomically at that time).

Usually these two mean almost the same thing, but they will differ under
the following conditions:

-  clock skew between the application server and database server (should
   not be a problem on our servers).
-  with long running transactions, the second "now" will be the time at
   the start of the transaction.

In cases where you are comparing timestamps, mixing the two concepts of
"now" can result in race conditions. In most cases in Launchpad, the
database transaction time is the correct one to use.

Database Transaction Time
~~~~~~~~~~~~~~~~~~~~~~~~~

Storing the current database transaction time in the database use the
following syntax:

.. code:: python

   from lp.services.database.constants import UTC_NOW

   person.datecreated = UTC_NOW

.. note::

    You won't be able to read the value as a Python ``datetime``
    object until the object is flushed to the database, or the transaction
    is committed.

To store a time relative to the present time in a database column, we
can make use of the fact that ``UTC_NOW`` is an ``SQL()`` type:

.. code:: python

   membership.dateexpires = UTC_NOW + datetime.timedelta(months=6)

The database transaction time can be retrieved using
``lp.services.database.sqlbase.get_transaction_timestamp``.

Present Time
~~~~~~~~~~~~

To create a Python ``datetime`` object that represents the present time, use
the following code:

.. code:: python

   import datetime
   import pytz

   UTC = pytz.timezone('UTC')
   dt = datetime.datetime.now(UTC)

Note that the ``datetime.utcnow()`` method should not be used -- it creates a
naïve ``datetime`` value, which can not be compared against other values in
Launchpad.
