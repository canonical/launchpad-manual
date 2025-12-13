Launchpad Code Hosting
======================

.. include:: ../../includes/important_not_revised.rst

Launchpad hosts source code using `Git <https://git-scm.com/>`__ and
`Bazaar <https://www.breezy-vcs.org/>`__ branches. However dealing
with code in Launchpad covers many more areas than just hosting
branches.

Code for the web application is only part of the Launchpad codehosting
system. The major sub-systems are:

-  The `git` and `bzr` / `brz` clients (neither of which is part of
   Launchpad, but their behaviours are important to us)
-  Connectivity to Launchpad (git, git+ssh, and https for Git; SFTP and
   bzr+ssh for Bazaar)
-  Hosting infrastructure
-  The underlying object model
-  The web application
-  Email processing
-  Code imports (from CVS, Subversion, git and Mercurial)
-  Branch source code browser (`cgit <https://git.zx2c4.com/cgit/>`__
   for Git; :doc:`loggerhead <../how-to/land-update-for-loggerhead>` for Bazaar)
-  Source package recipes (`git-build-recipe`/`bzr-builder\` integration
   with :doc:`Soyuz ../how-to/use-soyuz-locally`)

Each of these subsystems also have multiple moving parts and some have
other asynchronous jobs associated with them.

The `codehosting overview diagram :attachment:../images/codehosting.png`
summarises how some of these systems interact.

You can :doc:`run the codehosting system locally <../how-to/codehosting-locally>`.

We no longer put significant effort into bzr hosting beyond making sure
it remains functional. The future of bzr is
`Breezy <https://www.breezy-vcs.org/>`__; Launchpad has migrated to it
for code hosting, and will migrate to it for code imports in due course.

The bzr/brz client
------------------

This is what users install on their systems to use Bazaar. The bzr
application is also installed on the server side for Launchpad to use to
access the information in the Bazaar branches.

'''Parts [and responsibilities] '''

-  bzr/brz client [maintained by the
   `Breezy <https://www.breezy-vcs.org/>`__ community]
-  bzr.plugins.launchpad [shared with the
   `Breezy <https://www.breezy-vcs.org/>`__ team]
-  server side of lp name resolution

Connectivity to Launchpad
-------------------------

Git
~~~

\`turnip\` implements several frontends for different transports.

**Parts [and responsibilities]**

-  haproxy configuration (encoded in the
   https://git.launchpad.net/launchpad-mojo-specs/tree/mojo-lp-git/services)
-  frontends (`turnip-pack-frontend-git`, \`turnip-pack-frontend-ssh`,
   \`turnip-pack-frontend-http`)
-  \`turnip-pack-virt\` for path virtualisation (translating from the
   URL path namespace to physical storage on disk)
-  \`turnip-pack-backend\` for backend storage, calling out to \`git
   upload-pack\` and \`git receive-pack\` to do most of the hard work
-  \`nfs-ganesha\` to allow horizontally scaling \`turnip\`
-  git hooks which call out to Launchpad, for e.g. push notifications or
   to check per-ref permissions
-  Launchpad's XML-RPC interfaces in \`lp.code.xmlrpc.git\`

Bazaar
~~~~~~

Connecting to the code hosting system from the outside world is done
either through SSH using SFTP or the bzr+ssh protocol, or through HTTP.
Apache handles the HTTP routing using a number of mod-rewrite rules.

'''Parts [and responsibilities] '''

-  HTTP Apache configuration [shared with LOSAs]
-  branch location rewrite script (called by mod-rewrite rule)
-  ssh server

   -  

      -  authentication
      -  SFTP implementation
      -  smart server launching

-  smart server

   -  

      -  lp-serve plugin
      -  bzr's smart server [shared with
         `Breezy <https://www.breezy-vcs.org/>`__ team]

-  codehosting transport implementations
-  codehosting interfaces on xmlrpc.lp.internal

Hosting infrastructure
----------------------

This really groups together the bits around what happens once we have a
branch that a user has pushed to us, and the associated jobs that get
kicked off.

'''Parts [and responsibilities] '''

-  puller (Bazaar only)
-  scanner

   -  

      -  revision email jobs

-  scalability concerns - efficient storage and responsiveness [shared
   with LOSAs]

   -  

      -  stacking

-  reclamation cleanup jobs
-  backup support scripts

The web application
-------------------

Code that is executed as part of the Launchpad web application. The core concepts are documented on the :ref:`Code Concepts <code-concepts>` page.

**Major features**

-  general information
-  listings for various registry objects - people, teams, projects,
   distros, packages
-  privacy
-  code reviews
-  merge management
-  branch gardening
-  linking to other launchpad apps (bugs, blueprints, rosetta (soyuz
   soon))

   -  

      -  translation jobs [rosetta team primarily responsible for this]

-  asynchronous generation of review diffs

Email processing
----------------

There is also the processing of incoming email to the code.launchpad.net
domain. Currently there are two main things are triggered with incoming
email:

-  creating a new merge proposal (an possibly a source branch) from a
   merge directive
-  processing email comments (with possible commands)

Code imports
------------

Launchpad provides a way for users to get access to source code from
other systems as Bazaar branches (from CVS, Subversion, git and
Mercurial). This also supports mirroring Git repositories from elsewhere
into Git repositories in Launchpad.

-  code import jobs
-  integration of import tools

   -  

      -  CSCVS for CVS (and legacy Subversion imports)
      -  bzr-svn and subvertpy for all new Subversion imports
      -  bzr-git and dulwich for git
      -  bzr-hg for mercurial imports

Git repository source code browser (cgit)
-----------------------------------------

Launchpad uses `cgit <https://git.zx2c4.com/cgit/>`__ to provide a web
view of the repository contents. We use an unmodified package of
\`cgit`; Launchpad's customisations are in
`turnip.pack.http <https://git.launchpad.net/turnip/tree/turnip/pack/http.py>`__.

Bazaar branch source code browser (loggerhead)
----------------------------------------------

Launchpad uses `loggerhead <https://launchpad.net/loggerhead>`__ to
provide a web view of the branch contents. We try not to have any
Launchpad specific code in loggerhead itself, but instead keep that in
the
`lp:~launchpad-pqm/loggerhead/devel <https://code.launchpad.net/~launchpad-pqm/loggerhead/devel>`__
branch.

-  loggerhead itself - community project but with major contributions
   from Canonical

See :doc:`Loggerhead for Launchpad developers <../how-to/land-update-for-loggerhead>` for details on
how to land changes to Launchpad loggerhead.

Source package recipes
----------------------

Check out the :ref:`source builds explanation <source-build-recipes>` for more
details on what recipes are.