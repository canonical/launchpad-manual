Create and Publish branches
===========================

For this section of the feature highlights guide, you might like to
actually create and publish a branch or two. You'll need to have Bazaar
installed and to have registered SSH keys with Launchpad, which you can
use to authenticate yourself.

For Ubuntu users, simply type "sudo apt-get install bzr" and you will be
all set. For users of other platforms, take a look at `these
instructions <http://bazaar-vcs.org/Download>`__ to install Bazaar for
yourself.

{i} Find out `how to create your SSH key and upload it to
Launchpad <CreatingAnSSHKeyPair>`__.

You should have at least version 0.15 of Bzr installed. To check:

::

   % bzr version
   Bazaar (bzr) 0.15.0candidate2

Alternatively, just read over the text to get a sense of what's
possible.

Create your branch
------------------

Now, let's create a branch of the famous ``GNU Hello`` application, which
is used as a demonstration of several GNU best practices and
technologies.

For simplicity we will use HTTP to fetch the code for this branch. This
is quite an inefficient protocol, for this purpose, so it takes a little
longer than normal to fetch the code. You can also use the optimised
smart server protocol, once you have registered your SSH keys to access
the Launchpad server securely.

We use HTTP here because it can be done anonymously.

::

   % bzr branch https://code.launchpad.net/gnuhello
   Branched 191 revision(s).

Done! You now have your own branch of GNU Hello.

::

   % cd gnuhello
   % ls
   ABOUT-NLS   ChangeLog     COPYING  Makefile.am  README        tests
   AUTHORS     ChangeLog.O   doc      man          README-alpha  THANKS
   autogen.sh  configure.ac  gnulib   NEWS         README.dev    TODO
   build-aux   contrib       INSTALL  po           src

You can see the latest commits on this branch. This is a branch of the
trunk, so it has all the latest commits that trunk had when you created
the branch.

::

   % bzr log | head --lines=13
   ------------------------------------------------------------
   revno: 191
   committer: karl
   timestamp: Tue 2007-02-13 23:09:30 +0000
   message:
     .
   ------------------------------------------------------------
   revno: 190
   committer: karl
   timestamp: Mon 2007-01-22 14:40:04 +0000
   message:
     update from texinfo
   ------------------------------------------------------------

Make changes to your branch
---------------------------

Because this is YOUR branch, you can commit to it immediately. Try
making some changes, then type "bzr commit".

Before doing this, you can optionally configure Bazaar so that it knows
who you are, and records that information with each commit. Type

::

   bzr whoami "Joe Smith <email@example.com>"

to set that up.

Publishing branches
-------------------

If you have `set up some SSH keys in your Launchpad
account <https://launchpad.net/people/+me/+editsshkeys>`__, you can
publish your branch with a single command.

You need to know the project name in Launchpad, your own Launchpad
username, and of course the name you want to give this branch. If your
branch is for personal use, and you don't want it to be listed in a
specific project, you can call it "junk". Simply use

::

   +junk

instead of the project name.

Continuing our example above, we will push this GNU Hello branch to
Launchpad with the command:

::

   % bzr push bzr+ssh://<me>@bazaar.launchpad.net/~<me>/gnuhello/mine

Of course, you must substitute your Launchpad username for in both
places in the above command.

Now, if you take a look at your own branch listing page, you will see
the GNU Hello branch listed:

``\ https://code.launchpad.net/\~``

As you can see, branching from an existing project, and publishing your
branch, are extremely easy. Once your branch is published it is easy for
others to find. If you would like your code to be included in the
project's official line of development (and hence in the next release!)
you can simply ask the project maintainers to review and merge your
branch.

It may seem strange that you need your account name TWICE in the
publishing command given above. The reason is that the first time
(account@...) is to tell Launchpad who you are logging in as. The second
time (~account/) is to tell it to put the branch into *your*
directory.

This is needed because you can also publish branches into directories
for each of the teams of which you are a member. And that leads us to
the next stop on our tour - `Team
Branches <FeatureHighlights/TeamBranches>`__!