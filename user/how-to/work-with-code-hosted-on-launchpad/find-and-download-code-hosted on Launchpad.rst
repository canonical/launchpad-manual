Find and download code hosted on Launchpad
==========================================

So, what does it mean to have code registered in Launchpad? Well, it can
be one of four things:

-  code in a Bazaar branch that's hosted directly by Launchpad
-  a Bazaar branch that's hosted elsewhere and mirrored by Launchpad
-  a Bazaar branch that's hosted elsewhere and registered in Launchpad
   but not mirrored
-  a Subversion or CVS repository that's imported into a Bazaar branch
   hosted by Launchpad.

If all you want is to get hold of that code, you don't need to worry
about its exact relationship with Launchpad because Launchpad sorts all
that out for you.

Get code
--------

`GnomeDo <https://launchpad.net/do>`__ is an application launcher for
Gnome desktops. You can create your own branch of Gnome Do's ``trunk``
`line of development <Projects/SeriesMilestonesReleases#Series>`__ with
just a few keystrokes and without even having to visit Launchpad's web
interface.

Once you've `got Bazaar on your
system <http://doc.bazaar-vcs.org/latest/en/mini-tutorial/index.html#installation>`__,
open a terminal and type the following:

::

   $ bzr branch lp:do

Bazaar will now download the latest version of Gnome Do's trunk branch
to your machine.

::

   $ bzr branch lp:do
   You have not informed bzr of your launchpad login. If you are attempting a
   write operation and it fails, run "bzr launchpad-login YOUR_ID" and try again.
   Branched 524 revision(s).

.. note::
   Don't worry about the login notice, as you're not yet uploading anything
   to Launchpad.

Now you have your own local branch of the Gnome Do trunk, complete with
full version control. You can commit any changes you like to that branch
and, when you're ready, upload your version back to Launchpad to sit
alongside the trunk and any other Gnome Do branches.

You can use this hassle-free way of obtaining branches for any project
that has code registered in Launchpad. All you need is the Launchpad
name of the project, which you can find by looking at the final portion
of the URL to the project's Launchpad overview page. For example: in
Gnome Do's case that's ``https://launchpad.net/do``.

Other branches associated with a project
----------------------------------------

If you want to download something other than a project's main line of
development, you need to visit the project's code overview page.

Let's visit `Gnome Do's code overview
page <https://code.launchpad.net/do>`__. Here you can see a list of all
the Gnome Do-related branches that Launchpad knows about.

Launchpad lists the branches in order of likely importance. So, the
branch that the Gnome Do team have marked as their trunk comes first and
is what you get when you use ``bzr branch lp:do``. At the time of
writing, the next two branches in the list are also associated with
Gnome Do series; in this case ``0.6`` and ``devel``. The address you need to
give Bazaar is also shown for both of these branches: for example,
``bzr branch lp:do/0.6`` and ``bzr branch lp:do/devel``.

Community branches
~~~~~~~~~~~~~~~~~~

Launchpad and Bazaar's flexibility mean that anyone can upload their
branch of code and associate it with any project in Launchpad. This is
great news because you can get near instant access to all development
effort for that project.

Click on any of the branches in Gnome Do's list and you'll see exactly
what you need to type in order to download it and create your own local
branch, using Bazaar.

Code hosted elsewhere
---------------------

So far, we've looked at branches of code that are hosted directly on
Launchpad. Hosting on Launchpad is a quick and free way to publish your
branch. However, as we saw in the introduction, you can use Launchpad to
get hold of code that's hosted elsewhere too.

`Bitlbee <https://launchpad.net/bitlbee>`__ is a gateway between various
IM networks and IRC. The bitlbee trunk branch is hosted by Bitlebee
themselves and mirrored by Launchpad. That makes no difference to
actually getting hold of that branch. Simply type:

::

   $ bzr branch lp:bitlbee

Similarly, you can get hold of code from the
`Banshee <https://launchpad.net/banshee>`__ music player's Subversion
repository as a Bazaar branch with:

::

   $ bzr branch lp:banshee

Wherever code originates, visit its overview page in Launchpad to find
the Bazaar command to download it to your own machine and create a local
branch.

Staying up to date
------------------

If you want to stay up to date with the commits made to a branch, you
can subscribe both to email updates and also to an Atom feed. Visit the
branch's overview page and click *Subscribe yourself* to receive email
updates each time someone commits to the branch. Alternatively, a feed
icon will appear in your browser's address bar (if you're using
Firefox); click that to subscribe to the Atom feed.

Similarly, Launchpad offers Atom feeds of:

-  branches associated with a person or team
-  commits made by a person or team
-  commits made to branches associated with a project.

To subscribe, visit the overview page for any of those and select the
feed icon in your browser's address bar.

Next steps
----------

Now that you've created your own branch of code from Launchpad you can
`upload it back to Launchpad <Code/UploadingABranch>`__ to appear
alongside all the other code associated with that project.