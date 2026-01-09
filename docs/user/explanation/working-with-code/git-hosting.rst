.. _hosting-git-repositories:

Hosting Git repositories
========================

.. include:: /includes/important_not_revised_help.rst

Launchpad supports hosting `Git <http://git-scm.com/>`_ repositories.
This is distinct from the :ref:`code import <code-imports>` facility that
Launchpad has included for many years; it is now possible to host Git
repositories on Launchpad directly.

Git repositories use a somewhat different model from Bazaar branches:
operations such as cloning happen at the level of a repository, but it
is common for a single repository to contain many branches. This means
that the Launchpad interface needs to be laid out somewhat differently
to support that.

What's supported?
-----------------

This summary is up-to-date as of December 2022.

Launchpad supports Git hosting. This means that you can:

-  push Git repositories over SSH or HTTPS
-  clone repositories over git://, SSH, or HTTPS
-  see summary information on repositories and the branches they contain
   in the Launchpad web UI
-  follow links from the Launchpad web UI to a full-featured code
   browser
-  push and clone private repositories, if you have a commercial
   subscription to Launchpad
-  propose merges from one branch to another, including in a different
   repository, provided that they are against the same project or
   package
-  link Launchpad bugs to merge proposals
-  add :ref:`webhooks` to notify third-party services when
   repositories are changed
-  use :ref:`recipes <source-package-recipes>` to build packages in PPAs
   for code in Launchpad-hosted Git repositories
-  mirror repositories from other sites

Configuring Git
---------------

Git identifies repositories using URLs. Unlike Bazaar, there is no
built-in abbreviation for repositories hosted on Launchpad, but it is
very easy to add such a thing yourself. Edit ``~/.gitconfig`` and add
these lines, where ``USER`` is your Launchpad username:

::

   [url "git+ssh://USER@git.launchpad.net/"]
           insteadof = lp:

This allows you to type ``git clone lp:REPOSITORY`` instead of ``git
clone git+ssh://git.launchpad.net/REPOSITORY``.

The rest of this documentation assumes that you have configured Git this
way.

You should check the :ref:`fingerprint <ssh-fingerprints>` of
git.launchpad.net when prompted to do so by SSH.

Getting code
------------

You can fetch the default repository for a project like this:

::

   $ git clone lp:PROJECT

For example, ``git clone lp:launchpad`` fetches Launchpad itself (or
will once we've finished converting it to Git!).

To keep your local clone up to date, run:

::

   $ git pull

Pushing code
------------

You can add a "remote" to your repository like this, if you own the
project:

::

   $ git remote add origin lp:PROJECT

Or like this (where ``USER`` is your Launchpad username), if you do not
own the project but want to contribute to it:

::

   $ git remote add origin lp:~USER/PROJECT

Or to push a repository that isn't part of any Launchpad project or
package, e.g. an ad-hoc experiment:

::

   $ git remote add origin lp:~USER/+git/REPOSITORY-NAME

Now, you can push a branch using a command such as this:

::

   $ git push origin my-changes

Permissions
-----------

By default, repository owners may create, push, force-push, or delete
any branch or tag in their repositories, and nobody else may modify them
in any way.

Repository owners can use the "Manage permissions" page of a repository
to change this by protecting branches or tags. By default, protecting a
branch implicitly prevents repository owners from force-pushing to it or
deleting it, while protecting a tag prevents repository owners from
moving it. You can modify these default permission grants to be more
restrictive (for example, you might prevent anyone from pushing to an
archived branch), or to grant other permissions (for example, you might
want to allow a contributor to push to certain branches in your
repository without owning it).

You may create rules that match a single branch or tag, or wildcard
rules that match a pattern: for example, ``*`` matches everything, while
``stable/*`` matches ``stable/1.0`` but not ``master``. The pattern is
implemented using Python's
`fnmatch <https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch>`__.

Any owner of a repository can change its permissions, so restricting
permissions for other repository owners is not a strict security
barrier. However, you can use the "View activity" page of a repository
to see what permission changes have been made.

Launchpad works out the effective permissions that a user has on a
protected branch or tag as follows:

1. Take all the rules that match the branch or tag.
2. For each matching rule, select any grants whose grantee matches the
   user, as long as the same grantee has not already been seen in an
   earlier matching rule. (A user can be matched by more than one
   grantee: for example, they might be in multiple teams.)
3. If the user is an owner of the repository and there was no previous
   "Repository owner" grant, then add an implicit grant allowing them to
   create or push.
4. The effective permission set is the union of the permissions granted
   by all the selected grants.

Repository URLs
---------------

Every Git repository hosted on Launchpad has a full "canonical" URL of
one of these forms (these are the versions you'd use in a web browser;
you only need to change the scheme and host parts for the command-line
Git client):

* ``https://code.launchpad.net/~OWNER/PROJECT/+git/REPOSITORY``::
  This identifies a repository for an upstream project.
* ``https://code.launchpad.net/~OWNER/DISTRIBUTION/+source/SOURCE/+git/REPOSITORY``::
  This identifies a repository for a source package in a distribution.
* ``https://code.launchpad.net/~OWNER/+git/REPOSITORY``::
  This identifies a "personal" repository with no particular connection to any
  project or package (like "+junk" in Launchpad's Bazaar code hosting).

These are unique, but can involve quite a lot of typing, and in most
cases there's no need for more than one repository per owner and target
(project or package). Launchpad therefore has the notion of "default
repositories". A repository can be the default for a target, in which
case it has one of these forms:

* ``https://code.launchpad.net/PROJECT``::
  This is the default repository for an upstream project.
* ``https://code.launchpad.net/DISTRIBUTION/+source/SOURCE``::
  This is the default repository for a source package in a distribution.

Or a repository can be a person's or a team's default for a target, in
which case it has one of these forms:

* ``https://code.launchpad.net/~OWNER/PROJECT``::
  This is an owner's default repository for an upstream project.
* ``https://code.launchpad.net/~OWNER/DISTRIBUTION/+source/SOURCE``::
  This is an owner's default repository for a source package in a distribution.

We expect that projects hosting their code on Launchpad will normally
have their primary repository set as the default for the project, and
contributors will normally push to branches in owner-default
repositories. The extra flexibility with named repositories allows for
situations such as separate private repositories containing embargoed
security fixes.

HTTPS authentication
--------------------

Access Tokens
~~~~~~~~~~~~~

To push repositories over HTTPS, or to clone or pull private
repositories over HTTPS, you need to use access tokens. These are text
strings generated by Launchpad that can be used as HTTP passwords for
particular repositories, with scope limitations and optional expiry
dates.

You can generate access tokens for a particular repository - which will
grant access to that particular repository, or for a project - which
will grant access to all repositories within that project (accessible by
the user that generated them).

Valid scopes
~~~~~~~~~~~~

For use with the ``git`` client, the relevant scopes are
``repository:pull`` to allow cloning or pulling the repository, and
``repository:push`` to allow pushing the repository; you may select
either or both.

There is also ``repository:build_status`` which allows seeing and
updating the build status for all commits in a repository.

Generating access tokens
~~~~~~~~~~~~~~~~~~~~~~~~

Via UI
^^^^^^

To generate an access token for a repository or project:

1. Navigate to it in the Launchpad web UI
2. Select "Manage access tokens"
3. Enter a description of the token
4. Select some scopes that the token should grant
5. [Optional] You may also set an expiry date for the token if you wish
6. Press "Create token"

Launchpad will generate a token and show it to you: note that Launchpad
only stores a hash of the token for verification and not the token
itself, so you must make a copy of the token at this point as Launchpad
will not be able to show it to you again.

Via API
^^^^^^^

Alternatively, you can generate access tokens using the :ref:`Launchpad
API <launchpad-api>`, as follows:

::

   # The path argument should be the clone URL for your repository or project, without the
   # leading "https://git.launchpad.net/".  For example, if you want to
   # generate a token for https://git.launchpad.net/~user/example-project, use
   # path="~user/example-project".
   >>> repository = lp.git_repositories.getByPath(path="...")
   # Generate a pull-only token:
   >>> repository.issueAccessToken(description="pull token", scopes=["repository:pull"])
   # Generate a push-only token:
   >>> repository.issueAccessToken(description="push token", scopes=["repository:push"])
   # Generate a token that can either pull or push:
   >>> repository.issueAccessToken(description="pull/push token", scopes=["repository:pull", "repository:push"])

Similarly, to create a project access token:

::

   >>> project = lp.load("<name of project>")
   # Generate a token that can either pull or push:
   >>> project.issueAccessToken(description="pull/push token", scopes=["repository:pull", "repository:push"])

Using access tokens
~~~~~~~~~~~~~~~~~~~

You can use access tokens as HTTPS passwords, in conjunction with your
Launchpad username. For one-off testing you can just enter these when
``git`` prompts you to do so. However, if you're using them more
seriously then you will probably want to store them somewhere; for that,
see the advice from "Pro Git" on `credential
storage <https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage>`__.

Revoking access tokens
~~~~~~~~~~~~~~~~~~~~~~

Tokens can be revoked in Launchpad's web UI by anyone that can see them
listed, where a user can see a token listed if they are the direct or
indirect (through team membership) owners of the token, or if they are
the direct or indirect owners of the git repository/project. Owners of
the git repository/project can see all its tokens.

.. _linking-to-bugs:

Linking to bugs
---------------

Git-based merge proposals can be linked to Launchpad bugs. This can be
done manually from the web UI for the merge proposal, but normally you
should just mention the Launchpad bug in the commit message of one of
the commits you want to merge. The required commit message text to link
to bugs #XXX and #YYY looks like this:

::

   LP: #XXX, #YYY

Technically, the commit message needs to match this regular expression,
case-insensitively:

::

   /lp:\s+\#\d+(?:,\s*\#\d+)*/

This is the same pattern used to match Launchpad bug references in
``debian/changelog`` files in source packages.

Bugs are not automatically closed when merge proposals land, because the
policy for when that should happen varies from project to project: for
example, projects often only close bugs when they make releases, or when
their code is deployed to production sites.

Users familiar with Bazaar on Launchpad should note that the model for
Git bug linking is slightly different: bugs are linked to merge
proposals rather than to individual branches. This difference is mainly
because individual branches within a Git repository are often much more
ephemeral than Bazaar branches.

If you need a more advanced bug-handling workflow for your project, you
can use a :ref:`webhook <webhooks>` to help. See
`kicad-git-hook <https://git.launchpad.net/kicad-git-hook>`_ for an
example contributed by a Launchpad user.

Mirroring repositories from other sites
---------------------------------------

You can tell Launchpad to create a repository which is imported from
some other site. There are two ways to set this up.

1. This method is preferred in the common case of importing the upstream
   repository for a project.

   -  Go to the main page in Launchpad for a project you maintain, and
      follow the "Code" link under "Configuration options".
   -  Set "Version control system" to "Git" if necessary.
   -  Select "Import a Git repository hosted somewhere else".
   -  Fill in the repository name (this should normally just be the
      project name).
   -  Set the repository owner if necessary (defaults to you, can be any
      public team you participate in).
   -  Fill in the URL of the remote repository.
   -  Launchpad will create the repository, set it as the default for
      your project, and schedule an import.

2. This method is useful for other cases, such as importing repositories
   that are not the primary upstream repository for a project.

   -  Go to the `Request a code import <https://code.launchpad.net/+code-imports/+new>`_ page.
   -  Select "Git" for both the version control system and the target
      version control system.
   -  Fill in the other details as above.
   -  Launchpad will create the repository and schedule an import, but
      in this case it will **not** set it as the default for your
      project.

In either case, Launchpad will mirror the whole repository from the
remote site, and will keep its copy up to date regularly. You won't be
able to push directly to the imported repository on Launchpad, but you
can create another repository in the same project and push branches to
that, and even create merge proposals if you want (though you may have
to tell the upstream maintainer about them separately!). You can create
source package recipes or Snap packages based on branches in the
imported repository.

Please note that Launchpad can only mirror public repositories.

Converting from Bazaar to Git
-----------------------------

There are useful recommendations from `launchpad team members <https://jugmac00.github.io/blog/migrate-a-repository-from-bazaar-to-git/>`_ 
and `other sources <https://astrofloyd.wordpress.com/2012/09/06/convert-bzr-to-git/>`_ 
for how to convert from Bazaar to Git. Here's one way that preserves tags and 
does a pretty good job for relatively simple Bazaar branches.

::

   $ cd /some/place  # parent directory of Bazaar branch
   $ mkdir new-git-repo
   $ cd new-git-repo
   $ git init .
   $ bzr fast-export --export-marks=../marks.bzr ../old-bzr-branch | git fast-import --export-marks=../marks.git
   $ git checkout master

Now the ``new-git-repo`` directory is a Git repository with history
equivalent to your old Bazaar branch. You should push it somewhere, and
to ensure that everything is correct you should re-clone it locally to
whatever final destination path you want to work in.

If you have several different Bazaar branches that form part of the same
project, or if your Bazaar branches constitute packaging for a project
whose upstream is in revision control elsewhere, then you may well want
to do a more careful conversion. For this,
`reposurgeon <http://www.catb.org/~esr/reposurgeon/>`_ is an excellent
tool: it gives you a language for describing the transformations you
want to make to your input branches, so you can run the migration
several times with different tweaks before deciding that the result is
the one you want to publish to the world.

Once you're ready to use Git by default for your project, you can
configure this from ``https://launchpad.net/PROJECT/+configure-code`` (which
is linked from the "Configuration Progress" section of the main project
page on Launchpad).

Deleting a Git repository
-------------------------

In order to delete a Git repository, you need to follow these steps:

- go to the project
- scroll down to the "Code" section
- click on repository listed as "lp:"
- on the right hand side click on "Delete repository"
- confirm the deletion on the next page

As an alternative you can also use "lp-shell" to delete the repository:

::

   lp.load('path to repository').lp_delete()
