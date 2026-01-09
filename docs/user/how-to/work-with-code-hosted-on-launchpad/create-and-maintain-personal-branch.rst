.. _create-and-maintain-personal-branch-in-launchpad:

Create and maintain a personal branch in Launchpad
==================================================

.. include:: /includes/important_not_revised_help.rst

Branches hosted by Launchpad are usually asssociated with a project.

If you'd prefer to upload a branch to Launchpad without it showing up in
any project's branch listings, you can use the ``+git``
pseudo-project. This can be useful if your branch is:

-  for a project not yet in Launchpad
-  not ready to be publicly associated with a project.

``+git`` branches work in a similar way to normal branches: anyone
can create their own branch and they show up in `your own branch
list <https://code.launchpad.net/people/+me>`__.

However, there are some differences:

-  you can't propose a +git branch for merging
-  they don't show up in any project's branch listing
-  you don't earn karma from +git branches.

If you want to collaborate on a +git branch with someone else, you need
to make the branch be owned by a team that both you and the other person
are members of. Better still, when you are ready to collaborate, you
should :ref:`create a
project <registering-your-project>` and move
the ``+git`` branch into the project.

Create a +git branch
---------------------

Adding a ``+git`` branch to Launchpad is the same as creating any other
hosted branch. Instead of using the project name in the branch URL, you
use +git.

For instance:

.. terminal::
    git push git.launchpad.net:~matthew.revell/+git/mybranch

Next steps
----------

If you want to work on a project that uses an external git repository to host 
its main line of development, you can ask Launchpad to 
:ref:`import it into a git branch <import-code-into-launchpad>`.
