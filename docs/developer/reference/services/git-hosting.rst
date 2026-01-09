Git hosting
===============

Description
-----------

Launchpad has direct Git hosting support. The major subsystems involved are:

* The git client
* Hosting service (turnip)
* The web application (Launchpad)
* Repository source code browser (cgit)

Git client
----------

This is what users install on their systems to use Git. 
It is also installed on the hosting backend to support the ``receive-pack`` and ``upload-pack`` protocols.

Hosting service
---------------

The outside world connects to the Git hosting service using one of several protocols:

* ``git://``
* ``git+ssh://``
* ``https://``

The Git "dumb" HTTP transport will not be supported, as it has largely been considered 
deprecated since the provision of "smart" HTTP transport in Git v1.6.6 (released January, 2010).

SSL is terminated by haproxy (haproxy has two units haproxy/1* and haproxy/0) for HTTPS, and all the other 
protocols also pass through haproxy for load balancing (although at the moment we only have a single backend).  
See the full charm configuration at `launchpad-mojo-specs <https://git.launchpad.net/launchpad-mojo-specs/tree/lp-git/bundle.yaml>`_.

The underlying protocol endpoints live in `lp:turnip <https://code.launchpad.net/turnip>`_, 
which invokes ``git upload-pack`` and ``git receive-pack`` to implement the git protocol itself.

``turnip`` also provides an internal API used by the Launchpad web application to manipulate and inspect repositories; 
and in turn the Launchpad web application provides an internal XML-RPC interface used by ``turnip`` to translate logical 
repository paths to filesystem paths and to notify Launchpad of repository changes.

``turnip`` is deployed using Juju, using the `turnip charms <https://git.launchpad.net/turnip/tree/charm>`_.  

For more details, see the `turnip documentation <https://turnip.readthedocs.io/en/latest/index.html>`_ 

The web application
-------------------

Code that is executed as part of the Launchpad web application.  Major features:

 * general information
 * listings for various registry objects - people, teams, projects, packages
 * default repositories for projects and packages
 * privacy settings

Repository source code browser
------------------------------

Launchpad uses the external `cgit <https://git.zx2c4.com/cgit/>`_ project to provide a web view of the repository contents.  
This is invoked by ``turnip`` when it receives HTTPS requests that don't correspond 
to git smart HTTP protocol, and ``turnip``` deals with configuring ``cgit`` appropriately for each repository.

Log files
---------
See `Reading Launchpad logs via rsync <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/reference/reading-launchpad-logs-via-rsync/>`_.

Production
~~~~~~~~~~

* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-access.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-api-access.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-api-error.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-pack-backend.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-pack-frontend-git.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-pack-frontend-http.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-pack-frontend-ssh.log``
* ``rless turnip-pack-{1,2,3,4}.lp.internal::turnip-logs/turnip-pack-virt.log``

Qastaging
~~~~~~~~~

* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-access.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-api-access.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-api-error.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-pack-backend.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-pack-frontend-git.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-pack-frontend-http.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-pack-frontend-ssh.log``
* ``rless turnip-pack-{1,2}.qastaging.lp.internal::turnip-logs/turnip-pack-virt.log``