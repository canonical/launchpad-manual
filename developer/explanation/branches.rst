About Launchpad branches
========================

.. include:: ../includes/important_not_revised.rst

Where's trunk?
--------------

Launchpad has four master branches (this is unusual; most projects only
have one). They are:

1. `master <https://code.launchpad.net/~launchpad/launchpad/+git/launchpad/+ref/master>`__
   Where most development takes place (except anything that involves
   changing the database schema; see below).
2. `db-devel <https://code.launchpad.net/~launchpad/launchpad/+git/launchpad/+ref/db-devel>`__
   Changes that modify the database schema get merged here first.
3. `stable <https://code.launchpad.net/~launchpad/launchpad/+git/launchpad/+ref/stable>`__
   This is fed by regular merges from the **master** branch, and is
   deployed to
   `qastaging.launchpad.net <https://qastaging.launchpad.net/>`__
   frequently.
4. `db-stable <https://code.launchpad.net/~launchpad/launchpad/+git/launchpad/+ref/db-stable>`__
   This is fed by regular merges from the **db-devel** branch. It is
   deployed to `staging.launchpad.net <https://staging.launchpad.net>`__
   frequently, and deployed to
   `launchpad.net <https://launchpad.net/>`__ on each DB schema
   deployment. After deployment, **db-stable** is merged back into
   **master**, completing the cycle.

In summary: **db-stable** is the post-test-run counterpart of
**db-devel**, and **stable** is the post-test-run counterpart of
**master**, where *"post-test-run"* means that once code hits foo-devel
it is only cleared into foo-stable if the buildbot test runner succeeds.

If you want to know how all of this works behind the scenes, read
`Trunk/Glue <Trunk/Glue>`__ (after reading the rest of this page).

Look at the Pretty Pictures
---------------------------

Diagrams might be the best way to understand this. (If they don't work,
there's text afterwards, don't worry.)

.. XXX: add missing images

Below, we break the process down a bit with a different diagramming
approach. Here's what happens when you submit to **master**:

Where are the expected potential problems in the process? Glad you
asked!

It is also possible to submit directly to the **db-devel** branch.

Let's Try That in Words
-----------------------

Database changes can be destabilising to other work, so we isolate them
out into a separate branch (**db-devel**). Then there are two arenas for
stabilising changes for deployment: **stable** (which ends up on
`qastaging <https://qastaging.launchpad.net>`__ and is fed from the
**master** branch), and **db-stable** (which ends up on
`staging <https://staging.launchpad.net>`__ and is fed from the
**db-devel** branch).

(Note that the actual images here date from the Bazaar world, and so
talk about "devel" rather than "master". You can regard these two names
as interchangeable. Feel free to update the images if you have time.)

In summary:

-  Developers submit to **master** and **db-devel**.

-  Buildbot tests the tip of **db-devel**, in addition to **master**. If
   a **db-devel** change passes, it is pushed automatically to
   **db-stable**.

-  When changes are approved by buildbot to go from **master** to
   **stable**, a script also generates a PQM request to merge **stable**
   with **db-devel**, sent as if it came from the Launchpad list. The
   Launchpad list will be informed of merge failures, and Launchpad
   developers will collectively be responsible for correcting them.
   (***TODO: is this some internal list?***)

-  Staging runs **db-stable**; qastaging runs **stable**. We will deploy
   production DB schema changes from **db-stable**. (After a deployment,
   **db-stable** is manually pushed to **devel** and **stable**.)

Problems that can occur
~~~~~~~~~~~~~~~~~~~~~~~

-  **The merge from stable to db-devel fails.** That's a real risk
    but we expect it to occur infrequently. When it does occur, the
    Launchpad list (***TODO: which one?***) will be emailed, and it is
    the collective responsibility of everyone to fix the problem, by
    manually submitting a branch to **db-devel** that includes the
    branch that failed to merge plus any necessary adjustments.

Where to Send Merge Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Merge requests that do any of the following should be targeted at the
**db-devel** branch:

-  adds a cold database patch (see :doc:`../how-to/database-schema-changes-process`)
-  depends on database schema change only in **db-devel** /
   **db-stable**

All other developer merge requests for the launchpad tree should be
targeted at the **master** branch.

The current \`buildbot-poller.py\` script on the PQM box monitors
buildbot to discover what revisions have passed the tests. When a new
revision is "blessed" by buildbot, the script copies it over to
**stable**. The poller script merges the blessed revision into the
**db-devel** branch. It is also responsible for checking a new buildbot
build testing **db-devel**. The poller will copy revisions of
**db-devel** that buildbot blesses to **db-stable**.

Staging releases should run code from **db-stable**. qastaging and
production should continue to run code from **stable**.

When a DB schema deployment is made, the **db-stable** code should be
merged into **master**. This is the responsibility of the person who
organised the deployment.

Problems with the automated merge requests are sent to the Launchpad
list (***TODO: which list?***).

When the merge of **stable** -> **db-devel** does not work
automatically, it should be done manually and submitted. The tests do
not need to be run (rationale: the bots don't run the tests when they do
it automatically, and the failure messages can clutter up the ML really
fast.)

How do I submit to db-devel?
----------------------------

See also WorkingWithDbDevel.

::

   cd ~/canonical/launchpad/launchpad
   git checkout -b mydbbranch db-devel
   make build
   make schema

...hack until ready to submit...

::

   git push -u myusername mydbbranch

Now create and land a merge proposal.

FAQ
---

Can I land a test fix before buildbot has finished a test run that has failed or will fail?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can, and please do if appropriate, because this will mean that
other developers will not encounter a broken tree at all.

What happens if the automatic merge from stable to db-devel fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The (internal! change?) launchpad list gets an email. This is described
on the /Trunk page.

A build failed for some reason other than a test failure. What do I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Force a build at https://lpbuildbot.canonical.com/force.
