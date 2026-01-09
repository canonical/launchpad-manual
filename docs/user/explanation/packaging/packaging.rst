.. _packaging:

Packaging
=========

Using Launchpad, you can build and distribute packages for operating
systems that use Debian-style packaging. Right now, Launchpad's
packaging system (sometimes called Soyuz) supports the build and
distribution of packages for Ubuntu.

Launchpad can help you build and distribute two types of Ubuntu package:
official packages and your own packages in your personal package archive
(PPA), which is your own apt repository.

-  :ref:`personal-package-archive`: build and distribute Ubuntu packages in your apt repository.

   -  :ref:`Installing software from a PPA <install-software-from-ppas>`: how to get and use software from a PPA.
   -  :ref:`Building a source package: <building-a-source-package>` how to adapt your Ubuntu package building skills to your PPA
   -  :ref:`Uploading a source package <upload-a-package-to-a-ppa>`

-  :ref:`Common package upload errors <troubleshoot-package-upload-errors>`

-  :ref:`Prioritising package builds <prioritising-builds>`: find out how Launchpad calculates the priority of package builds (i.e. build scores)

-  `Official Ubuntu packages <https://wiki.ubuntu.com/MOTU/GettingStarted>`_: find out about becoming an Ubuntu packager with the MOTU team

-  :ref:`package recipes <source-package-recipes>`: automatically assemble a package from git branches

-  `Packaging binaries <https://wiki.ubuntu.com/MOTU/School/PackagingWithoutCompiling>`_: how to go about packaging software which is only available as a binary.

To get started with your own source package recipes, you'll need source code in Launchpad,
packaging information and a recipe that brings them all together.

.. _source-package-recipes:

Source package recipes
----------------------

Source package recipes are a great way of trying out the latest code
from a project, with relatively little effort.

Whether you want to help others test your code, or you want to run a
modified or bleeding edge version of your favourite software, with
Launchpad's source package recipes you can:

-  take the code in one or more Git branches
-  borrow the packaging information from the software's existing Ubuntu
   package
-  sit back and get an automatic build on every day the source changes,
   which is then published in the PPA of your choice.

So you can run the latest code, with or without your chosen
modifications, without having to install from source. Plus, you get
automatic Ubuntu update reminders whenever the package changes.

Source package builds is the name we give to this Launchpad feature.
Most source package builds are automatically built each day and you'll
see those referred to as daily builds.

Why source package recipes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're running a software project, the main advantage of source
package recipes is that they help with testing. In particular, they can
help:

-  **Tighten the feedback loop:** making new code available almost
   straight away, in a way that's easy to install, brings developers and
   testers closer together
-  **Lowers the barrier to becoming a tester:** adding a PPA is an easy
   and common task for Ubuntu users, meaning that anyone can help test
   your software
-  **Easier verification testing:** people who've reported a bug can
   quickly and simply check that the bug is fixed in a future revision.

There are also some considerations that may mean source package recipes
are not suitable for your project, such as:

-  Your project doesn't use feature branches or keep the trunk in a
   buildable state.
-  Your project is in the early stages of development or in the middle
   of a major refactoring and not yet ready for testing.
-  Sometimes users think source package builds are supported releases,
   which can both add to bug noise and generate support requests.
-  If users cannot easily go back to their previous version of your
   software after using source package builds (for example you do a
   one-time database upgrade or something from one version to another)
   then this can be problematic.

.. _source-build-recipes:

Source build recipes
--------------------

A "recipe" is a description of the steps needed to construct a package
from a set of Git branches. Its format specifies:

-  Which branch to use for the source code: trunk branch, beta branch,
   etc.
-  Which branch to use for the packaging information: separate branch,
   Ubuntu branch, etc.
-  The correct package version (so people can still upgrade to the new
   stable version when it's released.
-  What to modify to make the source build properly.

This recipe format is used for git via git-build-recipe.

Writing a recipe
~~~~~~~~~~~~~~~~

Recipes have a simple format.

They always start with a line similar to this:

::

   # git-build-recipe format 0.4 deb-version 1.0+{revtime}

Let's take a look at this in more detail:

-  ``# git-build-recipe format 0.4`` specifies which recipe format we're
   using. The current format is 0.4.
-  ``deb-version 1.0+{revtime}`` specifies the version to give the
   package we're building. ``{revtime}`` is a substitution variable;
   more on which later.

Specifying the branches
~~~~~~~~~~~~~~~~~~~~~~~

The next line of a recipe specifies which branch to base the package on ``lp:germinate``.

This says that we will use the trunk of the ``germinate`` project in
Launchpad. This could just as easily be any other branch in Launchpad,
using the short format that you can find on any branch overview page.

If you're using git, then the format is similar, but you should normally
provide a branch name as a revision specifier (if you don't, then the
recipe builder will assume HEAD):

::

   lp:germinate master

Note that if you've converted a project from bzr to git, then the
``lp:PROJECT`` alias for the project's default branch may still be
configured for bzr, and will currently take precedence over the git
default repository. You can always disambiguate like this:

::

   https://git.launchpad.net/germinate master

Next, you can specify any number of other branches to include. There are
two ways to include those branches additional branches:

-  merge: this specifies a simple ``git merge`` of the two branches.
-  nest: inserts the content of the second branch into a specific
   location within the main branch.

Merging
~~~~~~~

::

    merge SHORT-NAME URL [REVISION]

Most often you'll use the "merge" command:

::

   merge fix-build lp:~contributor/germinate fix-build

Here ``fix-build`` is a unique short name that we'll use to refer to
this branch in substitution variables. The short name can be anything
you like, so long as it is unique to this branch within this recipe.

In this example, the branch ``fix-build`` fixes a problem in the trunk
that prevents it from building. This branch could be anything:
stand-alone packaging information, some other modification to the branch
that's not yet present in the trunk and so on.

You should normally provide a branch name as a revision specifier.

The second ``fix-build`` here is something that identifies a commit,
usually a ref (branch or tag) name. Be careful not to confuse this with
the short name used in substitution variables; you could equally well
use the following and only have to adjust some variable references:

::

   merge some-nonsense lp:~contributor/germinate fix-build

Nesting
~~~~~~~

::

    nest SHORT-NAME URL TARGET-DIRECTORY [REVISION]

Nesting works in a similar way but has more scope:

::

   nest pyfoo lp:pyfoo foo

The ``nest`` keyword puts the contents of one branch into a specific
location in another branch, instead of merging it.

In this case, we are nesting the contents of ``lp:pyfoo`` in a new
``foo`` directory in the ``lp:germinate`` branch. Again, we've given
the branch a short name, ``pyfoo``, that we can use to refer to it in
substitution variables.

You can also act on the nested branch in the same way as you can the
main branch: you can merge and nest other branches in your nested
branch.

::

   nest pyfoo lp:pyfoo foo master
   merge branding lp:~bob/pyfoo ubuntu-branding

Be careful not to confuse the short name used for substitution variables
(here, ``branding``) with the git branch name (here, ``ubuntu-branding``).

Any lines that are indented by two spaces, and are directly below your
``nest`` line, will act on the nested branch. In this example, the
``ubuntu-branding`` branch will be merged into ``pyfoo`` before
it is nested in your primary branch.

nest-part
^^^^^^^^^

::

    nest-part SHORT-NAME URL SOURCE-DIRECTORY [TARGET-DIRECTORY [REVISION]]

If you want to nest only one directory from another branch, you can use
``nest-part``. It works in the same way as ``nest``, except that
you specify which directory you're taking from the nested branch.Provide a 
branch name as a revision specifier:

::

   nest-part packaging lp:~some-person/some-project debian debian master-with-packaging

Again, we've given the branch a short name, ``packaging``, that we can
use to refer to it in substitution variables. Be careful not to confuse
this with the git branch name (here, ``master-with-packaging``).

Packaging information
~~~~~~~~~~~~~~~~~~~~~

One of the branches that you include in your recipe must include
packaging information in the ``debian`` directory. If it doesn't
appear in one of the other branches you specify, you must specifically
pull in a ``debian`` directory from elsewhere.

In our example recipe we'll use the ``nest-part`` above.

What our recipe looks like
--------------------------

Adding up all the lines above, our full recipe would look like this:

::

   # git-build-recipe format 0.4 deb-version 1.0+{revtime}
   lp:germinate
   merge fix-build lp:~contributor/germinate fix-build
   nest pyfoo lp:pyfoo foo master
     merge branding lp:~bob/pyfoo ubuntu-branding
   nest-part packaging lp:~some-person/some-project debian debian master-with-packaging

Specifying revisions
--------------------

Sometimes you want to specify a specific revision of a branch to use,
rather than the HEAD symbolic reference.

You can do this by including a revision specifier at the end of any
branch line. For example:

::

   merge packaging lp:~bob/pyfoo ubuntu-branding revtime:2355

Similarly for the main branch:

::

   lp:germinate revtime:1234

Git allows you to tag a certain revision with an easily memorable
name. You can request a specific tagged revision like this:

::

   lp:germinate tag:2.0

Here, the recipe would use the revision that has the tag "2.0".

A revision specifier may be anything that you could pass to ``git rev-parse`` 
in a clone of the given repository.

Version numbers and substitution variables
------------------------------------------

In the first line of the recipe, we specified a version number for the
package we want to build, using:

::

   deb-version 1.0+{revtime}

Rather than specify a fixed version number, we need it to increase every
time the package is built. To allow for this, you can use multiple
substitution variables.

.. list-table::
   :header-rows: 1

   * - Variable
     - Purpose
     - Introduced in (recipe format version)
   * - time
     - Replaced by the date and time (UTC) when the package was built.
     - 0.1
   * - revno
     - Replaced by the revision number.
     - 0.1
   * - latest-tag
     - Replaced by the name of the most recent tag
     - 0.4
   * - revdate
     - Replaced by the date of the revision that was built
     - 0.4
   * - revtime
     - Replaced by the time of the revision that was built
     - 0.4
   * - git-commit
     - Replaced with the first 7 characters of the git commit that was built
     - 0.4
   * - debversion
     - Replaced with the version in debian/changelog
     - 0.3
   * - debupstream
     - Replaced by the upstream portion of the version number taken from debian/changelog. For example: if the version is 1.0-1, this would evaluate to 1.0.
     - 0.1
   * - debupstream-base
     - Similar to {debupstream}, but with any VCS identifiers (e.g. "bzr42", "svn200") stripped, and updated to always end with a "+" or "~")
     - 0.3

All variables other than ``time`` are derived from a particular
branch. By default they use the base branch (eg. ``{revno}``), but
they can also use a named branch (eg. ``{revno:packaging}``).

``debversion``, ``debupstream`` and ``debupstream-base``
require ``debian/changelog`` to exist in the given branch. For
recipe versions 0.4 and newer, you **must** specify the name of the
branch (e.g. ``{debupstream-base:packaging}``). In recipe versions
0.3 and earlier, the changelog will be read from the final tree if the
branch name is omitted.

The advantages of using {revno} and/or {time}:

-  **{revno}:** if you want to ensure there's a new package version
   number whenever the contents of the branch has changed. This is
   particularly useful if you specify a {revno} for each branch in your
   recipe.
-  **{time}:** if you want the package version to increase whether or
   not the contents of one of more of the branches has changed.

You can use as many substitution variables as you like. For example:

::

     deb-version 1.0+{revno}-0ubuntu0+{revno:packaging}+{time}

Here the ``packaging`` in ``revno:packaging`` refers to the
short name we gave the branch we're using for packaging.

This example would generate a package version something like:

::

   1.0+4264-0ubuntu0+2145+200907201627

Most substitution variables work the same way for git-based recipes.
``{revno}`` is a little peculiar: it is replaced by the length of
the left-hand history (i.e. following only the first parent at each
step) of the commit in question, to emulate Bazaar revision numbers.
This is not very git-like, and most users should normally use
``{revtime}`` or ``{revdate}`` instead, which are monotonically
increasing. However, this can result in very long version strings,
especially if there are multiple branches involved; so this may for
instance be useful as ``{revno:packaging}`` to encode the length of
the packaging branch.

``{git-commit}`` should be used with care. Commit hashes do not
increase monotonically, so are not normally suitable for use in version
strings. At best, this may be useful for information.

Further information
-------------------

- :ref:`Daily builds getting started <building-a-source-package>`
