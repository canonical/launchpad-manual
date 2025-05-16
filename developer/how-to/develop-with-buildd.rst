How to develop with Buildd
==========================

LXD VM Support
--------------

This is now on stable and allows for management of VMs with the same LXD CLI.

For now, we need to use the ``images:`` source for images, rather than the ``ubuntu:`` images. The default ubuntu images do not have the LXD agent preinstalled. Once they do, this gets a bit simpler.

It is also slightly simpler to use the ``ubuntu`` user, as it is already available in the image and doesn't require as many hoops jumped to get ``uid``/``gid`` mapping to work.

Create a LXD profile for VMs
----------------------------

This is a convenience helper profile for VMs that will add users and run ``cloud-init`` for installing the LXD VM agent. It is not required and you can pass the options on the ``lxc`` command.

The password for the user can be generated using:

.. code-block:: sh

    $ mkpasswd -m sha-512 <password>

``mkpasswd`` lives in the ``whois`` package.

For now, we are using the LXD provided cloud images as it has the LXD agent and ``cloud-init`` preinstalled. This requires a smaller LXD profile, but needs some extra commands afterwards.

To create this run:

.. code-block:: sh

    $ lxc profile create vm

and then:

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
        users:
        - name: "ubuntu"
          passwd: "<shell password hash>"
          lock_passwd: false
          groups: lxd
          shell: /bin/bash
          sudo: ALL=(ALL) NOPASSWD:ALL
          ssh-import-id: <lp username>
    description: ""
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
        path: <path to folder you want to share to in the VM>
        source: <path to folder you want to share from the host>
        type: disk


Start the LXD VM
----------------

Start a VM via downloading the images: cloud image

``lxc launch images:ubuntu/<release name>/cloud -p vm -p default <vm name> --vm``

This will take a while to settle. You can monitor its progress with ``lxd console <vm name>``.

Once it has complete cloud-init, you should then see an IP assigned in ``lxc list`` and be able to execute a bash shell with ``lxc exec <vm name> bash``.

Configure password and ssh
--------------------------

This should be done by the cloud-init config in the profile, but the package is not installed at the time that is run, so do it afterwards manually:

.. code-block:: sh

    $ lxc exec <vm name> sudo passwd ubuntu
    $ lxc exec <vm name> --user 1000 "/usr/bin/ssh-import-id" <launchpad user id>


This will not be required once we can use the ``ubuntu:`` image source in LXD.

Launchpad Buildd
----------------

We'll need a clone of this and then build and install it for running.

Branch
------

.. code-block:: sh

    $ sudo apt install git
    $ git clone https://git.launchpad.net/launchpad-buildd

Install dependencies
--------------------

.. code-block:: sh

    $ cd launchpad-buildd
    $ sudo apt-add-repository ppa:launchpad/ubuntu/buildd-staging
    $ sudo apt-add-repository ppa:launchpad/ubuntu/ppa
    $ vi /etc/apt/sources.list.d/launchpad-ubuntu-ppa-bionic.list <uncomment deb-src line>
    $ sudo apt update
    $ sudo apt build-dep launchpad-buildd fakeroot
    $ sudo apt install -f

Note: if ``fakeroot`` can't be found try:

.. code-block:: sh

    $ sudo sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
    $ sudo apt-get update
    $ sudo apt build-dep launchpad-buildd fakeroot
    $ sudo apt install -f

Make and install the package
----------------------------

.. code-block:: sh

    $ cd launchpad-buildd
    $ make
    $ cd ..
    $ sudo dpkg -i ./python3-lpbuildd_<version>_all.deb ./launchpad-buildd_<version>_all.deb

Run the buildd
--------------

Edit ``/etc/launchpad-buildd/default`` and change ``ntphost`` to something valid (``ntp.ubuntu.com`` should work)

.. code-block:: sh

    $ sudo mkdir -p /var/run/launchpad-buildd
    $ sudo chown ubuntu: /var/run/launchpad-buildd
    $ cd launchpad-buildd
    $ /usr/bin/python3 /usr/bin/twistd --no_save --pidfile /var/run/launchpad-buildd/default.pid --python /usr/lib/launchpad-buildd/buildd-slave.tac -n

Making changes
--------------

The package is installed as a system deb, so to make changes you will need to rebuild and reinstall the package following the 'Make and install' section.

Testing
-------

You probably want the next section (:ref:`Configuring Launchpad <configuring-launchpad>`) at this point, but if you are doing any buildd development and need to test your changes without having to have the whole system running, you can use the XML-RPC interface to cause builds to happen.

Getting a base image
--------------------

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
-----------------------

You can try running a build via the XML-RPC interface. Start a Python/IPython repl and run.

.. code-block:: python

  import xmlrpclib
  proxy = xmlrpclib.ServerProxy("http://localhost:8221/rpc")
  proxy.status()

Assuming that works, a sample build can be created using (relying on the OCI capabilities being merged into launchpad-buildd):
Note that if we are using the ``lxd`` backend we should specify that in our build ``args`` by adding ``"image_type": "lxd"``.

.. code-block:: python

  proxy.build('1-3', 'oci', '<sha1sum of base, possibly from previous section>', {}, {'name': 'test-build', 'series': 'bionic', 'arch_tag': 'amd64', 'git_repository': 'https://github.com/tomwardill/test-docker-repo.git', 'archives': ['deb http://archive.ubuntu.com/ubuntu bionic main restricted', 'deb http://archive.ubuntu.com/ubuntu bionic-updates main restricted', 'deb http://archive.ubuntu.com/ubuntu bionic universe']})

.. _configuring-launchpad:

Configuring Launchpad
---------------------

Change ``https://launchpad.test/ubuntu/+pubconf`` as admin from ``archive.launchpad.test`` to ``archive.ubuntu.com``.

In ``launchpad/launchpad/configs/development/launchpad-lazr.conf`` change:

1: ``git_browse_root`` from ``https://git.launchpad.test/`` to ``http://git.launchpad.test:9419/``

2: ``git_ssh_root`` from ``git+ssh://git.launchpad.test/`` to ``git+ssh://git.launchpad.test:9422/``

3: ``builder_proxy_host`` from ``snap-proxy.launchpad.test`` to ``none``

4: ``builder_proxy_port`` from ``3128`` to ``none``

In ``launchpad/launchpad/lib/lp/services/config/schema-lazr.conf`` under the ``[oci]`` tag add a pair of private and public keys in order to be able to add OCI credentials, valid example below:

1: ``registry_secrets_private_key``: ``U6mw5MTwo+7F+t86ogCw+GXjcoOJfK1f9G/khlqhXc4=``

2: ``registry_secrets_public_key``: ``ijkzQTuYOIbAV9F5gF0loKNG/bU9kCCsCulYeoONXDI=``



Running soyuz and adding data
-----------------------------

First, you'll need to run some extra bits in Launchpad:

.. code-block:: sh

    $ utilities/start-dev-soyuz.sh
    $ utilities/soyuz-sampledata-setup.py
    $ make run

Image Setup
-----------

Consult the 'Launchpad Configuration' section of :doc:`use-soyuz-locally` to do the correct ``manage-chroot`` dance to register an image with launchpad. Without this, you will have no valid buildable architectures.

User setup
----------

It's convenient to add your user to the correct groups, so you can interact with it, without being logged in as admin.

 1. Log in as admin
 2. Go to https://launchpad.test/~launchpad-buildd-admins and add your user
 3. Go to https://launchpad.test/~ubuntu-team and add your user

Registering the buildd
----------------------

The buildd that you have just installed needs registering with Launchpad so that builds can be dispatched to it.

 1. Go to https://launchpad.test/builders

 2. Press 'Register a new build machine'

 3. Fill in the details.

    - The 'URL' is probably ``http://<buildd ip>:8221``.

    - You can make the builder be either virtualized or non-virtualized, but each option requires some extra work.  Make sure you understand what's needed in the case you choose.

    - Most production builders are virtualized, which means that there's machinery to automatically reset them to a clean VM image at the end of each build.  To set this up, ``builddmaster.vm_resume_command`` in your config must be set to a command which ``buildd-manager`` can run to reset the builder.  If the VM reset protocol is 1.1, then the resume command is expected to be synchronous: once it returns, the builder should be running.  If the VM reset protocol is 2.0, then the resume command is expected to be asynchronous, and the builder management code is expected to change the builder's state from ``CLEANING`` to ``CLEAN`` using the webservice once the builder is running.

    - Non-virtualized builders are much simpler: ``launchpad-buildd`` is cleaned synchronously over XML-RPC at the end of each build, and that's it.  If you use this, then you must be careful not to run any untrusted code on the builder (since a ``chroot`` or container escape could compromise the builder), and you'll need to uncheck "Require virtualized builders" on any PPAs, live file systems, recipes, etc. that you want to be allowed to build on this builder.

 4. After 30 seconds or so, the status of the builder on the builders page should be 'Idle'. This page does not auto-update, so refresh!

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
