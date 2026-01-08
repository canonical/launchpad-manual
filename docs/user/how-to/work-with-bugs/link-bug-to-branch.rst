.. _link-a-bug-reports-to-a-branch:

Link a bug reports to a branch
==============================

.. include:: /includes/important_not_revised_help.rst

If your project uses both Launchpad Bugs and Launchpad Code -- whether
directly hosting Git branches on Launchpad or importing from elsewhere -- you 
can link bug reports directly to the code where someone is working on a fix.

Fix a bug in a dedicated branch
-------------------------------

Let's say you're new to a project. You spot a bug report and you're pretty 
certain you can fix it. You :ref:`pull down your own branch <host-a-git-repository-on-launchpad>` 
of the project's trunk and hack away. Every now and then, you push your branch 
up to Launchpad.

You can tell everyone who's interested in the bug about your work by
linking your branch to the report. Now, anyone looking at the bug report
can click straight through to see your branch.

Create a link using the Launchpad web interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, visit your bug report in Launchpad. Click ``Link to related branch``,
then select the branch.

Create a link from the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also link to bugs by adding appropriate text to your commit message 
instead. For example, your commit message might look like this:

::

   Shorten error message

   The previous 3000-line message was too hard to read.

   LP: #12345

Note that Git bug links will only be recorded once you :ref:`propose a merge <create-and-manage-a-merge-proposal>` 
that includes such commits.

See :ref:`Launchpad's Git hosting documentation <linking-to-bugs>` for more 
details.

Find links to branches
----------------------

In branch listings, and on the branch overview page itself, Launchpad
uses an icon to indicate a link between a bug report and a branch of
code. Similarly, there's a yellow Bazaar icon in bug listings to show
which reports are linked to a branch of code.

Next step
---------

Launchpad helps you to stay on top of the bugs you're interested in,
both by email and Atom feeds. Let's take a look at :ref:`bug
subscriptions <bug-subscription>`.

Read more about :ref:`linking bugs to dedicated branches <linking-bugs-to-dedicated-branches>`.
