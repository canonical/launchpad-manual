.. meta::
   :description: How to develop with Buildd using LXD VM.

How to develop with Buildd
==========================

This tutorial helps you set up buildd locally and run local builds via the CLI.

Set up buildd
--------------
For local buildd development, we use LXD VMs and manage them with the
standard ``lxc`` CLI.

Before continuing, make sure LXD is installed and initialized on your machine.
You can follow the official LXD getting started guide:
`https://documentation.ubuntu.com/lxd/latest/getting_started <https://documentation.ubuntu.com/lxd/latest/getting_started/>`_.


Create a LXD profile for VMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a convenience helper profile for VMs that will add users and run 
``cloud-init`` for installing the LXD VM agent. It is not required and you can 
pass the options on the ``lxc`` command.

For now, we are using the LXD provided cloud images as it has the LXD agent and
``cloud-init`` preinstalled. This requires a smaller LXD profile, but needs 
some extra commands afterwards.

To create this run:

.. code-block:: sh

    $ lxc profile create vm

and then you can setup a LXD VM profile using the following template:

.. code-block:: sh

    $ lxc profile edit vm

.. code-block:: yaml

    name: vm
    config:
      limits.cpu: "2"
      limits.memory: 4GB
      user.vendor-data: |
        #cloud-config
        package_update: true
        ssh_pwauth: yes
        packages:
          - openssh-server
          - byobu
          - language-pack-en
          - git
        users:
        - name: "ubuntu"
          groups: lxd
          shell: /bin/bash
          sudo: ALL=(ALL) NOPASSWD:ALL
          ssh-import-id: <lp username>
    config:
      raw.idmap: |
        uid <output of "id -u"> 1000
        gid <output of "id -g"> 1000
    devices:
      config:
        source: cloud-init:config
        type: disk
      eth0:
        name: eth0
        nictype: bridged
        parent: lxdbr0
        type: nic
      work:
        path: "/home/ubuntu/launchpad-buildd"
        source: <path to folder you want to share from the host>
        type: disk


Start the LXD VM
~~~~~~~~~~~~~~~~

Start the LXD VM

.. code-block:: sh
  
  $ lxc launch ubuntu:noble -p vm -p default buildd --vm

This will take a while to settle. You can monitor its progress with:

.. code-block:: sh
  
  $ lxc console build

Once it has completed running `cloud-init`, you should see an IP address assigned to the VM in
``lxc list`` and be able to execute a bash shell with 

.. code-block:: sh
  
  $ lxc exec buildd bash

Configure password and SSH
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: Ideally cloud-init should do all these, check why cloud-init is not 
.. setting this up.

This should be done by the cloud-init config in the profile, but the package is not installed at the time that is run, so do it afterwards manually:

.. code-block:: sh

    $ lxc shell buildd
    $ su ubuntu
    $ ssh-import-id <launchpad user id>


Set up Launchpad Buildd
~~~~~~~~~~~~~~~~~~~~~~~

We'll need a clone of this and then build and install it for running.

.. code-block:: sh

    $ git clone https://git.launchpad.net/launchpad-buildd


Add the staging Buildd and Launchpad PPA.

.. code-block:: sh

    $ cd launchpad-buildd
    $ sudo apt-add-repository ppa:launchpad/ubuntu/buildd-staging
    $ sudo apt-add-repository ppa:launchpad/ubuntu/ppa

We need to enable ``deb-src`` for the primary archive and the Launchpad PPA. 

.. code-block:: sh

    $ sudo vim /etc/apt/sources.list.d/launchpad-ubuntu-ppa-noble.sources
    $ sudo vim /etc/apt/sources.list.d/ubuntu.sources
    $ sudo apt update
    $ sudo apt build-dep launchpad-buildd fakeroot
    $ sudo apt install -y fakeroot
    $ sudo apt install -f

Install or run buildd
~~~~~~~~~~~~~~~~~~~~~

You have three options for running launchpad-buildd locally:

**Option 1: Install from PPA (simplest)**

Install the package directly from the PPA:

.. code-block:: sh

    $ sudo apt install launchpad-buildd

Then edit ``/etc/launchpad-buildd/default`` and change ``ntphost`` to something valid (``ntp.ubuntu.com`` should work).

Start the buildd service:

.. code-block:: sh

    $ sudo systemctl start launchpad-buildd

**Option 2: Build and install the package (for testing changes)**

Build the package from source and install it:

.. code-block:: sh

    $ cd launchpad-buildd
    $ make
    $ cd ..
    $ sudo apt install ./launchpad-buildd_260_all.deb

Then edit ``/etc/launchpad-buildd/default`` and change ``ntphost`` to something valid (``ntp.ubuntu.com`` should work).

Start the buildd service:

.. code-block:: sh

    $ sudo systemctl start launchpad-buildd

**Option 3: Run directly from source (for active development)**

Run the server directly without installing, useful for rapid development iteration:

.. code-block:: sh

    $ cd launchpad-buildd
    $ sudo mkdir -p /var/run/launchpad-buildd
    $ sudo chown ubuntu: /var/run/launchpad-buildd
    $ /usr/bin/python3 /usr/bin/twistd --no_save --pidfile /var/run/launchpad-buildd/default.pid --python /usr/lib/launchpad-buildd/buildd-slave.tac -n

Note: You still need to edit ``/etc/launchpad-buildd/default`` and set ``ntphost`` to something valid (``ntp.ubuntu.com`` should work).

Making changes
~~~~~~~~~~~~~~

To make changes to the `launchpad-buildd` code:

- If you installed `buildd` from the PPA (Option 1): Clone the repository first, make your changes, then follow Option 2 or Option 3 above.
- If you built and installed (Option 2): Make your changes, rebuild with ``make``, and reinstall the package.
- If you're running directly (Option 3): Make your changes and restart the server. This is the fastest iteration cycle for development.

Testing
-------

You probably want the next section (:ref:`Configuring Launchpad <configuring-launchpad>`) at this point, but if you are doing any buildd development and need to test your changes without having to have the whole system running, you can use the XML-RPC interface to cause builds to happen.

Getting a base image
~~~~~~~~~~~~~~~~~~~~

First, we need a base image to use for the builds. Usually, this is pulled as part of a build, but if we don't have Launchpad involved, we need to set this up manually.
To download the image we need to set up the ``ubuntu-archive-tools``.

.. code-block:: sh

    $ git clone https://git.launchpad.net/ubuntu-archive-tools
    $ sudo apt install python3-launchpadlib python3-ubuntutools

Now we can download the image. Please note that there are two types of images: ``chroot`` and ``lxd`` images.
``chroot`` backend is only used for ``binarypackagebuilds`` and ``sourcepackagerecipebuilds`` while all the other build types use an ``lxd`` image.

To download the ``lxd`` image proceed as follows:

.. code-block:: sh

    $ ./manage-chroot -s bionic -a amd64 -i lxd get 
    $ sha1sum livecd.ubuntu-base.lxd.tar.gz
    $ mv livecd.ubuntu-base.lxd.tar.gz <sha1sum from previous line>

To download a ``chroot`` image proceed as follows:

.. code-block:: sh

    $ ./manage-chroot -s bionic -a amd64 get
    $ sha1sum livecd.ubuntu-base.rootfs.tar.gz
    $ mv livecd.ubuntu-base.rootfs.tar.gz <sha1sum from previous line>
    
Now we should copy the downloaded image to the builder file cache to be picked up during the build phase if you are running your builder locally.

.. code-block:: sh
    
    $ sudo cp <sha1sum named file> /home/buildd/filecache-default
    $ sudo chown buildd: /home/buildd/filecache-default/<sha1sum named file>

Running a build locally
~~~~~~~~~~~~~~~~~~~~~~~

You can test the builder via the XML-RPC interface without a full Launchpad instance.

First, ensure you have a base image in the builder's file cache. Copy the ``chroot`` or ``lxd`` tarball to ``/home/buildd/filecache-default/`` where the filename is its ``sha1sum``:

.. code-block:: sh

    $ sudo cp <sha1sum-named-file> /home/buildd/filecache-default
    $ sudo chown buildd: /home/buildd/filecache-default/<sha1sum-named-file>

Then start a Python REPL and run:

.. code-block:: python

  from xmlrpc.client import ServerProxy
  proxy = ServerProxy("http://localhost:8221/rpc")
  
  # Check builder status
  proxy.status()
  
  # Inject a base image
  proxy.ensurepresent(
    "<sha1sum-of-base-image>", 
    "http://path-to-image/image.tar.gz", 
    "", 
    ""
  )
  
  # Run a build (using lxd backend for example)
  proxy.build(
    '1-3',
    'oci',
    '<sha1sum-of-base>',
    {},
    {
      'name': 'test-build',
      'image_type': 'lxd',
      'series': 'noble',
      'arch_tag': 'amd64',
      'git_repository': 'https://github.com/user/repo.git',
      'archives': [
        'deb http://archive.ubuntu.com/ubuntu noble main restricted',
        'deb http://archive.ubuntu.com/ubuntu noble-updates main restricted'
      ]
    }
  )
  
  # Check build status
  proxy.status()
  
  # Clean up after testing
  proxy.clean()


Running a build on qastaging
----------------------------

We can use XML-RPC to interact also with qastaging/staging builders. 
First of all, we should be able to ssh into our bastion and ssh into the ``launchpad-buildd-manager`` unit since it's the one that has the firewall rules to talk with builders.

Then we should follow the same procedure to get the correct ``sha1sum`` of a backend image.

.. code-block:: sh

    $ ./manage-chroot -s bionic -a amd64 -i lxd get 
    $ sha1sum livecd.ubuntu-base.lxd.tar.gz

We want to call the ``manage-chroot`` command to download the LXD image from our database, in this way we can compute the ``sha1sum`` on it and 
we can pass all the arguments that we need to call the ``ensurepresent`` function. The arguments that the function takes are the ``sha1sum`` hash 
of the image we want, the URL from which we retrieved the image, username and password.
At this point we should select the builder that we want to interact with. We can navigate to ``https://qastaging.launchpad.net/builders/qastaging-bos03-amd64-001`` and get the builder location.
In this example ``http://qastaging-bos03-amd64-001.vbuilder.qastaging.bos03.scalingstack:8221``

.. code-block:: python

  import xmlrpclib
  proxy = xmlrpclib.ServerProxy("http://qastaging-bos03-amd64-001.vbuilder.qastaging.bos03.scalingstack:8221/rpc")
  proxy.status()

  # Inject the backend image we retrieved before.
  proxy.ensurepresent("<sha1sum from the previous step>", "<url from the previous step>", "admin", "admin")

  # Start the build.
  proxy.build('1-3', 'snap', '<sha1sum from the previous step>', {}, {'name': 'test-build', 'image_type': 'lxd', 'series': 'bionic', 'arch_tag': 'amd64', 'git_repository': 'https://github.com/tomwardill/test-docker-repo.git', 'archives': ['deb http://archive.ubuntu.com/ubuntu bionic main restricted', 'deb http://archive.ubuntu.com/ubuntu bionic-updates main restricted', 'deb http://archive.ubuntu.com/ubuntu bionic universe']})

  # Clean the builder after a failure or a success.
  proxy.clean()

Proxy setup
-----------

If our build needs to talk with the external world we will need to set up the proxy for our builders, with the word ``proxy`` we are referring here to both builder proxy and fetch service.
First of all, we need to pull the token to authenticate our ``launchpad-buildd-manager`` against the proxy.

All these commands should be run on the ``launchpad-build-manager`` unit.

.. code-block:: python

  admin_username = <builder_proxy_auth_api_admin_username>
  admin_secret = <builder_proxy_auth_api_admin_secret>
  auth_string = f"{admin_username}:{admin_secret}".strip()
  basic_token = base64.b64encode(auth_string.encode("ASCII"))

We can retrieve ``builder_proxy_auth_api_admin_username`` and ``builder_proxy_auth_api_admin_secret`` values from the ``launchpad-buildd-manager`` configuration.
Once we have the basic token we can call the proxy, asking for a token:

.. code-block:: sh

  $ curl -X POST http://builder-proxy-auth.staging.lp.internal:8080/tokens -H "Authorization: Basic <basic_token>" -H "Content-Type: application/json" -d '{"username": <your_app_name>}'

Now we have all the information that we need to populate ``args`` that we need in the ``build`` function to use the proxy.
These ``args`` are ``"proxy_url": "http://<your_app_name>:<token_from_curl>@builder-proxy.staging.lp.internal:3128"`` and 
``"revocation_endpoint": "http://builder-proxy-auth.staging.lp.internal:8080/tokens/<your_app_name>"`` that we can assemble manually starting from 
the information we retrieved before, ``<your_app_name>`` will be the name that we will pass to our build function (see the following code) and
the ``<token_from_curl>`` will be the token we retrieved from the ``curl`` of the previous step.

The modified ``build`` call will look like:

.. code-block:: python
  
  # Start the build.
  proxy.build(
    'app-name',
    'snap',
    '<sha1sum from the previous step>',
    {},
    {'name': 'app-name',
    'image_type': 'lxd',
    'series': 'bionic',
    'arch_tag': 'amd64',
    'git_repository': 'https://github.com/tomwardill/test-docker-repo.git', 
    'archives': [
      'deb http://archive.ubuntu.com/ubuntu bionic main restricted',
      'deb http://archive.ubuntu.com/ubuntu bionic-updates main restricted',
      'deb http://archive.ubuntu.com/ubuntu bionic universe'
    ],
    "proxy_url": "http://app-name:<token_from_curl>@builder-proxy.staging.lp.internal:3128",
    "revocation_endpoint": "http://builder-proxy-auth.staging.lp.internal:8080/tokens/app-name"
    })
