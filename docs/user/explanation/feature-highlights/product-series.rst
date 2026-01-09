.. _series-major-stable-and-development-branches:

Series: major stable and development branches
=============================================

.. include:: /includes/important_not_revised_help.rst

When we think of the way a project organises itself, there are some
special branches: they represent major lines of development, and
releases are "cut" from them. Typically these branches represent:

-  **Development trunk:** this is the current "tip" of development
   across the core project community, representing the very cutting edge
   of work on that project. In general, the only releases made from the
   development trunk are snapshot, milestone or test releases, to
   generate more widespread testing and feedback.

-  **Stable and supported branches:** these represent the latest work on
   the stable versions of the project, which are still supported. If
   updated stable releases are to be made they will come from these
   branches.

-  **Obsolete branches:** for major release versions that are now out of
   date and no longer being updated. It's likely that work is no longer
   done on these branches.

We call each of these "major" lines of development a "series", because
they primarily represent a "series of releases of the same major
version".

Note, there are usually multiple series for a given project, especially
one that has produced stable releases. For example, a project might have
a version 1.2 which is still supported, a 1.3 which is the "latest
stable version" and recommended for new users, and a trunk which
represents the current line of active development and is the source of
snapshot test releases for the next stable version.

Take a look at the Zope3 project: https://launchpad.net/zope3

The stable and trunk series are shown in the "Timeline" section of the
page:

The trunk series here is identified with the words "Current development
focus".

Naming series
-------------

There's some flexibility in the way projects name and organise
themselves. For example, in the GNOME project, the "development trunk"
is a series with an "odd" version number, such as 2.17. When it is ready
for release, it is branched with an "even" version number, such as 2.18.
Once GNOME make the stable release, the branch it to create 2.19, the
new "trunk".

Sometimes, projects also call the trunk "MAIN", a term from the days of
CVS. In the Zope3 example above, the 3.4 series was the trunk at the
time of writing.

For convention, we encourage projects to call their development focus
"trunk" and leave it as the same branch over time. When creating a new
stable series, branch from trunk, create the series and link the branch
to that series. This ensures that people who create a checkout of
"trunk" don't find that it goes stale because it has been turned into a
stable series, suddenly. And those who checkout or branch from a stable
series will get what they expect, too.

Series and branches
-------------------

In Launchpad, each project can register multiple series. Each of those
series can be associated with a branch. By default, if you don't specify
which series you are interested in, you will get the current development
trunk series (**usually** called trunk, but not always). 

Note that this is different to the previous approach of branching from a
specific person's version of a project. Here you are branching from one
of the "major project branches", or series.

Not every series has a branch associated with it. Often, series are
registered to handle a set of translations for a particular major
version of the software, or so that bugs can be targeted there for
release management. But we do encourage you to make sure, when you
branch from trunk to make a new major stable release, that you set up a
series for it and link the branch to it.
