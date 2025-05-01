Branch imports
==============

There's a lot of free software code available in CVS or Subversion (SVN)
repositories. as their primary revision control system. They are
well-understood and fast - for the core developers - systems. While they
do have the disadvantage that branching and merging are not well
supported, they're still effective and hence widely used.

The biggest downside to this approach, however, is that it treats
newcomers and drive-by participants as second-class citizens. They don't
get any form of revision control that can interoperate with that core
team. Instead, they have to email patches, which can rot over time.

Launchpad and Bazaar can help you address this problem, without asking
the project's core developers to change en-masse to a different version
control system. You can ask Launchpad to import a CVS or Subversion
repository into a Bazaar branch on Launchpad.

Trunk imports
-------------

Launchpad supports the import of the primary development trunk of a
project from CVS or SVN. A good example is the Drupal project. Launchpad
imports Drupal's trunk as `its "main"
series <https://launchpad.net/drupal/main>`__ in Launchpad.

As you can see, there's a Bazaar branch of Drupal's code. Launchpad
updates that branch regularly by importing the latest from Drupal's
trunk Subversion repository. It works just like any other branch in
Launchpad: you can see the latest commits and you can create your own
Bazaar branch of it and then upload it back to Launchpad.

Perhaps the most visible difference between a branch that's the result
of an import from CVS or Subversion is that the branch's owner is the
`VCS imports <https://code.launchpad.net/~vcs-imports>`__ team/

Requesting an import
--------------------

Import precision
~~~~~~~~~~~~~~~~

Unfortunately, the initial import process is not an exact science. CVS
and Subversion don't record enough information for a deterministic
import into Bazaar, which is more rigorous about things like renames and
changesets.

In most cases, where the CVS and SVN repositories have not been manually
edited or altered, we can infer what we need and the import goes through
smoothly. Sometimes, however, people have tried to work around
limitations in CVS or SVN by altering the repositories
behind-the-scenes. This is especially true of CVS, which does not
support renames, so people have tended to do them manually.

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
days to get a good import together. In a very few cases, the old
repositories are so wedged that we can't get all the history exactly
right. It's best just to get started and see how it goes. We are
constantly improving the voodoo.