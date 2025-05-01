~- `Launchpad Help <FrontPage>`__ > `Packaging <Packaging>`__ >
`PPAs <PPA>`__ > Deleting packages -~

Package deletion
================

You can delete any package from your PPA. However, it can take some time
before the package is removed from the listing on your PPA overview page
and the reported size of your archive is adjusted.

The deletion page allows you to schedule packages for deletion. To do
this, search first for the desired packages, select one or more of them,
input a comment, and request deletion. Deletion will affect the source
selected and any binary packages built from it.

Deletion marks the packages as deleted in the UI, but they are actually
removed from your PPA in separate steps:

:literal:`Archive`   ``indexes:`` A deleted package disappears from the archive indexes in at most 20 minutes. As soon as this happens, users will no longer be able to install it via apt.

:literal:`Files`   ``on``   ``disk:`` A file will be removed from the archive disk pool only when all packages referencing it have been scheduled for deletion. This includes packages published in other series, or multiple package versions referring to the same original upstream tarball.

The job that removes files from disk runs every six hours. It may take
some time to remove a file from disk, depending on the number of
packages referencing it.

.. note::
    Launchpad retains a copy of deleted files for up to seven days
    after you delete it from the archive. Follow the individual file links
    in the package's *Built packages* section.

The easiest alternative to replace a broken source is always to upload a
package with a higher version number and let the system automatically
supersede and remove the older version. You should not attempt to use
deletion requests to re-upload the same source version with different
contents, as this is still prevented even after the content has been
deleted.