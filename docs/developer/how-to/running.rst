.. _setting-up-and-running-launchpad-advanced:

Setting up and running Launchpad (Advanced)
===========================================

.. note::

    `Ask for help <https://dev.launchpad.net/Help>`_ right away if you run
    into problems.

This page explains how to set up and run Launchpad (for development) on your
own machine, using a `LXD
<https://documentation.ubuntu.com/lxd/en/latest/>`_-managed container to
isolate it from the rest of your system.

After you've done this, you may want to read about
:doc:`../explanation/navigating`.

.. _supported_operating_systems:

Supported operating systems
===========================

For the host system, any reasonably modern Ubuntu release should work.
Other Linux distributions that have LXD should work too, though we don't
test on them.

Launchpad requires Ubuntu 20.04 LTS with Python 3.8. Ubuntu 22.04 is known not
to work yet.

We'd like Launchpad to run on other operating systems, especially `Debian
GNU/Linux <https://www.debian.org/>`_, so that more people can contribute to
Launchpad development.  If you're interested in working on Launchpad
portability, please `let us know <https://dev.launchpad.net/Help>`_.  Note
that our focus is on getting Launchpad to build easily so more people can
participate in Launchpad development.  Running a stable production instance
would be *much* harder than running a single-developer test instance, and we
don't recommend it.  Unlike many open source projects, we're not seeking to
maximize the number of installations; our goal is to improve the `instance
we're already running <https://launchpad.net/>`_.

Why use LXD containers?
=======================

Launchpad development setup makes significant changes to your machine; it's
nice to be unaffected by those when you're not doing such development.
Using containers means that the version of Ubuntu on your host system
doesn't need to match Launchpad's requirements.  Multiple containers can be
used to work around Launchpad's limitations regarding concurrent test runs
on a single machine.

LXD also has some nice snapshotting and ZFS capabilities, and is what other
Launchpad developers use, so other people will be able to help you debug
your setup if needed.

The installation script is written with the assumption that it will be
running inside such a container.  If you run it on your host system, it may
well break it.

Create a LXD container
======================

This assumes you already have LXD set up.  If not, follow the `instructions
<https://documentation.ubuntu.com/lxd/en/latest/getting_started/>`_ for
getting it installed and configured on your network.

1. If you haven't done so already, run this script to set up LXD to let you
   use your home directory inside the container.  Some developers prefer to
   only mount a subdirectory of their home directory in the container: to do
   that, replace ``$HOME`` with ``$HOME/src`` or similar.  Although it may
   be tempting, make sure not to call your local user "launchpad", as that
   will break; see :ref:`database-permissions`.

.. code-block:: sh

    #!/bin/sh
    
    id=400000  # some large uid outside of typical range, and outside of already mapped ranges in /etc/sub{u,g}id
    uid=$(id -u)
    gid=$(id -g)
    user=$(id -un)
    group=$(id -gn)
    
    # give lxc permission to map your user/group id through
    sudo usermod --add-subuids ${uid}-${uid} --add-subgids ${gid}-${gid} root
    
    # create a profile to control this
    lxc profile create $user >/dev/null 2>&1
    
    # configure profile
    cat << EOF | lxc profile edit $user
    name: $user
    description: allow home dir mounting for $user
    config:
      raw.idmap: |
        uid $uid $id
        gid $gid $id
      user.user-data: |
        #cloud-config
        runcmd:
          - "groupadd $group --gid $id"
          - "useradd $user --uid $id --gid $group --groups adm,sudo --shell /bin/bash"
          - "echo '$user ALL=(ALL) NOPASSWD:ALL' >/etc/sudoers.d/90-cloud-init-users"
          - "chmod 0440 /etc/sudoers.d/90-cloud-init-users"
    devices:
      home:
        type: disk
        source: $HOME
        path: $HOME
    EOF

2. Create a container. This command creates a Ubuntu 20.04 unprivileged
   container using the profile created in the previous step.

.. code-block:: sh

    lxc launch ubuntu:20.04 lpdev -p default -p $USER

.. note::
   If the command above fails with ``Error: No root device could be found``, you may need to run

   .. code-block:: sh

        lxd init

   This will ensure you have initialized your LXD storage.

3. Find the container IP, either from ``lxc list`` or ``lxc info lpdev``.

.. note::
   If your new container does not have an IPv4 address when you run ``lxc list``, 
   see :ref:`Network Connectivity <network-connectivity>` in Troubleshooting section.

4. In order to be able to ssh into the container, you need to add your
   public key to your local ``.ssh/authorized_keys`` configuration.  Also
   make sure that both ``.ssh`` (700) and ``authorized_keys`` (600) have the
   correct permissions.

5. Connect as follows.  (The -A permits you to access Launchpad code hosting
   from within the container without needing to reenter passphrases.)

.. code-block:: sh

    ssh -A $USER@IP_ADDRESS_FROM_LXC_LS

.. note::
   LXD provides a way to access the LXD containers using DNS names, for example, ``lpdev.lxd``,
   where ``.lxd`` is the default base domain name for the LXD bridge and ``lpdev`` is the name of
   the LXD container. To set this up, follow the instructions in
   https://documentation.ubuntu.com/lxd/en/latest/howto/network_bridge_resolved/.
   Once the setup is done, you can use ``lpdev.lxd`` in the above command instead of the
   IP address of the ``lpdev`` container.

Getting Launchpad
=================

Do all this *inside* the container you set up previously.  Be aware that
changes in your home directory inside the container will also be seen
outside the container and vice versa.

If your Launchpad username differs from your local one, then put this in
``~/.ssh/config`` in the container before doing anything else, replacing
``LPUSERNAME`` with your Launchpad username::

    Host git.launchpad.net
            User LPUSERNAME

Then:

.. code-block:: shell-session

   $ mkdir ~/launchpad
   $ cd ~/launchpad
   $ curl https://git.launchpad.net/launchpad/plain/utilities/rocketfuel-setup >rocketfuel-setup

Read through the rocketfuel-setup script at this point and make sure you're
OK with what it's going to do.  (See :doc:`../explanation/running-details` if you want to
know more.)

.. code-block:: shell-session

   $ chmod a+x rocketfuel-setup
   $ ./rocketfuel-setup

This will take a while -- maybe a few hours to get everything, depending on
your Internet connection.

Note that you will be prompted for your ``sudo`` password, and for a
Launchpad login ID (that is, your username on ``launchpad.net``).  The sudo
access is necessary to get Launchpad running on your box; the Launchpad
login is not strictly necessary, and you can just hit Return there if you
want.  See below for an explanation.

Note that this will make changes to your Apache configuration if you already
have an Apache server in your container.  It will also add entries to
``/etc/hosts``, and it will setup a PostgreSQL server in your container.

If you are running ``rocketfuel-setup`` to bring up a new container but your
home directory already has a usable Launchpad tree, you can pass
``--no-workspace`` to only perform the system-wide setup.

Note that if ``rocketfuel-setup`` bails out with instructions to fix
something, you just need to run it again and it should pick up where it left
off.

.. code-block:: shell-session

   $ sudo apt full-upgrade

This is just to make doubly-sure everything from the Launchpad PPA gets
installed.

.. code-block:: shell-session

   $ ls
   launchpad/    lp-sourcedeps/ rocketfuel-setup
   $ cd launchpad

You are now in a newly-cloned Git repository, with one branch ('master'),
into whose working tree the other source dependencies have been symlinked.
The source dependencies actually live in ``../lp-sourcedeps``.

.. _pre-commit:

Installing the pre-commit hook
==============================

If you intend to make any changes to Launchpad, you should also set up
`pre-commit <https://pre-commit.com/>`__ now:

1. Install ``pre-commit`` itself.  If your host system is Ubuntu 20.10 or
   newer, then ``sudo apt install pre-commit`` is enough; otherwise, you can
   install it in your user account (`pipx <https://pypi.org/project/pipx/>`_
   works well to keep it isolated; whatever you do, don't run ``pip``
   system-wide as root!).  We require this to be installed separately rather
   than including it in Launchpad's virtual environment because developers
   commonly run ``git commit`` outside the container used for running
   Launchpad.

2. Install the ``pre-commit`` git hook by running ``pre-commit install`` in
   your newly-cloned ``launchpad`` repository.

Building
========

Before you can run Launchpad for the first time, you need to set up PostgreSQL.

.. note::

    **DO NOT run the database setup script below if you use PostgreSQL for
    anything other than Launchpad!**  Running the script will destroy any
    PostgreSQL databases on your system.  See
    https://dev.launchpad.net/DatabaseSetup for details.

.. code-block:: shell-session

    $ ./utilities/launchpad-database-setup $USER

**(Please have read the previous comment before you run the above command!)**

Finally, build the database schema (this may take several minutes):

.. code-block:: shell-session

    $ make schema

If you encounter an error while building Python wheels, see :ref:`pynacl-fix`.

Running
=======

Now you should be able to start up Launchpad:

.. code-block:: shell-session

    $ make run

This only runs the basic web application.  `Codehosting
<https://dev.launchpad.net/Code/HowToUseCodehostingLocally>`_ and `Soyuz
<https://dev.launchpad.net/Soyuz/HowToUseSoyuzLocally>`_ require additional
steps.

For subsequent builds, you can just do ``make run`` right away.  You don't
need to do ``make schema`` every time, and you should avoid it because it's
expensive and because it will clean out any data you might have put into
your test instance (through the web UI or by running other scripts).

CSS Watch
---------

While running a local instance of Launchpad, if you are interested in updating
CSS or SCSS files, they will not re-render automatically.
To enable that and make frontend changes more straight-forward, you can run:

.. code-block:: shell-session

    $ make css_watch

This should be run in a separate terminal session alongside ``make run``.

Accessing your web application
==============================

When running ``make run``, your application is running in your container, but it
is not yet accessible outside of it - this includes your host machine, i.e.,
you won't, for example, be able to access your application from your browser.

Unless the only thing you're doing is running parts of the test suite, you
probably want to make your new Launchpad instance accessible from other
machines on the same local network, or in particular from the host system.

Amending the Apache configuration
---------------------------------

Launchpad's default development Apache config
(``/etc/apache2/sites-available/local-launchpad.conf``) only listens on
127.0.0.88.  This can be overridden with the ``LISTEN_ADDRESS`` environment
variable when running ``make install``.  You probably want to make it listen
on everything:

.. code-block:: shell-session

    $ sudo make LISTEN_ADDRESS='*' install

Amending the hosts file
-----------------------

Launchpad makes extensive use of virtual hosts, so you'll need to add
entries to ``/etc/hosts`` on any machine from which you want to access the
Launchpad instance.

Within the container running the instance, you can see the relevant hostnames
in ``/etc/hosts`` - these need to be added to the machine you want to access
the application from, mapped to the server machine or container's external IP address.

For example, to access the application in your host system (and your browser),
you should copy the ``*.launchpad.test`` hostnames you see in the ``hosts`` file 
within the container running the application, and append them to your host system's
``hosts`` file, mapped to the IPv4 address of the container running the app.

This should look similar to this:

.. code-block::

    # Launchpad virtual domains. This should be on one line.
    <your container IPv4 address>     launchpad.test answers.launchpad.test archive.launchpad.test api.launchpad.test blueprints.launchpad.test bugs.launchpad.test code.launchpad.test feeds.launchpad.test keyserver.launchpad.test ppa.launchpad.test private-ppa.launchpad.test testopenid.test translations.launchpad.test xmlrpc-private.launchpad.test xmlrpc.launchpad.test

.. note::

    To access the application in a Windows machine, it may be helpful to know that
    the Windows equivalent of ``/etc/hosts`` is located at
    ``C:\WINDOWS\system32\drivers\etc\hosts``.  Note that Windows' version has a
    line length limit, so you might have to split it across multiple lines or
    only include the hostnames that you need.

You should now be able to access ``https://launchpad.test/`` in a web
browser on a suitably configured remote computer. Accept the local
self-signed certificate. You can log in as ``admin@canonical.com`` without
a password. (This is only for development convenience, and assumes that you
trust machines that can route to your LXD containers; of course a production
deployment would need real authentication.). If you want to create more user
accounts, see :doc:`./manage-users`.

Accessing launchpad.test from a single host over SSH
----------------------------------------------------

As an alternative to the above, SSH provides a SOCKS proxy.  By running that
proxy on the target machine, you can view its Launchpad web site as if you
were on that machine, without having to open non-SSH ports to a wider
network.  To do so:

.. code-block:: shell-session

    $ ssh -D8110 target-machine

Then set your browser's SOCKS proxy settings to use ``target-machine:8110``.

Stopping
========

You can stop Launchpad by hitting **Control-C** in the terminal where you
started it:

.. code-block:: shell-session

    ^C
    [...shutting down Launchpad...]
    $ 

Or you can be at a prompt in the same directory and run this:

.. code-block:: shell-session

    $ make stop

Troubleshooting
===============

.. _network-connectivity:

Network connectivity
--------------------

"The LXC container is not getting an IPv4 address assigned and the network
connectivity inside the container doesn't work."

On Ubuntu 21.10, ``ufw`` uses ``nftables`` by default, so if you are using
Ubuntu 21.10 on the host and ``ufw`` is enabled with the default policy of
blocking incoming and routed traffic, the rules added by LXD will not take
effect, and hence LXD's traffic will be dropped.

The fix is to add ``ufw allow`` rules to allow incoming and routed traffic
on the bridge interface, like this (replacing ``lxdbr0`` with the name of
the bridge interface on your computer):

.. code-block:: sh

    sudo ufw allow in on lxdbr0
    sudo ufw route allow in on lxdbr0

.. _pynacl-fix:

Error building Python wheels
----------------------------

When running ``make schema`` on some machines, ``pynacl`` `fails to build <https://github.com/pyca/pynacl/issues/553>`_, leading to ``ERROR: Failed building wheel for pynacl``.

If you encounter this issue, try running the following:

.. code-block:: shell-session

    $ sudo apt install --yes libsodium-dev

Then add the following line to the ``Makefile`` under the ``PIP_ENV`` commands:

.. code-block:: shell-session

    PIP_ENV += SODIUM_INSTALL=system

Then run `make schema` again.

Email
-----

"I have Launchpad running but emails are not sent."

Development Launchpads don't send email to the outside world, for obvious
reasons.  They connect to the local SMTP server and send to root.  To create
new users, create a new account and check the local mailbox, or see
:doc:`./manage-users`.

.. _database-permissions:

Database permissions
--------------------

"My database permissions keep getting deleted!"

If your local account is called "launchpad" it conflicts with a role called
"launchpad" which is defined in ``database/schema/security.cfg``.  You need
to rename your local account and re-assign it superuser permissions as the
``utilities/launchpad-database-setup`` script does.
