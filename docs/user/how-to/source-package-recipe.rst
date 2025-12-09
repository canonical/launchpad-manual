.. _create-a-source-package-recipe:

Create a source package recipe
##############################

.. include:: /includes/important_not_revised_help.rst


Overview
========

To create your own source package recipes, you need:

-  sourcecode in Launchpad (either hosted directly on Launchpad or
   imported from elsewhere)
-  a branch with buildable code
-  a recipe.

You should also have confirmed that your build will work by testing it
locally.

Let's take a quick look at these in turn and then we can look at them in
more detail later on.

Watch the screencast
--------------------

If you prefer, you can `watch our screencast <http://youtu.be/_bG-SXNX9Ww>`_, which will take you through each of the steps you need to get a source package recipe up and running.

Code in Launchpad
=================

The code that you want to use for your source package recipe must be in
Launchpad as a :ref:`Git <host-a-git-repository-on-launchpad>` branch that you 
have uploaded to Launchpad (easier) or as :ref:`an import from elsewhere <code-imports>`.

You can import code that is hosted anywhere on the internet, so long as
Launchpad can reach it and it is available without needing a username
and password. Launchpad can import code hosted in the following formats:

-  Bazaar
-  git
-  Subversion
-  CVS

Packaging
=========

It's likely that someone has already packaged the software you want to
build. If that's the case, Launchpad can borrow that packaging
information and you're pretty much sorted.

Similarly, if there's a branch in Launchpad that contains packaging
information for your software, you can use that.

If there's no existing packaging, either for Debian or Ubuntu, you'll need to create your own. You should `read the Ubuntu community's guide to packaging <http://packaging.ubuntu.com/html/>`_ to get started.

**Note:** you need to make sure that the build process specified by your
packaging and deal with what's in your branch. For example, if you work
on a C project with autotools, you might have to run ``autoreconf -i``
at some stage during the build to make sure that all the auto-generated
files (which are not in version control) are present.

The recipe
----------

The recipe is a simple description of what steps are needed to construct
a package from your various Bazaar or Git branches. It specifies:

-  which branch to use: such as the project's trunk branch or an
   experimental branch
-  where to find the packaging information: e.g. an Ubuntu source
   package branch or some other Bazaar or Git branch
-  which version to give the package: this is important to allow users
   to upgrade to the stable version once it is released in their distro
-  what to modify to make the source build properly.

Trying it out
=============

The best way to learn how to create a source package recipe is to try
out a simple example. All you need is a text editor and the
*bzr-builder* plugin for Bazaar, or the *git-build-recipe* program for
Git.

Getting bzr-builder
-------------------

On recent Ubuntu releases you can `install the bzr-builder package <http://apt.ubuntu.com/p/bzr-builder>`_ to run tests locally.

Getting git-build-recipe
------------------------

As of Ubuntu 16.04, you can `install the git-build-recipe package <http://apt.ubuntu.com/p/git-build-recipe>`_ to run tests locally.

On previous releases of Ubuntu, you can get the version running on
Launchpad's builders from the `buildd PPA <https://launchpad.net/~canonical-is-sa/+archive/ubuntu/buildd>`_.

Writing a basic recipe
----------------------

There are different ways to write a recipe but, for this example, we're
going to use the simplest: you use the project's trunk, which contains
no packaging, and nest another branch that contains only packaging
information.

For this example, we'll use the `Wikkid wiki <https://launchpad.net/wikkid>`_ project.

The anatomy of a recipe
~~~~~~~~~~~~~~~~~~~~~~~

Open your text editor and enter:

::

   # bzr-builder format 0.3 deb-version {debupstream}+{revno}+{revno:packaging}
   lp:wikkid
   merge packaging lp:~thumper/wikkid/debian

Now save the file as *wikkid.recipe*.

**Important:** if for whatever reason either the Wikkid trunk or
Thumper's packaging branch become unbuildable you may need to try this
out with another project.

This recipe is pretty straightforward to read, but let's look at each
line in turn.

The first line tells Launchpad which recipe version we're using (in this
case it's 0.3), along with how we want to name the resultant package.

The next line specifies the code branch, using Launchpad's short name
system.

Finally, we specify where to find the packaging branch and say that we
want to nest it into the code branch.

Testing your recipe and build
-----------------------------

You should always test your recipe locally before sending it to
Launchpad.

Testing the recipe
~~~~~~~~~~~~~~~~~~

Let's start by testing the recipe itself. For now, we'll assume you're
running the Ubuntu version that you want to test against.

**Note:** if you want to test a specific version, see the `Ubuntu guide <http://wiki.ubuntu.com/UsingDevelopmentReleases>`_.

The bzr-builder plugin adds a *dailydeb* command to Bazaar.

Let's try it out in your terminal:

::

   $ bzr dailydeb --allow-fallback-to-native wikkid.recipe working-dir

This processes your recipe and creates a directory called
``working-dir``, into which it places the resulting source tree and
source package.

Things are similar for git, but use ``git-build-recipe`` instead of
``bzr dailydeb``.

Testing the build
~~~~~~~~~~~~~~~~~

If bzr-builder processed the recipe without any problems, you'll now
have a source package. Let's make sure it builds.

First, you need to set up *pbuilder*, a tool that creates a clean,
minimal environment for the build. This ensures that the build will work
everywhere and that it's not dependent on something unusual in your own
environment.

**Step 1:** Install pbuilder with ``sudo apt-get install pbuilder``

**Step 2:** Edit ``~/.pbuilderrc`` and add:

::

   COMPONENTS="main universe multiverse restricted"

**Step 3:** ``sudo pbuilder create``

Now, kick off the test build with:

::

   sudo pbuilder build <working-dir>/<project>_<version>.dsc

If the build succeeds, you can test-install the resulting package from
``/var/cache/pbuilder/result/``.

Setting up the recipe in Launchpad
==================================

Now that you've confirmed that both the recipe and build work, the rest
is very simple.

Browse to the branch you want to build in Launchpad and click
**Create packaging recipe**.

**Create the build in Launchpad**

Now fill in all the necessary details:

-  *Name:* a short name for the recipe. Remember: you might want more
   than one.
-  *Description:* make your intention clear and tell potential users of
   the build what they're signing up for.
-  *Owner:* select who drives these builds.
-  *Build daily:* enables automatic daily builds, rather than building
   on-demand only.
-  *Daily build archive:* the PPA where you want to publish the package.
-  *Default Distribution Series:* select all the Ubuntu releases you
   want to build the package for. Make sure all these builds work before
   you sign up for them!
-  *Recipe text:* paste your recipe in here.

Building
========

If you have checked "built daily", Launchpad will automatically schedule
a build of your recipe once every day, if any of the branches specified
have changed since the last build. However, it's a good idea to try
building it yourself first, to make sure that everything is working
correctly. You can use the "Request build(s)" link for this: **Manually request a build**
