Launchpad public mailing lists archives
=======================================

Short description
-----------------

The Launchpad mailing lists hosting service was shut down in October 2025 and
the static archives of the public mailing lists that existed at that time have
been made available for backup and archiva.

Detailed description
--------------------

Launchpad mailing lists were built on top of the Mailman 2.x application and
that provided static archives for all the mailing lists on Launchpad. To
facilitate backup and archival, we have set up an archive of the public
Launchpad mailing lists archives that existed at the time of the shut down in
October 2025. These archives are available at https://archive.lists.launchpad.net.

Since the mailing list hosting service has been shut down, these archives are
hosted in a Swift bucket in the Canonical ProdStack 6 environment and fronted
by the IS content-cache charm setup in the Canonical ProdStack 5 cloud.

The https://lists.launchpad.net links for these public mailing lists will
redirect automatically to the same URL on the archive site for easy access.

Troubleshooting
---------------

The IS team owns the ProdStack 6 Swift bucket that contains the static archives
and can help with providing read-write credentials to the bucket, if necessary.

The content-cache configuration for this setup is in the ``lp:canonical-mojo-specs``
repository in the ``is-content-cache/production/sites.yaml`` file (this is
Canonical-internal).
