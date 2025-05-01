Link code to bug reports and blueprints
=======================================

Launchpad is much like a fancy china dinner service: you can get a great
deal of use and contentment from just one or two pieces. However, the
really exciting - and sometimes unexpected, in a good way - things start
to happen when you've got the whole lot.

If you're working on a project that uses Launchpad Code and Launchpad
Bugs, for example, you can link a branch of code to the bug report it
fixes. Similarly, you can offer more than just status updates to fans of
that fantastic new feature you're working on - and tracking as a
`blueprint <Blueprint>`__ - by linking the blueprint to a branch of your
code.

Bazaar also gets in on the act, as we'll see in a moment or two.

Fixing bugs in dedicated branches
---------------------------------

Let's say you're new to a project. You spot a bug report and you're
pretty certain you can fix it. You `pull down your own
branch <Code/FindingAndDownloading>`__ of the project's trunk and hack
away. Every now and then, you `push your branch up to
Launchpad <Code/UploadingABranch>`__.

You can tell everyone who's interested in the bug about your work by
linking your branch to the report. Now, anyone looking at the bug report
can click straight through to see your branch.

Now imagine the project were using a more traditional version control
system and they were tracking their bugs in a standalone tracker. As a
newcomer, you could paste your patches as bug comments, while hacking
away on your own machine. With Launchpad and Bazaar you get full version
control, without affecting the official project branch itself, and
anyone else can take part by downloading and creating their own branch
of your work.

Create a link
-------------

Using the Launchpad web interface:

**Step 1**: Visit your branch page in Launchpad.

**Step 2**: Click ``Link to a bug report``.

**Step 3**: Select the bug report and you're done!

Create a link using Bazaar
~~~~~~~~~~~~~~~~~~~~~~~~~~

Just as you can register and push your branch to Launchpad directly from
Bazaar, you can also create a bug-branch link.

::

   $ bzr commit --fixes lp:12345

Find links to branches
----------------------

In branch listings, and on the branch overview page itself, Launchpad
uses an icon to indicate a link between a bug report and a branch of
code. Similarly, there's a yellow Bazaar icon in bug listings to show
which reports are linked to a branch of code.

Let's take a look at an example: take the `branch listing for the
Drizzle <https://code.launchpad.net/drizzle>`__ project. As you can see,
some branches have grey bug icons beside their name. Click on one of
those the bug icons and Launchpad will take you to the bug report page.

From the other side of this relationship - i.e. Drizzle's bug listing
pages - you'll see the yellow Bazaar logo next to bug reports that are
linked to a branch. Clicking on the Bazaar icon takes you to the
relevant branch.

https://code.launchpad.net/drizzle

Each link between a bug and branch has its own status and whiteboard.
The status indicates the progress of the fix and you can use the
whiteboard for more detailed information.

Next steps
----------

Most branches in Launchpad are associated with a project. However, you
can also `host personal branches <Code/PersonalBranches>`__ using
Launchpad.
