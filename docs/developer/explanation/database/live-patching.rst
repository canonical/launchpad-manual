.. meta::
   :description: Understand live database patching techniques for deploying 
      schema changes on Launchpad's PostgreSQL database.

.. _live-database-patching:

Live database patching
======================

This page describes the schema changes that we can deploy on Launchpad's
replicated PostgreSQL database, and the two mechanisms we use to apply them:

- **Hot schema changes** deploy changes without causing any downtime.
- **Cold schema changes** deploy changes with minimal downtime (a few seconds
  per change).

In both cases, we deploy the changes without altering the running appserver
code, so each change must be compatible with the existing live code. This means
that, before landing a database patch, we may need to land code first so that
everything runs both with and without the patch applied. For the end-to-end
workflow, see :ref:`database-schema-changes-process`.

We land cold schema changes on ``db-devel`` and hot ones on ``devel``. All
schema changes must land without appserver code changes, although test changes
may be included when trigger or database function changes are being landed. For
more on developing against the ``db-devel`` branch, see
:ref:`working-with-db-devel`.

.. note::

   These instructions only apply to tables under native PostgreSQL streaming
   replication. ``lp_*`` tables are replicated to SSO via Slony, so they
   require extra special care. See :ref:`postgresql-and-launchpad` for more on
   how Launchpad uses replication.

Hot patches
-----------

We can apply some database patches live. We currently apply them by crafting an
appropriate wrapper script and then running it directly on the master database
node, from where it replicates to the slaves.

The ``(major, minor, patch)`` revision tuple must be manually inserted into the
``LaunchpadDatabaseRevision`` table on the master. Failing to do this aborts the
next full upgrade, because the system attempts to apply a patch that has already
been applied. This situation is normally caught by the full staging update.

We intend to automate this in the future, to at least handle the happy path and
avoid accidentally running a hot patch during a fastdowntime deployment.

Index creation
~~~~~~~~~~~~~~

Index creation for all but the smallest tables should be done in a hot patch.

The patch must use ``CREATE INDEX CONCURRENTLY``, which runs three separate fast
transactions to create, populate, and activate the index. This adds some
contention, but it is minimal.

Don't start index creation while there are long-running transactions in
progress: the index will not complete until those transactions have completed,
because it has to wait for the existing read transactions on the table to finish
before it can be activated.

``CREATE INDEX CONCURRENTLY`` cannot run inside a transaction, so if the index
cannot be built for some reason, such as trying to build a ``UNIQUE`` index on
non-unique data, manual repair is needed to back out the changes.

.. warning::

   Deleting an index requires a fastdowntime deploy.

Run index creation from a ``screen(1)`` session or similar to avoid network
dropouts: for ``CREATE INDEX CONCURRENTLY``, an early disconnection results in
an invalid index rather than a rollback.

Once the index is built on the master, it replicates automatically to the
slaves. After creating the indexes, confirm that there are no invalid indexes 
on the affected tables.

Views
~~~~~

Run the ``CREATE OR REPLACE VIEW`` statements on the master.

Stored procedures
~~~~~~~~~~~~~~~~~

Stored procedures can be changed, as long as the signature is still consistent
with any triggers. Table trigger definitions must be done as cold patches.

Cold patches
------------

Cold patches must be applied with no other system activity, to prevent locks
from holding the patch up. We have automation around this to apply them as
rapidly as possible.

Patch process overview
~~~~~~~~~~~~~~~~~~~~~~

1. Update the ``wildcherry`` Launchpad source tree to the revision to run. Make
   sure that the revision will include only one new patch. We apply one patch
   at a time to reduce the debugging burden when something goes wrong after
   applying it, and run ``make clean build``.

2. Run ``full-update.py --dry-run`` and check that only the expected database
   patch will be applied.

3. Run ``full-update.py``.

Table creation
~~~~~~~~~~~~~~

Creating a table can sometimes be done hot, but not reliably, because foreign
key relations need exclusive table locks to activate. Do it as a cold patch.

.. warning::

   Don't attempt to create a table without the DBA available. There are still
   edge cases where we cannot do this live, such as a table with foreign key
   constraints to a busy table, which requires locks on the busy table that
   will not be granted quickly enough.

Table renaming
~~~~~~~~~~~~~~

Because code is deployed separately from database updates, we need to maintain a
fully updateable working alias from the old table name to the new one. See
:ref:`rename-database-table` for an example database patch.

Adding columns
~~~~~~~~~~~~~~

If the table is large enough that applying the patch raises performance
concerns, split the work into the following steps. All steps aside from the
first are optional, depending on the desired result.

1. Create the column without indexes and without setting ``NOT NULL`` or a
   default value.
2. Set the default value.
3. Add the index via a hot patch.
4. Run a garbo job (or similar) to fill in the values.
5. Set the column ``NOT NULL``.

.. note::

   We still need to work out how we test that things work both with and without
   the database patch applied.
