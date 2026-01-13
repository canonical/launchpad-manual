Ubuntu package publishing
=========================

The Ubuntu package lifecycle describes the process from a `source package upload <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-format/#source-packages>`_
to the `Ubuntu package archive <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-archive/>`_.
This involves multiple steps in which the original source package is verified,
built into a `binary package <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-format/#binary-packages>`_
and finally published into the package archive.

Please note that this document only describes the technical steps
involved in the publishing process. It does not describe the policies
and review processes involved in accepting package changes or migrations
between suites.

Source package upload
---------------------

The first step of the publishing process is to upload a source package
with a signed source ``.changes`` file. The signed document references
and includes checksums of the source package and of the files to upload.
These files are usually uploaded with ``dput`` or ``dput-ng``, which use
FTP or SFTP to push the files to Launchpad, specifically ``upload.ubuntu.com``.

The Ubuntu upload processor (``process-upload.py``) runs periodically.
When it finds a newly uploaded source package,
it performs various checks, including:

- ensuring the signature on the changes file is valid and that the key used
  is associated with a user who has permission to upload
  to the target distribution/series/archive
- ensuring all checksums match
- confirming that it really is a source upload

..
    TODO: Create and link to librarian explainer

Once all checks pass, the script uploads the files to the librarian and
creates a queue entry (``PackageUpload``) in the database.
If any checks fail, the package upload is marked as ``REJECTED``.

If the upload is automatically accepted (e.g. for the devel series when it is not frozen),
the system immediately creates a ``PENDING`` source package publishing history
entry and creates all necessary binary package build requests for the architectures
supported by the Ubuntu series that the uploaded source package targets.
Otherwise, these are created later when the package is accepted from the queue.

Building
--------

The ``buildd-manager`` service manages the builder VMs of all
supported architectures in the Launchpad build farm by communicating with the
``launchpad-buildd`` service that runs on them.

For a binary package build, a ``launchpad-buildd`` instance is given a list
of artifacts to download from the librarian, the source package,
and the chroot to build the source package in. The VM then downloads the chroot,
unpacks it, and uses ``sbuild`` to build the package.

The ``buildd-manager`` queries all ``launchpad-buildd`` instances
regularly. Once a VM reports that a build is complete, it copies the
changes file and build artifacts (mostly debs, ddebs, and the buildinfo file)
off the builder and uploads them as a binary package.

Binary package upload
---------------------

The binary packages from the Launchpad builders
are processed by ``process-upload.py``. This script again performs
various checks such as ensuring the architecture of the built debs
matches what was expected and verifying that the checksums match.

Once all checks pass, the artifacts are copied
to the librarian and a queue entry is created.
If any checks fail the package upload is marked as ``REJECTED``.

Queue processing
----------------

Binary queue items usually go straight into the ``ACCEPTED`` state, 
but a build that introduces new binary packages goes into ``NEW``.
This occurs either because the binary package was newly accepted into
the archive or due to the package being a kernel package. Kernel packages are
always published as new binary packages with the version as a part
of the binary package name.

The ``process-accepted`` script iterates through all ``ACCEPTED``
binary queue items and creates new ``PENDING`` binary package
publishing history entries.

Publication
-----------

The archive publisher reads the set of current publication records
for a component, i.e. ``main/universe/...``, of a suite (which is a combination
of a series and a pocket like ``noble-proposed`` or ``questing-release``),
makes sure that these packages are present in the archive on the diskpool and creates
the index files to be consumed by `apt` which describe the
sources and binaries that are currently published.

Once all component/suite combinations have been published for a series,
it also generates the ``Release`` file, signs it using the appropriate signing key
and synchronises its working copy with the active archive copy.
