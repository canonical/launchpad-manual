.. meta::
   :description: Comprehensive step-by-step guide to create database schema
      patch.

.. _create-a-db-patch:

Create a database patch
=======================

Launchpad's schema is changed through database patches. These live in branches
that go through review and landing, just like code changes.

Schema patches can either be applied while the system has deliberately been brought down
(cold patches) or while the system is up and actively being used (hot patches). Changes such as
updating a table, which will be affected by ongoing activity, **and** adding an index,
which can be done without affecting behavior of the system, must be split into two separate
patches — one cold and one hot.

See :ref:`database-patching` for more information about how cold/hot
patching works.

Schema patches must **not** be combined with changes to the Launchpad
python code — any branch landing on the devel or db-devel must either be a schema patch
or be a code change.
**Test only** code may be included if absolutely necessary.
Exceptions to this rule require approval from the project lead, because
deploying them will require a 1 hour+ complete downtime window.

Making a database patch
-----------------------

You need to run these steps whenever you make a schema change:

1. In your local development Launchpad instance, run ``make schema`` to get a pristine database of sample data.
2. Add a patch number in `the dbpatches
   repository <https://code.launchpad.net/~launchpad/+git/dbpatches>`__.
   If you are in the ``~launchpad`` team please allocate this yourself. Other
   developers can ask any ``~launchpad`` member to allocate a patch number for
   them.
   Commit and push directly to the main branch. No review is needed.
3. Create a SQL file named ``patch-XXXX-YY-Z.sql`` in ``database/schema/``,
   where ``XXXX-YY-Z`` is the patch number allocated in the previous
   step. The schema application code only picks up files matching this
   exact naming pattern. 
   
   Your patch should look like this:

  .. code-block:: SQL

   -- Copyright 2026 Canonical Ltd.  This software is licensed under the
   -- GNU Affero General Public License version 3 (see the file LICENSE).

   SET client_min_messages=ERROR;

   -- put your changes in here.

   INSERT INTO LaunchpadDatabaseRevision VALUES (XXXX, YY, Z);

4. Run your new SQL patch on the development database to ensure that it
   works:

   .. code-block:: bash

       psql launchpad_dev -1 -f your-patch.sql
5. Run ``make schema`` again and check that your patch gets applied. This
   is needed to allow the test suite to see your changes.
6. You may also wish to run ``make newsampledata``. Although it isn't
   critical, this lets you see what changes your patch would make to
   initial setups. This will produce a lot of noise. Feel free to ignore it.
7. Review the sample data changes that occurred using ``git diff
   database/sampledata``. This diff can be hard to review as-is. You
   might want to use a graphical diff viewer like ``kompare`` or
   ``meld``. Make sure that you understand all
   the changes you see.
8. If you have added, removed or renamed a table or column, ensure that your
   patch includes appropriate ``COMMENT`` statements.
9. Run ``make schema`` again to ensure that it works, and that you now
   have a pristine database with the new sample data. If you don't
   want to clean your ``launchpad_dev`` database, then you can use
   ``make -C database/schema test`` instead to update only the test
   databases.
10. Make any necessary changes to ``database/schema/fti.py``,
    ``database/schema/security.cfg``.
11. Run the full test suite to ensure that your new schema doesn't
    accidentally break any existing tests/code.

Propose your patch for deployment

Commit your patch without sample data changes, then push and propose for merging to
``db-devel`` if it's a cold patch or ``master`` if it's a hot patch.

The schema change is approved for landing when you have an 'Approved'
vote from a DB reviewer (unless the reviewer in question explicitly
sets a higher barrier).

In case you're not a member of ``~launchpad``, ask a member of the team to do
these last steps for you:

* QA the patch to confirm it applies cleanly and meets performance requirements. Make sure cold patches do not take more than a few seconds to apply.
* Wait until there are **no** blockers to deploying the patch. One
  common blocker is having code changes made prior to the patch sitting
  in stable and not yet deployed to all affected service instances.
* Request a deployment per the internal `production change
  process <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/launchpad-rollout/launchpad-deployments/production-change-processes/>`__.


Rules for patches
-----------------

* Operations that claim locks on tables should be done using ``CONCURRENTLY``.
* When dropping a table, make sure that you drop or update any dependent triggers, views and foreign keys beforehand.
* Do not migrate data in schema patches unless the data size is
  extraordinarily small (< 100s of rows).
* Similarly, new columns must default NULL unless the data size is
  extraordinarily small (< 100s of rows).
* When changing existing DB functions, start your patch with the
  original version (``SELECT pg_get_functiondef(oid) FROM pg_proc WHERE
  proname IN ('foofunc', 'barfunc') ORDER BY proname;``). This makes it
  much easier to review the diff.

Notes on changing security.cfg
------------------------------

If your changes to ``security.cfg`` are additive in nature like adding new
permissions to an existing role or adding a new role, then you can land them
on ``master`` rather than ``db-devel``.
These changes are deployed during no-downtime rollouts.

Any update that revokes permissions from an existing role (including removing
a role entirely), must be landed on ``db-devel`` and deployed during a
fast-downtime deployment. This is because a full update (including revocation)
requires resetting all permissions, which cannot be done without downtime.

Adding new roles requires manual DB reconfiguration, so you need to
file a ticket to grant access to relevant machines and make sure it is
resolved **before landing the branch** that needs them.

Sample data
-----------

If your branch needs to make changes to the database schema, the
sample data should be updated to match your schema changes.

Never *add* new rows to the sample data.

Sample data is used to provide well-known baseline data for the test
suite, and to populate a developer's Launchpad instance so that
``launchpad.test`` can display interesting stuff. Keep the following
guidelines and recommendations in mind before you make
changes to the test suite sample data, or you may break the tests for
yourself or others.

Sample data is for developer's instances only and is of no use on production systems.

If your tests require new data, create the data in your test's harness instead
of adding new sample data. This often makes the tests themselves more readable.
It also reduces the chance that your changes will break other tests. Add the new
data in your test's ``setUp()`` or in the narrative of your doctest.
The test suite uses the ``launchpad_ftest_template`` database, so
there is no chance that running the test suite will accidentally alter
the sample data.

However, if you interact with the web UI for ``launchpad.dev`` your
changes will end up in the ``launchpad_dev`` database. This database is
used to create the new sample data, so you must run
``make schema`` to start with a pristine database before generating new
sample data. If in fact you do want the effects of your UI interactions
to land in the new sample data, then the general process is to

* run ``make schema``
* interact with ``launchpad.dev``
* run ``make newsampledata``

.. note::
  Be aware that if you generate new sample data, this will probably
  have an effect on tests not related to your changes. If you make
  changes to the sample data, you must run the full test suite
  and ensure that you get no failures.

