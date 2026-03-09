.. meta::
   :description: Set up and use Soyuz locally for package building and testing.

How to use Soyuz locally
========================

This tutorial walks you through setting up Soyuz locally and running a build.
By the end, you will be able to dput a package to your local development
environment and build and publish it to a PPA.

Initial setup
-------------

Ensure you have Launchpad set up locally. Follow the :doc:`quickstart guide <running-quickstart>` if you
do not have it already.

Run the following steps from within the development environment.

Start the Launchpad appserver:

.. code-block:: sh

    $ make run

Ensure that Soyuz-related services are running:

.. code-block:: sh

    $ utilities/start-dev-soyuz.sh

Some services may already be running, in which case you will see failures that are probably harmless. Logs and PID files for these processes are stored under ``/var/tmp``.

.. note::

  ``txpkgupload`` currently fails to start because Launchpad requires
  PyYAML > 5.x, which is incompatible with ``txpkgupload``. While this is
  being fixed, patch the txpkgupload package to use ``safe_load`` instead of
  ``load``.

  .. code-block:: python

      # File: env/lib/python3.8/site-packages/txpkgupload/plugin.py
      # Line 136
      return cls.to_python(yaml.safe_load(stream))

Create a GPG key for the ``ubuntu`` user:

.. code-block:: sh

    $ sudo -u ubuntu gpg --full-generate-key
    $ sudo -u ubuntu gpg --list-keys

Set up the Soyuz sample data (replace ``you@example.com`` with an email address you own and have a GPG key for):

.. code-block:: sh

    $ utilities/soyuz-sampledata-setup.py -e you@example.com

This prepares sample data in the ``launchpad_dev`` database including recent Ubuntu series. If you get a "duplicate key" error, run ``make schema`` and try again.

Open your test PPA in a browser:

.. code-block:: text

    https://launchpad.test/~ppa-user/+archive/test-ppa

Log in with your email address and password ``test``. This user has your GPG key associated, has signed the Ubuntu Code of Conduct, and is a member of ``ubuntu-team`` (conferring upload rights to the primary archive).


Extra PPA dependencies
~~~~~~~~~~~~~~~~~~~~~~

The testing PPA has an external dependency.  If that's not enough, or not what you want:

* Log in as `admin@canonical.com:test` (I suggest using a different browser so you don't break up your ongoing session).
* Open https://launchpad.test/~ppa-user/+archive/test-ppa/+admin
* Edit external dependencies.  They normally look like:

.. code-block:: sh

    deb http://archive.ubuntu.com/ubuntu %(series)s main restricted universe multiverse


Set up a builder
~~~~~~~~~~~~~~~~

Follow setup part in :doc:`develop-with-buildd` to set up ``launchpad-buildd``
locally. 


.. note::
    If using a lxc container, set ``lxc.aa_profile = unconfined`` in  
    ``/var/lib/lxc/container-name/config`` which is required to disable 
    ``AppArmor`` support.

    If you are running Launchpad in a container, you will more than likely want 
    your VMs network bridged on ``lxcbr0``. 

In your builder VM/lxc, you need a few more additional packages:

.. code-block:: sh

    $ sudo apt-add-repository ppa:launchpad/buildd-staging
    $ sudo apt-get update
    $ sudo apt-get install bzr-builder quilt binfmt-support qemu-user-static

To run the builder by default, you should make sure that other hosts on the 
Internet cannot send requests to it!  Then:

.. code-block:: sh

 $ echo RUN_NETWORK_REQUESTS_AS_ROOT=yes | sudo tee /etc/default/launchpad-buildd
 $ sudo systemctl restart launchpad-buildd

Registering the builder
~~~~~~~~~~~~~~~~~~~~~~~

The buildd that you have just installed needs registering with Launchpad so that builds can be dispatched to it.

1. Go to https://launchpad.test/builders and login using the ``admin@canonical.com`` admin user.

2. Press ``Register a new build machine``.

3. Fill in the details:

   - URL: ``http://<buildd-ip>:8221``
   - Builder type: Choose between:
     
     - *Virtualized* (similar to production): Automatically resets VMs after each build
     - *Non-virtualized* (simpler for local development): Non-virtualized builders are simpler but require careful security (no untrusted code)
   
   For local development, chose ``non-virtualized`` builder.

4. Change the builder from ``manual`` to ``auto`` mode via the UI.

5. After 30 seconds, the builder status should be ``Idle``. Refresh the page (it does not auto-update).

Launchpad configuration
~~~~~~~~~~~~~~~~~~~~~~~

.. _configuring-launchpad:

You need to make some changes on the Launchpad appserver to enable builds.

Change https://launchpad.test/ubuntu/+pubconf as admin from ``http://archive.launchpad.test`` to ``http://archive.ubuntu.com``.

In ``launchpad/launchpad/configs/development/launchpad-lazr.conf``, set the following configuration to point builders to your local environment:

.. code-block:: ini

    git_browse_root = http://git.launchpad.test:9419/
    git_ssh_root = git+ssh://git.launchpad.test:9422/
    builder_proxy_host = none
    builder_proxy_port = none

In ``launchpad/launchpad/lib/lp/services/config/schema-lazr.conf``, add OCI credential keys under the ``[oci]`` tag (example values):

.. code-block:: ini

    registry_secrets_private_key = U6mw5MTwo+7F+t86ogCw+GXjcoOJfK1f9G/khlqhXc4=
    registry_secrets_public_key = ijkzQTuYOIbAV9F5gF0loKNG/bU9kCCsCulYeoONXDI=

Setting up chroots
~~~~~~~~~~~~~~~~~~

Get an Ubuntu ``buildd chroot`` from Launchpad using ``manage-chroot`` from `lp:ubuntu-archive-tools <https://code.launchpad.net/~launchpad-dev/ubuntu-archive-tools/>`_:

.. code-block:: sh

    $ manage-chroot -s noble -a amd64 -i chroot get
    $ LP_DISABLE_SSL_CERTIFICATE_VALIDATION=1 manage-chroot -l dev -s noble -a amd64 -i chroot -f livecd.ubuntu-base.rootfs.tar.gz set


User setup
----------

Add your user to the correct groups so you can interact without being logged in as admin:

1. Log in as ``admin@canonical.com:test``
2. Go to https://launchpad.test/~launchpad-buildd-admins and add your user
3. Go to https://launchpad.test/~ubuntu-team and add your user


Upload a source to the PPA
--------------------------

First, set up the upload directory and configure dput:

.. code-block:: sh

    $ scripts/process-upload.py /var/tmp/txpkgupload

Add the ``lpdev`` configuration to ``~/.dput.cf``:

.. code-block:: ini

    [lpdev]
    fqdn = ppa.launchpad.test:2121
    method = ftp
    incoming = %(lpdev)s
    login = anonymous

Upload your source package:

.. code-block:: sh

    $ dput -u lpdev:~ppa-user/test-ppa/ubuntu some_source.changes

Accept the source upload in the processing queue:

.. code-block:: sh

    $ scripts/process-upload.py /var/tmp/txpkgupload -C absolutely-anything -vvv

If this is your first time building with Soyuz locally, publish the ubuntu archive:

.. code-block:: sh

    $ scripts/publish-distro.py -C

The builder should start building within five seconds. Wait until the build page shows "Uploading build", then process the completed build:

.. code-block:: sh

    $ scripts/process-upload.py -vvv --builds -C buildd /var/tmp/builddmaster

Create publishings for the binaries:

.. code-block:: sh

    $ scripts/process-accepted.py -vv --ppa ubuntu

Publish the source and binaries:

.. code-block:: sh

    $ scripts/publish-distro.py -vv --ppa

.. note::

    Private archive builds will not be dispatched until their source is published.

Build an OCI image
------------------

Using the Launchpad interface, create a new OCI project and recipe. Once you have requested a build, create the actual build jobs:

.. code-block:: sh

    $ ./cronscripts/process-job-source.py -v IOCIRecipeRequestBuildsJobSource

If you have idle builders, the build should start. Make sure ``utilities/start-dev-soyuz.sh`` has run and check the builders status at the ``/builders`` page on Launchpad.

Once the build finishes, collect the built layers and manifests:

.. code-block:: sh

    $ ./scripts/process-upload.py -M --builds /var/tmp/builddmaster/

At this point, each build page should display the built files. To upload the built image to a registry, run:

.. code-block:: sh

    $ ./cronscripts/process-job-source.py -v IOCIRegistryUploadJobSource

You can manage the push rules via the ``Edit push rules`` button on the OCI recipe page.


Dealing with the primary archive
--------------------------------

Upload your source package to the primary archive:

.. code-block:: sh

    $ dput lpdev:ubuntu some_source.changes

Process the upload:

.. code-block:: sh

    $ scripts/process-upload.py -vvv /var/tmp/txpkgupload

Watch the output — the upload might end up in NEW. If it does, go to the queue and accept it. Your builder should then start building. Once finished, the binaries might go into NEW as well. Accept them if required.

Create publishings for accepted packages:

.. code-block:: sh

    $ scripts/process-accepted.py -vv ubuntu

Publish the distro:

.. code-block:: sh

    $ scripts/publish-distro.py -vv

On the first run, add ``-C`` to ensure a full publication of the archive:

.. code-block:: sh

    $ scripts/publish-distro.py -vv -C
