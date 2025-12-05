Ubuntu archive publisher
========================

The Ubuntu archive publisher updates the archive on disk
and places new uploads into the archive periodically. It then supersedes
older versions of the same package or deletes them
in a process called domination. Finally it generates the index files
``Sources``, ``Packages`` and ``Release`` which are consumed by clients
like ``apt``.

The publisher for the Ubuntu archive is separated into five distinct steps
which will now be discussed in detail.


Step A: Publishing
------------------

The publisher collects all package publishing history entries
which are marked as ``PENDING`` or ``PUBLISHED`` and that are not
yet published. These entries were previously created
by the ``process-accepted`` script.

The files are then added to the diskpool either by
adding the file directly or by using a symlink if the necessary
files are already present in another component or pocket.

Step A2: Marking pockets with deletions as dirty
------------------------------------------------

After all new packages are published successfully,
all suites with package publishing history entries
with status ``DELETED`` are marked
as dirty as an intermediate step.

This ensures that domination (Step B) will run on these suites
and all deleted packages are scheduled for deletion.


Step B: Judge and dominate
--------------------------

The ``judge`` and ``dominate`` processes mark older versions of newly published
packages as superseded or prepare them for deletion. The final deletion is handled by
a separate process called ``process-deathrow``.

Domination
~~~~~~~~~~

Domination is the procedure used to identify and
supersede all old versions for a given publication,
source and binary, inside a suite.

Binary packages are dominated in two passes, the first
tries to supersede architecture-dependent publications; the
second tries to supersede architecture-independent ones.
An architecture-independent publication is kept alive as long as any
architecture-dependent publications from the same source package build
are still live for any architecture, because they may depend
on the architecture-independent package.

For source packages only the latest version stays live, while
all older publications are marked as superseded by the respective
oldest live releases that are newer than the superseded ones.

Judging
~~~~~~~

The dominator also processes the superseded publications and marks the ones with
unnecessary files as 'eligible for removal', meaning a ``SUPERSEDED``
or ``DELETED`` publication status and a defined ``scheduleddeletiondate``,
which will then be considered for archive removal by the deathrow processing.

In order to judge if a source is 'eligible for removal' it also checks
if its resulting binaries are still required in the archive, i.e.,
old binary publications can (and should) hold their respective sources in the archive.


Step C: Generate Sources and Packages
-------------------------------------

The publisher uses ``apt-ftparchive`` to generate all necessary index
files and checksums for the archive on the diskpool.
Clients like ``apt`` use these index files to access a
distribution source.


Step D: Write out Release files
-------------------------------

The publisher generates the Release files for each suite (distribution series and pocket).
This involves collecting all index files generated in the previous step and
``Contents`` files.

A ``Release`` file is created containing metadata about the suite (Origin, Label,
Codename, etc.) and checksums for all collected files. If the archive is configured
for signing, the publisher also generates ``Release.gpg`` and ``InRelease`` signatures.

Finally, if enabled for the series, the publisher updates the by-hash directory
structure to support hash-based retrieval of index files, and synchronizes timestamps
across core files.