Database schema changes process
===============================

.. include:: ../../includes/important_not_revised.rst

Step-by-step procedure
----------------------

1. Prepare a branch containing just `your database
   patch <#Making_a_database_patch>`__ for review.

   -  The patch must either be a hot patch (function / trigger / index)
      or a cold patch (model change / model change + function/trigger).
      If you need both hot and cold changes, you require multiple
      branches.

2. Submit a merge proposal for your branch, requesting a **db** review
   from launchpad-reviewers. For hot patches the target branch is
   ``master``, but for cold patches it should be ``db-devel``.

3. Iterate on the branch as needed. The DB review process can sometimes
   require significant changes to achieve acceptable performance on
   either the patch application or queries / updates to the resulting
   schema.


4. The schema change is approved for landing when you have an 'Approved'
   vote from a DB reviewer (unless the reviewer in question explicitly
   sets a higher barrier).

5. Wait until there are **no** blockers to deploying the patch. One
   common blocker is having code changes made prior to the patch sitting
   in stable and not yet deployed to all affected service instances.


6. Land the branch on ``master`` (for hot patches) or ``db-devel`` (for
   cold patches) by setting the merge proposal to Approved as usual,
   unless someone has stated it is being landed it on your behalf. (Only
   Canonical staff can do the landing step).

7. [Cold patches] Wait until the branch reaches staging. Use the
   `db-stable deployment
   report <https://deployable.ols.canonical.com/project/launchpad-db>`__
   to check this.

8. [Cold patches] After the branch reaches staging check the duration
   that the patch took to apply by rsyncing
   ``pamola.internal::staging-logs/dbupgrade.log`` from carob. If it
   took more than 15 seconds, mark the revision bad and revert it.

9. [Cold patches] QA the patch as usual, check things still work on
   staging.

10. [Hot patches] Ask a member of IS to manually apply the patch to
    qastaging, and check that things still work. *Note: This is a
    temporary exception from normal deployment rules, to be reviewed when
    buildbot is faster.*

11. Request a deployment per the internal `production change
    process <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/launchpad-rollout/launchpad-deployments/production-change-processes/>`__.

12. Now get your python code that builds on the schema landed and
    deployed as usual.

Background
----------

We change the schema through database patches. These live in branches
that go through review and landing, just like code changes.

Schema patches are either applied while the system has no activity
('cold patches') or while the system is under load ('hot patches'). Some
things, like changing a table **and** adding an index, will need to be
split into two separate patches - one hot and one cold.

Schema patches must **not** be combined with changes to the Launchpad
python code - any branch landing on devel or db-devel must be one or the
other. Test \*only\* code may be included if absolutely necessary.
Exceptions to this rule require approval from the project lead, because
deploying them will require a 1 hour plus complete downtime window.

Cold schema patches always land on ``db-devel``. After they are made live
they will be promoted to ``master`` as part of the go-live process.

Hot Patches
~~~~~~~~~~~

:doc:`../explanation/live-patching` explains how
hot-patching works and what sorts of things we can hot-patch. It's the
authority — we may be able to hot-patch more as our tooling improves.

Cold Patches
~~~~~~~~~~~~

Anything that is not a hot patch is a cold patch and can only be applied
while the appservers and so on are disconnected from the database
cluster.

For qa on a cold patch, check the application time from the staging log

-  it must be < 15 seconds [even with cold disk cache], or we will
   exceed our downtime window. To exceed that window requires sign-off by
   the technical architect or project lead.

If some parts of a change can be applied as a hot patch, it is a good
idea to do it that way, in order to keep application time minimal. For
example, applying an index to thousands of rows may be okay, but tens of
thousands of rows is typically too slow to do in a cold patch.

Deploying patches
-----------------

After successful QA on a patch, request a deploy via the internal
process `production change
process <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/launchpad-rollout/launchpad-deployments/production-change-processes/>`__..

Reviews
-------

All schema changes should have reviews of type "db" requested from the
regular review team (``launchpad-reviewers``). An approve vote from any DB
reviewer is sufficient to land the patch.

As schema changes have no appserver code changes landed at the same
time, no other reviews are needed (unless an exception to the no-mixing
rule has been granted, in which case a normal review is also needed).

Changes to the permissions in ``database/schema/security.cfg`` or the
comments in ``database/schema/comments.sql`` are not schema patches and
do not require db review when done on their own. If they are included in
a schema patch then the db reviewer will review them.

Patch ids
---------

The schema application code needs a unique id for each patch. This is
allocated by editing a shared document stored in the `dbpatches
repository <https://code.launchpad.net/~launchpad/+git/dbpatches>`__. If
you are in ``~launchpad`` please allocate this yourself. Other
developers can ask any ~launchpad member to allocate a patch number for
them.

As we no longer synchronise appserver deployments with schema
deployments, **no-one should use a -0 patch.**

Instructions for choosing a patch number are in the docs in the
dbpatches repository.

Making a database patch
-----------------------

You need to run these steps whenever you make a schema change,
regardless of whether you intend to delete sample data or not. For
example, if you are adding a new column to the ``Person`` table, these
steps ensure that the sample data will include this new column.

1. Run ``make schema`` to get a pristine database of sample data.

2. Claim a patch number in `the dbpatches
   repository <https://code.launchpad.net/~launchpad/+git/dbpatches>`__
   (be sure to commit and push back to the ``main`` branch).

# Create a SQL file in ``database/schema/`` containing the changes you
want. It should look like this:

::

   -- Copyright 2011 Canonical Ltd.  This software is licensed under the
   -- GNU Affero General Public License version 3 (see the file LICENSE).

   SET client_min_messages=ERROR;

   -- put your changes in here.

   INSERT INTO LaunchpadDatabaseRevision VALUES (XXXX, YY, Z);

3. Run your new SQL patch on the development database to ensure that it
   works. Do this by running ``psql launchpad_dev -1 -f your-patch.sql``

4. Run ``psql launchpad_ftest_playground -f your-patch.sql`` as the
   ftest playground db is used to regenerate sampledata snapshots in the
   following step. (Also be sure you ran ``psql launchpad_dev -f
   your-patch.sql`` in the previous step-- this updates the dev
   database's sampledata. Note that this is *not* sufficient to let the
   test suite see your changes: for that, you'll need to update
   ``launchpad_ftest_template``, though it's simplest to run ``make
   schema`` or ``make -C database/schema test`` as described below.)

5. You may wish to run ``make newsampledata``, although it isn't
   critical; this will let you see what changes your patch would make to
   initial setups.

   - This will produce a lot of noise. Feel free to ignore it.

6. Review the sample data changes that occurred using ``git diff
   database/sampledata``. This diff can be hard to review as-is. You
   might want to use a graphical diff viewer like ``kompare`` or
   ``meld`` which will make it easier. Make sure that you understand all
   the changes you see.

7. Move your pending SQL file into ``database/schema/`` with a name like
   ``patch-xx-yy-zz.sql`` (where *xx* matches the existing patches), and
   ending with the line ``INSERT INTO LaunchpadDatabaseRevision VALUES
   (xx, yy, zz);``.

8. If you have removed or renamed a table or column, ensure that your
   patch includes appropriate ``COMMENT`` statements.

9. **Run** ``make schema`` **again to ensure that it works, and that you now
   have a pristine database with the new sample data.** If you don't
   want to blow away your ``launchpad_dev`` database, then you can use
   ``make -C database/schema test`` instead to update only the test
   databases.

10. New tables and columns need corresponding ``COMMENT`` statements in
    your patch.

11. Make any necessary changes to ``database/schema/fti.py``,
    ``database/schema/security.cfg``.

12. **Run the full test suite to ensure that your new schema doesn't
    break any existing tests/code by side effect.**

13. Commit without sample data changes, push and propose for merging to
    ``db-devel``

Rules for patches
~~~~~~~~~~~~~~~~~

1. To drop a table, use ``DROP TABLE`` as usual. Make sure that you drop or
   update any dependent triggers, views and foreign keys before.

2. Do not migrate data in schema patches unless the data size is
   extraordinarily small (< 100's of rows).

3. Similarly, new columns must default NULL unless the data size is
   extraordinarily small (< 100's of rows).

4. When changing existing DB functions, start your patch with the
   original version (``SELECT pg_get_functiondef(oid) FROM pg_proc WHERE
   proname IN ('foofunc', 'barfunc') ORDER BY proname;``). This makes it
   much easier to review the diff.

Sample data
~~~~~~~~~~~

Let's say your branch needs to make changes to the database schema. You
need to follow the steps on this page to ensure that the sample data is
updated to match your schema changes.

We have deprecated sample data. That means that you should never *add*
new rows to the sample data.

In fact, there are now two sets of sampledata that need to be updated.

We use sample data to provide well-known baseline data for the test
suite, and to populate a developer's Launchpad instance so that
``launchpad.dev`` can display interesting stuff. There are some
guidelines and recommendations you should be aware of before you make
changes to the test suite sample data, or you may break the tests for
yourself or others.

Please note that sample data is for developer's instances only. It would
make no sense to use the sample data on production systems!

If your tests require new data, you should create the data in your
test's harness instead of adding new sample data. This will often make
the tests themselves more readable because you're not relying on magical
values in the sample database. Doing it this way also reduces the chance
that your changes will break other tests by side-effect. Add the new
data in your test's ``setUp()`` or in the narrative of your doctest.
Because the test suite uses the ``launchpad_ftest_template`` database,
there is no chance that running the test suite will accidentally alter
the sample data.

However, if you interact with the web U/I for ``launchpad.dev`` your
changes will end up in the ``launchpad_dev`` database. This database is
used to create the new sample data, so it is imperative that you run
``make schema`` to start with a pristine database before generating new
sample data. If in fact you do want the effects of your u/i interactions
to land in the new sample data, then the general process is to

-  run ``make schema``
-  interact with ``launchpad.dev``
-  follow the ``make newsampledata`` steps above.

**Be aware though that your generation of new sample data will probably
have an effect on tests not related to your changes!** For example, if
you generate new karma events, you will break the ``karma_sample_data``
tests because they expect all karma events to be dated prior to the year
2002. If you make changes to the sample data, you **must** run the full
test suite and ensure that you get no failures, otherwise there is a
very high likelihood that you will break the trunk.

Resolving schema conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^

Resolving conflicts in ``current.sql`` manually is usually more trouble
than it's worth. Instead, first resolve any conflicts in
``comments.sql``, then:

::

   cd database/schema/
   mv {patch-in-question}-0.sql comments.sql pending/
   cp {parent branch, e.g. rocketfuel}/database/schema/comments.sql ./
   cp ../sampledata/current.sql.OTHER ../sampledata/current.sql
   make
   psql launchpad_dev -f pending/patch-xx-99-0.sql
   make newsampledata
   mv pending/{patch-in-question}-0.sql pending/comments.sql ./
   make   # Just to make sure everything works
   cd ../..
   bzr resolve database/sampledata/current.sql

Notes on Changing security.cfg
------------------------------

It is possible to land changes to security.cfg on ``master`` rather than
``db-devel``. These changes are deployed during no-downtime rollouts.

Note that adding new users requires manual DB reconfiguration, so you
need to file an RT ticket to grant access to relevant machines and make
sure it is resolved **before landing the branch** that needs them.
