Create and maintain a personal branch in Launchpad
==================================================

Branches hosted by Launchpad are usually asssociated with a project.

If you'd prefer to upload a branch to Launchpad without it showing up in
any project's branch listings, you can use the ``+junk``
pseudo-project. This can be useful if your branch is:

-  for a project not yet in Launchpad
-  not ready to be publicly associated with a project.

``+junk`` branches work in a similar way to normal branches: anyone
can create their own branch and they show up in `your own branch
list <https://code.launchpad.net/people/+me>`__.

However, there are some differences:

-  you can't propose a +junk branch for merging
-  they don't show up in any project's branch listing
-  you don't earn karma from +junk branches.

If you want to collaborate on a +junk branch with someone else, you need
to make the branch be owned by a team that both you and the other person
are members of. Better still, when you are ready to collaborate, you
should `create a
project <https://help.launchpad.net/Projects/Registering>`__ and move
the ``+junk`` branch into the project.

Create a +junk branch
---------------------

Adding a ``+junk`` branch to Launchpad is the same as creating any other
hosted branch. Instead of using the project name in the branch URL, you
use +junk.

For instance:

.. terminal::
    bzr push ~matthew.revell/+junk/mybranch

Next steps
----------

If you want to work on a project that uses an external Bazaar, git, CVS
or Subversion branch to host its trunk line of development, you can ask
Launchpad to `import it into a Bazaar branch <Code/Imports>`__.
