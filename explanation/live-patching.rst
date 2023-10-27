Live Database Patching
======================

.. include:: ../includes/important_not_revised.rst

This page documents the schema changes that can be deployed on
Launchpad's replicated PostgreSQL database.

We use Hot schema changes to deploy changes without causing downtime.

And we use Cold schema changes to deploy changes with minimal (a few
seconds per change) downtime.

In both cases, we deploy these changes without changing the running
appserver code, so the changes need to be compatible with the existing
live code. This means that, before landing the database patch, code may
need to be landed to ensure everything runs both with and without the
database patch applied.

Cold schema changes are landed on db-devel, and hot ones on devel. All
schema changes must land without appserver code changes (but test
changes may be included, if trigger/db function changes are being
landed).


.. note::

    These instructions only apply to tables under native PostgreSQL
    streaming replication. ``lp_*`` tables are replicated to SSO via Slony,
    so require extra special care.

Hot patches
-----------

Some database patches we can apply live. They are currently applied by
crafting an appropriate wrapper script and then running it directly on
the master database node, from where it will replicate to the slaves.

The (major, minor, patch) revision tuple needs to be manually inserted
into the XXX LaunchpadDatabaseRevision table on the master. Failing to do
this will abort the next full upgrade when the system attempts to apply
a patch that has already been applied (this situation is normally caught
by the full staging update).

We will be automating this in future, to handle at least the happy-path
and avoiding accidentally running a hot patch during a fastdowntime.

Index Creation
~~~~~~~~~~~~~~

Index creation for all but the smallest tables should be done in a hot
patch.

The patch needs to use CREATE INDEX CONCURRENTLY which will do 3
separate fast transactions to make, populate, and activate the index.
There is some contention added but it is minimal.

Don't bother starting index creation when there are long running
transactions in progress. The indexes will not complete until the long
running transactions have completed. (Because the index has to wait for
the existing read transactions on the table to complete before it can be
activated.

CREATE INDEX CONCURRENTLY cannot run inside a transaction, so if the
index cannot be built for some reason, such as trying to build a UNIQUE
index on non-unique data, manual repair will be needed to back out the
changes. /!\\ Note that deleting an index requires a fastdowntime
deploy.

Once built on the master, the index will automatically replicate to the
slaves.

Index creation should be done from a screen(1) session or similar to
avoid network dropouts - for CREATE INDEX CONCURRENTLY, early
disconnection will result in an invalid index rather than rolling back.

After creating the indexes, confirm that there are no invalid indexes on
the affected tables.

Views
~~~~~

Run the CREATE OR REPLACE VIEW statements on the master.

Stored Procedures
~~~~~~~~~~~~~~~~~

Stored procedures can be changed (as long as the signature is still
consistent with any triggers).

Table trigger definitions must be done as cold patches.

Cold Patches
------------

Cold patches need to be applied with no other system activity to prevent
locks holding the patch up. We have automation around this to do it as
rapidly as possible.

Patch Process Overview
~~~~~~~~~~~~~~~~~~~~~~

1. Update wildcherry Launchpad source tree to the revision to run: make
   sure that the revision will only include one new patch (we do one
   patch at a time to reduce the debugging burden when something goes
   wrong post-apply), and run 'make clean build'.

2. Run full-update.py --dry-run and check that only the expected db
   patch will be applied.

3. Run full-update.py

Table Creation
~~~~~~~~~~~~~~

This can sometimes be done hot, but not reliably due to FK relations
needing exclusive table locks to activate. Do it as a cold patch.

/!\\ Don't attempt to do this without the DBA available, as there still
seem to be edge cases where we cannot do this live (such as a table with
foreign key constraints to a busy table, requiring locks on the busy
table that will not be granted quickly enough).

Table Renaming
~~~~~~~~~~~~~~

Because code is being deployed separately from database updates, we need
to maintain a fully updateable working alias for the old table name to
the new table name. See
`Database/TableRenamePatch <Database/TableRenamePatch>`__ for an example
database patch.

Adding columns
~~~~~~~~~~~~~~

If the table is large enough that applying the patch raises performance
concerns, split the work up into the following steps. All steps, aside
from the first, are optional depending on the desired result.

1. Create the column without indices and without setting not-null or a
   default value.
2. Set the default
3. Add the index via a hot patch
4. Run a garbo job (or similar) to fill in the values
5. Set the column not-null.

TODO
----

-  Work out how we test things work both with and without the database
   patch applied.
