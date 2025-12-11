Signing service
===============

Short description
-----------------
A service for storing keys and signing messages.

Detailed description
--------------------
The signing service provides Launchpad with a way to sign important objects
such as boot loaders, kernel images, kernel modules, or archive metadata,
while isolating private keys so that other components of Launchpad cannot
read them directly.

It exposes authenticated and encrypted HTTP interfaces for generating keys,
injecting keys that were generated elsewhere, and signing data.

It is used both by Launchpad itself and by some other services within
Canonical, such as the Snap Models Service.

Documentation
-------------
`Official documentation <https://lp-signing.readthedocs.io/>`_

Git repository
--------------
`Main repository <https://git.launchpad.net/lp-signing>`_

Bug tracker
-----------
`Bug tracker <https://bugs.launchpad.net/lp-signing>`_

Deployment
----------
* `lp-signing charm <https://charmhub.io/lp-signing>`_
* `Mojo spec <https://git.launchpad.net/launchpad-mojo-specs/tree/lp-signing/>`_
* `Deploying lp-signing <https://lp-signing.readthedocs.io/en/latest/how-to/deployment.html>`_

Related specifications (only accessible for Canonical employees)
----------------------------------------------------------------
`Launchpad signing service <https://docs.google.com/document/d/1kCUUVFb1m0-Uo81tHFyYJCxysquMbKgJDMOSF63NWFc>`_

Log files
---------
See `Reading Launchpad logs via rsync <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/reference/reading-launchpad-logs-via-rsync/>`_.

Production
~~~~~~~~~~

* ``rless il3-signing1.lp.internal::lp-signing-gunicorn-logs/gunicorn.log``
* ``rless il3-signing2.lp.internal::lp-signing-gunicorn-logs/gunicorn.log``

Staging
~~~~~~~

* ``rless 10.132.60.12::lp-signing-gunicorn-logs/gunicorn.log``
* ``rless 10.132.60.220::lp-signing-gunicorn-logs/gunicorn.log``

Common support cases
--------------------
..
  XXX: https://warthogs.atlassian.net/browse/LP-1323: add documentation for enrolling a new client

More information
----------------
`Launchpad services diagram <https://app.diagrams.net/?src=about#Uhttps%3A%2F%2Fgit.launchpad.net%2Flaunchpad%2Fplain%2Fdoc%2Fdiagrams%2Farchitecture.html#%7B%22pageId%22%3A%2214glVH8XSJX-2FxTRWny%22%7D>`_
