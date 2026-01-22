Launchpad Code Hosting
======================

.. include:: ../../includes/important_not_revised.rst

Launchpad hosts source code using `Git <https://git-scm.com/>`__ branches. 
However dealing with code in Launchpad covers many more areas than just hosting
branches.

Code for the web application is only part of the Launchpad codehosting
system. The major sub-systems are:

-  The `git` client (which is not a part of Launchpad but its behaviour is 
   important to us).
-  Connectivity to Launchpad (git, git+ssh, and https for Git)
-  Hosting infrastructure
-  The underlying object model
-  The web application
-  Email processing
-  Code imports from git 
-  Branch source code browser (`cgit <https://git.zx2c4.com/cgit/>`__
   for Git)
-  Source package recipes (`git-build-recipe` integration with 
   :ref:`Soyuz <use-soyuz-locally>`)

Each of these subsystems also have multiple moving parts and some have
other asynchronous jobs associated with them.

The `codehosting overview diagram :attachment:../images/codehosting.png`
summarises how some of these systems interact.

You can `run the codehosting system locally <https://turnip.readthedocs.io/en/latest/development.html>`_

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

Hosting infrastructure
----------------------

This really groups together the bits around what happens once we have a
branch that a user has pushed to us, and the associated jobs that get
kicked off.

'''Parts [and responsibilities] '''

-  scanner

   -  revision email jobs

-  scalability concerns - efficient storage and responsiveness [shared
   with LOSAs]

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
other systems as git branches. This also supports mirroring Git repositories 
from elsewhere into Git repositories in Launchpad.

-  code import jobs
-  integration of import tools

Git repository source code browser (cgit)
-----------------------------------------

Launchpad uses `cgit <https://git.zx2c4.com/cgit/>`__ to provide a web
view of the repository contents. We use an unmodified package of
\`cgit`; Launchpad's customisations are in
`turnip.pack.http <https://git.launchpad.net/turnip/tree/turnip/pack/http.py>`__.

Source package recipes
----------------------

Check out the :ref:`source builds explanation <source-build-recipes>` for more
details on what recipes are.