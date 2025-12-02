Debian package publishing
=========================

The Debian package lifecycle describes the process from a `source package upload <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-format/#source-packages>`_ to the `Ubuntu package archive <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-archive/>`_.
This involves multiple steps in which the original source package is verified, built into a `binary package <https://documentation.ubuntu.com/project/how-ubuntu-is-made/concepts/package-format/#binary-packages>`_ and finally published into the package archive.

Please note that this document is not describing the review processes involved in accepting package changes or the migrations between suites, but rather the technical steps involved in the publishing process.

#####################
Source package upload
#####################

The first step of the publishing process is to upload a source package with a signed
source ``.changes`` file. The signed document references and includes checksums of the files to upload and
the source package. These files are usually uploaded with ``dput`` or ``dput-ng``, which use
FTP or SFTP to push the files to Launchpad.

The Ubuntu upload processor (``process-upload.py``) runs every minute. When it finds a newly
uploaded source package, it performs various checks, including:

- ensuring the signature on the changes file is valid and that the key used is associated with a user who has permission to upload to the target distribution/series/archive
- ensuring all checksums match
- confirming that it really is a source upload

..
    TODO: Create and link to librarian explainer

Once all checks pass, the script uploads the files to the librarian and creates a queue entry (``PackageUpload``) in the database.

If the upload is automatically accepted (e.g. for the devel series), the system immediately creates a ``PENDING`` source package
publishing history entry and creates all necessary binary package build requests. Otherwise these are created later when the
package is accepted from the queue.

########
Building
########

The Launchpad build farm is controlled by the ``buildd-manager`` daemon, which manages multiple
``launchpad-buildd`` instances for all supported architectures.

..
    Explain chroot?

For a binary package build, a ``buildd`` instance is given a list of artifacts to download from
the librarian, the source package, and the chroot to build it in. The VM then downloads the chroot,
unpacks it, and uses ``sbuild`` to build the package.

The ``buildd-manager`` queries all ``launchpad-buildd`` instances regularly. Once a VM reports that a build
is complete, it copies the changes file and built artifacts (mostly debs, ddebs, and the buildinfo file) off the builder.

#####################
Binary package upload
#####################

The binary packages from the Launchpad builders are processed by ``process-upload.py``.
This script again performs various checks like ensuring that the architecture of the built debs matches what was expected
and verifying that the checksums match.
Once all checks pass, the artifacts are copied to the librarian and a queue entry is created.

################
Queue processing
################

Binary queue items usually go straight into the ``ACCEPTED`` state, but a build that introduces
new binary packages goes into ``NEW``.

When the publisher sees an ``ACCEPTED`` binary queue item, it creates new ``PENDING`` binary package
publishing history entries.

###########
Publication
###########

The archive publisher reads the set of current publication records for a component (i.e. main/universe/…)
of a suite (which is a combination of a series and a pocket like ``noble/proposed`` or ``questing/release``),
makes sure that these packages are present in the pool and creates the index files to be consumed by `apt` which
describe the sources and binaries that are currently published.

Once all component/suite combinations have been published for a series, it also generates the Release file, signs it and
synchronises its working copy with the active archive copy.
