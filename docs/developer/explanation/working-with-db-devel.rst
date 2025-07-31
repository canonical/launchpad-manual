Working with db-devel
=====================

As the standard rocketfuel and ec2test scripts work on devel, some care
must be taken when developing against db-devel. This is a guide for all
who have only used rocketfuel-scripts so far.

You also should be familiar with the `process for schema
changes <https://dev.launchpad.net/PolicyAndProcess/DatabaseSchemaChangesProcess>`__.

Alternative trunk
-----------------

Check out the \`db-devel\` branch in your :doc:`existing git
clone <../how-to/running>`:

::

   git checkout db-devel
   git pull

Now you can use this to create new branches of db-devel:

::

   git checkout -b my-db-devel-branch db-devel

You can update db-devel by pulling in changes.

::

   git checkout db-devel
   git pull

You can merge changes from db-devel into your branch.

::

   git checkout my-db-devel-branch
   git merge db-devel
   git commit -m "Merge db-devel"

Or rebase it if you prefer:

::

   git checkout my-db-devel-branch
   git rebase db-devel

.. note::

    Should we make it a habit to prefix these branches' names
    with "db-" so we never forget? —jtv''

Pushing to Launchpad
--------------------

You can push to Launchpad as usual. If you haven't set up a contributor
remote already, replacing "myusername" with your Launchpad username:

::

   git remote add myusername lp:~myusername/launchpad

Then, to push a branch:

::

   git push -u myusername my-db-devel-branch

Creating a merge proposal
-------------------------

It is very important to get the merge target right when creating a merge
proposal, otherwise your reviewer will see a much larger patch than what
you thought you were submitting.

When creating a merge proposal through the UI make sure to set db-devel
as the target branch path.

.. note:: 

    It is a good idea to mention that you want to merge into
    db-devel in the cover letter because it is not *very* conspicuous to the
    reviewer otherwise.
