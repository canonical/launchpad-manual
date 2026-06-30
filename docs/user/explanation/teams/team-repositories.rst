.. meta::
   :description: Explanation of team repositories in Launchpad.

.. _team-repositories:

Team repositories
=================

In Launchpad, a team can own a Git repository just like an individual user.
When a team owns a repository, every member of that team can push to it. When
you push a branch to the repository, anyone on the team can commit to it.

A team-owned repository lives at a path based on the owning team, for example 
``~test-team/gnuhello`` for the Test team's repository for the ``gnuhello`` project.
The full path would be ``~test-team/gnuhello/+git/gnuhello``.

Access to team repositories is governed by membership. By default, any member
of the owning team can push to any branch in the repository. When someone is
removed from the team they won't be able to push to these branches anymore.
Repository owners can optionally define access rules for specific branch
patterns if finer-grained control is needed.

Working on a team repository
----------------------------

It's possible for multiple people in a team to push their commits to the same
branch in a team-owned repository. Git will make sure that each push doesn't
overwrite the work that is already there. If there is a conflicting commit
already pushed by someone else, your push is rejected until you integrate
their commits by fetching and merging or rebasing, before pushing again.

Unlike with lightweight checkouts in the now deprecated Bazaar, every team
member who clones a git repository gets a complete local copy of its branches
and full commit history. You can commit to existing branches or create new ones,
and inspect the entire history offline. To share your work with the team, push
it to a branch of the team repository.

A typical workflow looks like this:

#. Clone the shared repository so you have a full local copy.
#. Switch to a branch (or create a new one) and commit changes to it.
#. Fetch and integrate any new commits your teammates have pushed.
#. Push your commits to the upstream branch in the team repository.

Setting up a team repository
----------------------------

There are two ways to create a team-owned repository. You can create a new one
under the team, or hand over ownership of an existing personal repository to a
team.

Create a new team repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a member of a team, you can push directly into the team's namespace
and Launchpad will create the repository under the team for you. For example,
to create a repository for the ``gnuhello`` project owned by ``test-team``:

::

   git push git+ssh://<me>@git.launchpad.net/~test-team/gnuhello main

Launchpad creates the repository at ``~test-team/gnuhello`` with the team as
its owner. Every member of ``test-team`` can immediately push to it.

Convert an existing repository to a team repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have a personal repository (for example, ``~me/gnuhello``) and
want the whole team to be able to push to it, change its owner to the team.

Go to the repository's page in Launchpad, edit its details, and set the owner
to the team. Once you save the change, the repository moves into the team's
namespace (``~test-team/gnuhello``).

Adding a team branch
~~~~~~~~~~~~~~~~~~~~~~
If you are a member of a team, you can add a new branch to a shared repository
by creating it locally and pushing to the team repository. For example, if you
are a member of ``test-team`` which owns the ``gnuhello`` repository, you can
add a shared branch called ``newfeature`` by creating it locally, committing
changes, and pushing them. Launchpad will automatically create the new branch:

::
   
   git clone git+ssh://<me>@git.launchpad.net/~test-team/gnuhello
   cd gnuhello
   git checkout -b newfeature
   # create and commit changes
   git push <remote-name> newfeature

Other members of ``test team`` will be able to to fetch the new branch and
base their own work on it. They will also be able to push new commits to the
same branch. To start working on it, a team member clones the repository and
switches to the ``newfeature`` branch:

::

   git clone git+ssh://<me>@git.launchpad.net/~test-team/gnuhello
   cd gnuhello
   git switch newfeature

Administering team repositories
-------------------------------

Launchpad makes it easy to control who can commit to a team branch because they
are simply the members of the team that owns the repository. Granting or
revoking commit access is just a matter of adding or removing a team member.

This means that it is trivial to create a team to collaborate on a
feature. Create a new Launchpad team with the people that you want to be able
to commit to the feature's mainline branch. Push the initial branch to the
team space, and tell everyone to commit there!

Team branches are a very popular way for the Ubuntu teams to collaborate. For
example, you can set up teams around a single package or set of packages and
work on shared branches that contain the latest version of the relevant code.

A good example is the Ubuntu Core Development Team. It has branches for many
projects that are shared and to which any team member can commit: https://code.launchpad.net/~ubuntu-core-dev

Using forks alongside the shared repository
-------------------------------------------

Team members don't have to commit directly to the shared main branch. A common
approach is to do your work on a separate fork and only integrate it into the
shared branch once it's ready.

In the above example, you can create your own feature branch on a fork and
commit to it freely. You can push that branch to a repository in your own
personal space in Launchpad (for example, ``~me/gnuhello``) rather than the
team-owned repository. This gives you a backup and a place to share work in
progress without affecting the team's mainline.

When you are ready to contribute your work to the shared team branch, you
can integrate it yourself by making sure your copy of the shared branch is
up to date, merging the branch with your changes into it, and pushing the
result back to the team space.

Alternatively you can open a *merge proposal* asking for your branch to be
merged into the shared branch. This is Launchpad's equivalent of a pull request.
It lets teammates review the changes and approve them before they land in the
shared branch. This is the recommended path for non-trivial changes.
See :ref:`create-and-manage-a-merge-proposal` for details.

Next steps
----------

One of the most useful things you can do is to link your branches to a
description of the work they implement.

For example, if your branch fixes a bug, link the branch to the bug
report! And if it's a new feature, track that feature in Launchpad (we
call it a Blueprint) and link the branch to that.

That's the :ref:`next stop <linking-bugs-to-dedicated-branches>` in our
review of Launchpad.
