Import code into Launchpad
==========================

There's a lot of free software code available in CVS, Subversion (SVN)
and Git repositories, or Bazaar repositories that aren't hosted on
Launchpad. Sometimes you're going to want to have this code available on
Launchpad in Bazaar. Perhaps you use Bazaar for your project and you'd
like to use a Git-based project as a dependency. Perhaps you'd like to
do some work on a CVS project but would prefer to use a more modern
version control system. Maybe you'd like to hack on a project that uses
Subversion, but you don't have commit rights.

If any of this is striking a chord, then you probably want to know about
Launchpad's code import system.

Launchpad provides a free service which imports the trunk of a project
from Subversion, CVS, or Git to `Bazaar <http://bazaar-vcs.org>`__, or
from Git to Git, and then keeps that import up to date. This allows you
to make your own branches from the project trunk, and keep them up to
date by merging from trunk over time as you develop your feature.

Requesting an import
--------------------

To request an import, please:

- Make sure the project is `registered in
  Launchpad <https://launchpad.net/products>`__, or register it yourself.
- Then visit the `page for requesting a code
  import <https://code.launchpad.net/+code-imports/+new>`__ and fill
  out the details.

This will:

* Create an empty branch (for Bazaar) or repository (for Git) to contain the imported code.
* Subscribe you to it so that you will be notified both when the initial import completes
  and subsequent updates import new revisions.
* Notify the import operators who will check that the import location exists and approve the import.

.. note::
    If the import source is a Subversion repository, then it should
    be a "trunk" directory. If we can't find trunk in the repository, we
    won't activate the import.

Depending on the nature of the import source, there are different
restrictions on what branches can be tracked:

-  **CVS**: The importer can only track the HEAD branch of the project.
-  **Subversion**: All branches can usually be imported.
-  **Git**: Repositories with submodules or signed commits in their
   history can currently only be imported to Git, not to Bazaar.

Making your request
~~~~~~~~~~~~~~~~~~~

So, a good import is part voodoo, part science, part luck. An import
will not lose data - we can verify that the result of a checkout of the
Bazaar branch is identical to a checkout of the CVS branch. But getting
it to that point may well require inspection and custom work.

For this reason, we don't have an automated process for the import.
Instead, you `request
one <https://code.launchpad.net/+code-imports/+new>`__ and we put it in
a queue. Sometimes it takes just an hour or two, sometimes it can take
days to get a good import together. In very few cases, the old
repositories are so wedged that we can't get all the history exactly
right. It's best just to get started and see how it goes. We are
constantly improving the voodoo.

The initial import can take a long time—up to several days, depending on
the number of revisions that need to be converted. Once the import is
established it will be updated from the CVS or Subversion branch with
every 6-12 hours, although an import can be requested at any time by
clicking the "Import Now" button on the import page.

More information
----------------

Informal support happens in many different places in the free software
world. Launchpad aims to bring bug tracker-like qualities to giving and
asking for help. Let's look at `Launchpad Answers <Answers>`__.