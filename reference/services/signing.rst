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
https://lp-signing.readthedocs.io/

Git repository
--------------
https://git.launchpad.net/lp-signing

Bug tracker
-----------
https://bugs.launchpad.net/lp-signing

Deployment
----------
* `lp-signing charm <https://charmhub.io/lp-signing>`_
* `Mojo spec <https://git.launchpad.net/launchpad-mojo-specs/tree/lp-signing/>`_
* `Deploying lp-signing <https://lp-signing.readthedocs.io/en/latest/how-to/deployment.html>`_

Related specifications
----------------------
`Launchpad signing service <https://docs.google.com/document/d/1kCUUVFb1m0-Uo81tHFyYJCxysquMbKgJDMOSF63NWFc>`_

Log files
---------
See https://wiki.canonical.com/Launchpad/FreshLogs.

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
`Launchpad services diagram <https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=14glVH8XSJX-2FxTRWny#G1j-yk3c4mzYfMC79Y-uo9__u93pLWkiMi>`_
