How to use Soyuz locally
========================

.. include:: ../includes/important_not_revised.rst

You're going to run Soyuz in a branch you create for the purpose.  To get the whole experience, you'll also be installing the builder-side ``launchpad-buildd`` package on your system.

Initial setup
-------------

    * Run ``utilities/start-dev-soyuz.sh`` to ensure that some Soyuz-related services are running.  Some of these may already be running, in which case you'll get some failures that are probably harmless.  Note: these services eat lots of memory.
    * Once you've set up your test database, run ``utilities/soyuz-sampledata-setup.py -e you@example.com`` (where ''you@example.com'' should be an email address you own and have a GPG key for).  This prepares more suitable sample data in the ``launchpad_dev`` database, including recent Ubuntu series.  If you get a "duplicate key" error, ``make schema`` and run again.
    * `make run` (or if you also want to use codehosting, `make run_codehosting`—some services may fail to start up because you already started them, but it shouldn't be a problem).
    * Open https://launchpad.test/~ppa-user/+archive/test-ppa in a browser to get to your pre-made testing PPA.  Log in with your own email address and password ''test''. This user has your GPG key associated, has signed the Ubuntu Code of Conduct, and is a member ``ubuntu-team`` (conferring upload rights to the primary archive).


Extra PPA dependencies
^^^^^^^^^^^^^^^^^^^^^^

The testing PPA has an external dependency on Lucid.  If that's not enough, or not what you want:

    * Log in as `admin@canonical.com:test` (I suggest using a different browser so you don't break up your ongoing session).
    * Open https://launchpad.test/~ppa-user/+archive/test-ppa/+admin
    * Edit external dependencies.  They normally look like:

    .. code-block:: sh

        deb http://archive.ubuntu.com/ubuntu %(series)s main restricted universe multiverse


Set up a builder
----------------

Set up for development
^^^^^^^^^^^^^^^^^^^^^^

If you are intending to do any development on ``launchpad-buildd`` or similar, you possibly want :doc:`develop-with-buildd`.

Installation
^^^^^^^^^^^^

 * Create a new focal virtual-machine with ``kvm`` (recommended), or alternatively a focal ``lxc`` container. If using lxc, set ``lxc.aa_profile = unconfined`` in  ``/var/lib/lxc/container-name/config`` which is required to disable ``AppArmor`` support.

If you are running Launchpad in a container, you will more than likely want your VMs network bridged on ``lxcbr0``.

In your builder VM/lxc:

.. code-block:: sh

    $ sudo apt-add-repository ppa:launchpad/buildd-staging
    $ sudo apt-get update
    $ sudo apt-get install launchpad-buildd bzr-builder quilt binfmt-support qemu-user-static

Alternatively, launchpad-buildd can be built from ``lp:launchpad-buildd`` with ``dpkg-buildpackage -b``.

 * Edit ``/etc/launchpad-buildd/default`` and make sure ``ntphost`` points to an existing NTP server. You can check the `NTP server pool <http://www.pool.ntp.org/>`_ to find one near you.

To run the builder by default, you should make sure that other hosts on the Internet cannot send requests to it!  Then:

.. code-block:: sh

 $ echo RUN_NETWORK_REQUESTS_AS_ROOT=yes > /etc/default/launchpad-buildd

Launchpad Configuration
^^^^^^^^^^^^^^^^^^^^^^^

From your host system:

 * Get an Ubuntu ``buildd chroot`` from Launchpad, using ``manage-chroot`` from ``https://code.launchpad.net/+branch/ubuntu-archive-tools|lp:ubuntu-archive-tools``:
 * ``manage-chroot -s precise -a i386 get``
 * ``LP_DISABLE_SSL_CERTIFICATE_VALIDATION=1 manage-chroot -l dev -s precise -a i386 -f chroot-ubuntu-precise-i386.tar.bz2 set``
 * Register a new builder with the URL pointed to ``http://YOUR-BUILDER-IP:8221/`` (https://launchpad.test/builders/+new)

Shortly thereafter, the new builder should report a successful status of 'idle'.

If you want to test just the builder without a Launchpad instance, then, instead of using ``manage-chroot -l dev set``, you can copy the ``chroot`` tarball to ``/home/buildd/filecache-default/``; the base name of the file should be its ``sha1sum``.  You'll need to copy any other needed files (e.g. source packages) into the cache in the same way.  You can then send XML-RPC instructions to the builder as below.

Drive builder through RPC
-------------------------

With librarian running, fire up a ``python3`` shell and:

.. code-block:: python

    from xmlrpc.client import ServerProxy
    proxy = ServerProxy('http://localhost:8221/rpc')
    proxy.ensurepresent('d267a7b39544795f0e98d00c3cf7862045311464', 'http://launchpad.test:58080/93/chroot-ubuntu-lucid-i386.tar.bz2', '', '')
    proxy.build('1-1', 'translation-templates', 'd267a7b39544795f0e98d00c3cf7862045311464', {},
    {'archives': ['deb http://archive.ubuntu.com/ubuntu/ lucid main'], 'branch_url': '/home/buildd/gimp-2.6.8'})
    proxy.status()
    proxy.clean() # Clean up if it failed

You may have to calculate a new ``sha1sum`` of the ``chroot`` file.

Upload a source to the PPA
--------------------------

    * Run ``scripts/process-upload.py /var/tmp/txpkgupload`` (creates hierarchy) 
    * Add to ``~/.dput.cf``:

    .. code-block:: yaml

        [lpdev]
        fqdn = ppa.launchpad.test:2121
        method = ftp
        incoming = %(lpdev)s
        login = anonymous

    * Find a source package ``some_source`` with a changes file ``some_source.changes``
    * ``dput -u lpdev:~ppa-user/test-ppa/ubuntu some_source.changes``
    * ``scripts/process-upload.py /var/tmp/txpkgupload -C absolutely-anything -vvv # Accept the source upload.``
    * If this is your first time running soyuz locally, you'll also need to publish ubuntu: ``scripts/publish-distro.py -C``
    * Within five seconds of upload acceptance, the buildd should start building. Wait until it is complete (the build page will say "Uploading build").
    * ``scripts/process-upload.py -vvv --builds -C buildd /var/tmp/builddmaster # Process the build upload.``
    * ``scripts/process-accepted.py -vv --ppa ubuntu # Create publishings for the binaries.``
    * ``scripts/publish-distro.py -vv --ppa # Publish the source and binaries.``
    * Note that private archive builds will not be dispatched until their source is published.

Build an OCI image
------------------

    * Using Launchpad interface, create a new OCI project and a recipe for it.
    * On the OCI Recipe page, click on "Request builds", and select which architectures should be built on the following screen.
    * Once you have requested a build, you should run ``./cronscripts/process-job-source.py -v IOCIRecipeRequestBuildsJobSource`` to create builds for that build request.
    * If you have builders idle, this should start the build. Make sure to have run ``utilities/start-dev-soyuz.sh``, and check builders status at ``/builders`` page.
    * Once the build finishes, run ``./scripts/process-upload.py -M --builds /var/tmp/builddmaster/`` on Launchpad to make it collect the built layers and manifests.
    * At this point, in each build page you should have the files listed.
    * You can upload the built image to registry by running ``./cronscripts/process-job-source.py -v IOCIRegistryUploadJobSource`` in Launchpad. You can manage the push rules at OCI recipe's page, clicking at "Edit push rules" button.

Dealing with the primary archive
--------------------------------

    * ``dput lpdev:ubuntu some_source.changes``
    * ``scripts/process-upload.py -vvv /var/tmp/txpkgupload``
    * Watch the output -- the upload might end up in NEW.
    * If it does, go to the queue and accept it. 
    * Your builder should now be busy. Once it finishes, the binaries might go into NEW. Accept them if required.
    * ``scripts/process-accepted.py -vv ubuntu``
    * ``scripts/publish-distro.py -vv``
    * The first time, add ``-C`` to ensure a full publication of the archive.
