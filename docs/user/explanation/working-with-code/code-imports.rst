.. _code-imports:

Code imports
============

.. include:: /includes/important_not_revised_help.rst

There's a lot of free software code available in Git repositories that aren't 
hosted on Launchpad. Sometimes you're going to want to have this code available
on Launchpad. Perhaps you want to have closer integration between bug tracking 
and your source code. Or perhaps you want to make use of Launchpad's build 
recipe features to automatically build on multiple processor architectures when
you push new changes. 

If this is striking a chord, then you probably want to know about Launchpad's 
code import system.

Launchpad provides a free service which imports the trunk of a project from Git
repositories to Git, and then keeps that import up to date. This allows you to 
make your own branches from the project trunk, and keep them up to date by 
merging from trunk over time as you develop your feature.

Trunk imports
-------------

Launchpad supports the import of code from a remote repository. A good example 
is the `snapd` project. Launchpad imports snapd's trunk as its `"trunk" series <https://launchpad.net/snapd/trunk>`_ 
in Launchpad.

As you can see, there's a Git branch of snapd's code. Launchpad updates that 
branch regularly by importing the latest from snapd's trunk GitHub repository. 
It works just like any other branch in Launchpad:
you can see the latest commits and you can create your own branch of it and 
then upload it back to Launchpad.

Requesting an import
--------------------

To request an import, please:

- Make sure the project is `registered in Launchpad <https://launchpad.net/products>`_, or register it yourself.
- Then visit the `page for requesting a code import <https://code.launchpad.net/+code-imports/+new>`_ and fill out the details.

This will:

* Create an empty repository (for Git) to contain the imported code.
* Subscribe you to it so that you will be notified both when the initial import 
  completes and subsequent updates import new revisions.
* Notify the import operators who will check that the import location exists 
  and approve the import.

Importing to a Git repository allows you to import repositories with submodules
and signed commits.

Import precision
~~~~~~~~~~~~~~~~

The initial import process is not an exact science, but Git mostly records 
enough information for a deterministic import. This wasn't always the case with
imports from other VCS repositories that were previously supported on Launchpad
such as CVS and SVN.

In most cases, where the CVS and SVN repositories had not been manually
edited or altered, it was possible to infer the information that was required
for the import to proceed smoothly. Git, however, keeps track of renames and 
every commit is treated as an `atomic commit <https://www.geeksforgeeks.org/computer-networks/atomic-commit-protocol-in-distributed-system/>`_

Making your request
~~~~~~~~~~~~~~~~~~~

So, a good import is part voodoo, part science, part luck. An import
will not lose data - we can verify that the result of a checkout of the
Git branch is identical to a checkout of the CVS branch. But getting
it to that point may well require inspection and custom work.

For this reason, we don't have an automated process for the import.
Instead, you `request one <https://code.launchpad.net/+code-imports/+new>`_ 
and we put it in a queue. Sometimes it takes just an hour or two, sometimes it 
can take days to get a good import together. In very few cases, the old
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
asking for help. Let's look at :ref:`Launchpad Answers <launchpad-answer-tracker>`.
