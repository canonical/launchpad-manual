.. _setting-up-and-running-launchpad-quickstart:

=============================================
Setting up and running Launchpad (Quickstart)
=============================================

.. note::

    `Ask for help <https://dev.launchpad.net/Help>`_ right away if you run
    into problems.

This page explains how to quickly set up and run Launchpad (for development) on your
own machine, using a `LXD
<https://documentation.ubuntu.com/lxd/en/latest/>`_-managed container. You can 
`install <https://canonical.com/lxd/install>`_ LXD as a snap. 

After you've done this, you may want to read about
:doc:`../explanation/navigating`.

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

Setting up Launchpad Development Container
==========================================

.. code-block:: shell-session

   curl https://git.launchpad.net/launchpad/plain/utilities/rocketfuel-devstart > rocketfuel-devstart


.. code-block:: shell-session

   chmod a+x rocketfuel-devstart
   ./rocketfuel-devstart --help
   ./rocketfuel-devstart --download

Specify the ``--download`` flag to download and import the latest Launchpad Dev LXD image. 
To spin up new containers from an existing image just use run the script without any flags. 

Note that you will be prompted for your ``sudo`` password, a ``folder path``
which will server as the primary folder for your workspace and for a
Launchpad login ID (that is, your username on ``launchpad.net``).  The sudo
access is necessary to get Launchpad running on your box; the Launchpad
login is not strictly necessary, and you can just hit Return there if you
want.  See below for an explanation.

Please note that the script will add entries to ``/etc/hosts`` while bootstrapping the setup.

The setup mounts a host folder inside container so that you can perform git operations
from the host system without moving your SSH keys into the container. 

Once the setup completes, you will be prompted with a bunch of information like host
system workspace directory path, container workspace directory path and command to ssh 
into the container. 

Setting up VSCode IDE for development
=====================================

We recommend the following setup for easier development of Launchpad. 

1. Install `VSCode <https://code.visualstudio.com/docs/setup/linux#_snap>`_
2. Install `Remote SSH VSCode Extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_
3. Setup a SSH connection to your LXC container. You can use the ``ssh`` command from the script's output.
4. Once you have connected to your container. Open the path ``/home/ubuntu/launchpad-workdir/launchpad`` in VSCode either via UI
   or via VSCode's terminal ``code /home/ubuntu/launchpad-workdir/launchpad``
5. Install `Python Language Support <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_ from VSCode's extensions. 
6. Run ``Ctrl + Shift + P`` to open VSCode's command palette and type ``Python: Select Interpreter``. Click on ``Enter interpreter path`` 
   and select ``env/bin/python`` as your Python interpreter. IntelliSense should work at this point, if it doesn't reload VSCode. 

.. note::

    After configuring the above ``Python Support`` in your container.
    Starting a new terminal in VSCode will have ``virtualenv`` activated by default. 
    ``make run`` and other commands don't work properly within a virtualenv as they are not able to find some system
    dependencies. It is better to execute make commands in a separate shell. You can use ``lxc shell <container-name>`` 
    to start a bash shell. 

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
   your host's ``launchpad`` workspace directory. 

Running
=======

Before running Launchpad, its best to sync your local Launchpad repo with remote hosts because the images are pre-seeded with a Launchpad clone that might not be up to date. 
On your local system, go to the workspace directory you specified during setup and sync your local repo. 

.. code-block:: shell-session
    
    git remote -v
    git fetch
    git pull upstream master

.. note::

    Because the development image is built periodically rather than on every change
    to the main branch, it may not always contain the latest database migrations if
    a new image hasn’t been published with those changes yet. If needed, refer to 
    :ref:`this page <apply-database-schema-changes>` for instructions on applying 
    the newer database schema changes.

Now you should be able to start up Launchpad:

.. code-block:: shell-session

    make run

This only runs the basic web application.  `Codehosting
<https://dev.launchpad.net/Code/HowToUseCodehostingLocally>`_ and `Soyuz
<https://dev.launchpad.net/Soyuz/HowToUseSoyuzLocally>`_ require additional
steps.


CSS Watch
---------

While running a local instance of Launchpad, if you are interested in updating
CSS or SCSS files, they will not re-render automatically.
To enable that and make frontend changes more straight-forward, you can run:

.. code-block:: shell-session

    make css_watch

This should be run in a separate terminal session alongside ``make run``.

Accessing your web application
==============================

The application is installed by default to accept connections from ``* (all hosts)``.
You can visit ``launchpad.test`` and use ``admin@canonical.com`` as a pre-seeded user
for login.  

Stopping
========

You can stop Launchpad by hitting **Control-C** in the terminal where you
started it:

.. code-block:: shell-session

    ^C
    [...shutting down Launchpad...]
    

Or you can be at a prompt in the same directory and run this:

.. code-block:: shell-session

    make stop
