.. _linking-bugs-to-dedicated-branches:

Linking bugs to dedicated branches
==================================

.. include:: /includes/important_not_revised_help.rst

If you create a branch to fix a specific bug, and that branch is registered in 
Launchpad, you can link the bug report and the merge proposal for that branch.

Launchpad uses an icon to indicate the link in the branch and bug
listings. The icons are a quick way for anyone to see that you have code
that is intended to fix a particular bug.

For example, take the branch listing for the Beagle project. You can see
grey bug icons beside the name of some branches. Clicking on the bug
icon takes you to the relevant page in the bug tracker.

http://code.beta.launchpad.net/beagle

Similarly, on the bug listing pages, a yellow Bazaar logo appears next
to bugs that are linked to a branch. Clicking on the Bazaar icon takes
you to the relevant branch.

https://bugs.beta.launchpad.net/beagle/+bugs

Each link between a bug and a merge proposal has its own status and whiteboard.
The status indicates the progress of the fix, and you can use the whiteboard 
for more detailed information.

Any Launchpad user can have multiple branches of code for a project, and
teams can have multiple branches too. How do you know which branch to
use when starting new work?

For this, we have major branches in the project, which we call "Series",
and that's what we will :ref:`show you next <series-major-stable-and-development-branches>`.
