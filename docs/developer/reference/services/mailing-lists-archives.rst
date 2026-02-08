Launchpad public mailing lists archives
=======================================

Short description
-----------------

The Launchpad mailing list hosting service was shut down in October 2025. The
archives of the public mailing lists that existed at that time have been made
available for backup and preservation.

Detailed description
--------------------

Launchpad mailing lists were built on top of the Mailman 2.x application, which
provided an archive for each mailing list. To facilitate backup and
preservation, we have hosted a copy of the public Launchpad mailing lists'
archives at https://archive.lists.launchpad.net.

These files are hosted in a Swift bucket in the Canonical ProdStack 6
environment and served by the IS content-cache charm setup in the Canonical
ProdStack 5 cloud.

All valid https://lists.launchpad.net public mailing lists' links will redirect
automatically to the same URL on the archive site for easy access.

Troubleshooting
---------------

The IS team owns the ProdStack 6 Swift bucket that contains the static archives
and can help with providing read-write credentials to the bucket, if necessary.

The content-cache configuration for this setup is in the ``lp:canonical-mojo-specs``
repository in the ``is-content-cache/production/sites.yaml`` file (this is
Canonical-internal).
