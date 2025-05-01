Upload your Bazaar branch to Launchpad
======================================

Just as it's easy to `create your own Bazaar
branch <Code/FindingAndDownloading>`__ of code that's registered in
Launchpad, you can also host your code on Launchpad. It's free and means
that your code is:

-  available for anyone else to download and work with
-  publicly associated with the project it relates to
-  ready to take part in public merge requests and code review.

The easiest way to get your code on Launchpad is to push your branch
using Bazaar. Alternatively, Launchpad can mirror a Bazaar branch that's
hosted elsewhere on the internet or convert existing git, Subversion and
CVS repositories into Bazaar branches.

Push your Bazaar branch to Launchpad
------------------------------------

If you've already got a Bazaar branch on your local machine, getting
that branch up to Launchpad couldn't be easier.

In your terminal, go to the branch directory and type:

::

   bzr launchpad-login userid
   bzr push lp:~userid/project-name/branch-name

Replace *userid* with your Launchpad id, *project-name* with the
project's Launchpad id and then chose whichever branch name you want.

.. tip::
    If you have multiple ssh keys, you need to tell Launchpad which
    key to use.

Edit your ``~/.ssh/config file`` (if one doesn't exist, create a new
one) and add the following:

::

   Host bazaar.launchpad.net
       IdentityFile ~/.ssh/your_launchpad_key
       User your-launchpad-user-name

You should check the `fingerprint <SSHFingerprints>`__ of
bazaar.launchpad.net when prompted to do so by SSH.

Bazaar will now push your branch up to Launchpad. You can then view the
branch on your own `Launchpad branches
page <https://code.launchpad.net/people/+me>`__ and also on the
project's branches page.

Pushing subsequent changes to Launchpad
---------------------------------------

Now, when you work on your code, all you need to do is commit changes to
your local branch using ``bzr commit -m "Commit message"``.

You only need to push your changes up to Launchpad when you want to make
them public.

Mirror a branch that's hosted elsewhere
---------------------------------------

If you prefer to host your branch elsewhere, but still want to make it
available in Launchpad, you can ask Launchpad to mirror it.

Setting up a branch mirror is similar to registering a hosted branch,
except you supply the URL to your branch and Launchpad makes periodic
copies.

Next steps
----------

If you need to work on the same branch of code with a group of people,
you can `create a team branch <Code/TeamBranches>`__.
