Team branches
=============

The combination of Bazaar branch hosting and teams gives you a very
powerful capability to collaborate on code. Essentially, you can push a
branch into a shared space, and anyone on that team can then commit to
the branch.

This means that you can use Bazaar in the same way that you would use
something like SVN, i.e. centrally hosting a branch that many people
commit to.

Bazaar checkouts
----------------

It is possible for multiple people in a team each to ``bzr push`` their branches to the same location in the team space. For example,
``~team/gnuhello/newfeature``.

Bazaar will make sure that each push doesn't overwrite the work that is
already there. Instead, it must extend that work. However, this is not
usually the most optimal arrangement because each "push" can change the
history of the branch in a dramatic way.

To get a more SVN-like experience, we usually recommend that people use
Bazaar ``checkouts`` of a team branch. A checkout is essentially JUST
the working code tree, without all the branch history, because the
branch history stays on the central server.

When using Bazaar in this fashion it behaves very similarly to SVN. You
cannot commit locally, because the knowledge of your branch history is
on the remote server. But it does mean that you use less space locally,
because you don't need to store all of that history locally too.

Setting up a team branch
------------------------

To create a team branch, simply push a branch into a team space. For
example, if you are still in the ``gnuhello`` branch you created during the earlier example, and you are a member of
the ``test-team`` team, then you could create a shared branch of GNU Hello called
"newfeature" using the following command:

::

   % bzr push bzr+ssh://<me>@bazaar.launchpad.net/~test-team/gnuhello/newfeature
   Created new branch.

Now, it is possible for anybody else to branch from that branch. It is
also possible for anyone in the test-team to push an updated version of
that branch to the same location. But the preferred approach, in
general, is to encourage other team members to use a checkout of the
branch:

::

   % bzr checkout bzr+ssh://<me>@bazaar.launchpad.net/~test-team/gnuhello/newfeature

Now, whenever they commit, Bazaar will first make sure they are up to
date. If not, they can get up to date with ``bzr update`` and then commit.

Launchpad makes it extremely easy to administer the set of people who
can commit to a branch like this, because they are simply the members of
the team.

This means that it is trivial to create a team to collaborate on a
feature. Create a new Launchpad team, with the people that you want to
be able to commit to the feature's mainline branch. Push the initial
branch to that team space. Then, tell everyone to commit there!

Team branches are a very popular way for the Ubuntu teams to
collaborate. For example, you can set up teams around a single package
or set of packages, and work on shared branches that contain the latest
version of the relevant code.

The best example is the Ubuntu Core Development Team. It has branches
for many projects that are shared and to which any team member can
commit:

    https://code.launchpad.net/~ubuntu-core-dev

Here's a snippet from that page showing some of their branches:

Notice how this is being used to keep track of packages that the team
maintains both in Debian and Ubuntu. Shared branches can be used for
cross-project collaboration in a very efficient way, with branches for
specific projects and shared branches for work that is common to both of
them.

Combining branches and checkouts
--------------------------------

It is of course possible to get the best of both worlds, by combining
branches and checkouts.

In the above example, a member of the team might have a checkout of the
mainline branch to which they can commit, but then separately make their
own branch locally which allows them to commit locally.

They would develop on their own local branch, perhaps pushing that up to
the server in their own space rather than the team space. This gives
them full revision control in their own branch. When they are ready to
commit their work to the shared team mainline branch for the feature,
they simply make sure their checkout of that branch is up to date, then
merge from their local branch, and commit to the central server.

Branch statuses and links
-------------------------

The freedom to create branches is wonderful for encouraging
participation. With all those branches out there, it's good to tell
people which ones are most relevant to them. Pick good names for your
branches! Also, use the branch status - New, Experimental, Mature,
Obsolete, etc - to provide a hint to potential collaborators or testers
about the maturity of your code.

One of the most useful things you can do is to link your branches to a
description of the work they implement.

For example, if your branch fixes a bug, link the branch to the bug
report! And if it's a new feature, track that feature in Launchpad (we
call it a Blueprint) and link the branch to that.

That's the `next stop <FeatureHighlights/BugBranchLinking>`__ in our
review of Launchpad.