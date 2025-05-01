Link a bug reports to a branch
==============================

If your project uses both Launchpad Bugs and Launchpad Code -- whether
directly hosting Bazaar or Git branches on Launchpad or importing from
elsewhere -- you can link bug reports directly to the code where someone
is working on a fix.

Fix a bug in a dedicated branch
-------------------------------

Let's say you're new to a project. You spot a bug report and you're
pretty certain you can fix it. You `pull down your own
branch <Code/FindingAndDownloading>`__ of the project's trunk and hack
away. Every now and then, you `push your branch up to
Launchpad <Code/UploadingABranch>`__.

You can tell everyone who's interested in the bug about your work by
linking your branch to the report. Now, anyone looking at the bug report
can click straight through to see your branch.

Create a link to the branch
---------------------------

Using the Launchpad web interface:

First, visit your bug report in Launchpad. Click on ``Link to related branch``,
then select the branch.

Create a link using Bazaar
~~~~~~~~~~~~~~~~~~~~~~~~~~

Just as you can register and push a branch of code to Launchpad directly
from Bazaar, you can also create a bug-branch link.

::

   $ bzr commit --fixes lp:12345

Create a link using Git
~~~~~~~~~~~~~~~~~~~~~~~

If you manage your code using Git instead, then you can link to bugs by
adding appropriate text to your commit message instead. For example,
your commit message might look like this:

::

   Shorten error message

   The previous 3000-line message was too hard to read.

   LP: #12345

Note that Git bug links will only be recorded once you `propose a
merge <Code/Review>`__ that includes such commits.

See `Launchpad's Git hosting documentation <Code/Git#Linking_to_bugs>`__
for more details.

Find links to branches
----------------------

In branch listings, and on the branch overview page itself, Launchpad
uses an icon to indicate a link between a bug report and a branch of
code. Similarly, there's a yellow Bazaar icon in bug listings to show
which reports are linked to a branch of code.

Next step
---------

Launchpad helps you to stay on top of the bugs you're interested in,
both by email and Atom feeds. Let's take a look at `bug
subscriptions <Bugs/Subscriptions>`__.

Read more about :doc:`linking bugs to dedicated branches <../../explanation/feature-highlights/bug-branch-linking>`.