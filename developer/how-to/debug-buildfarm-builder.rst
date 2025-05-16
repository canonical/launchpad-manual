Debug Build Farm on qastaging
=============================

Access a builder
----------------

The builders are ephemeral, meaning they fully reset after a build.
Therefore, to access the builder, one should either:

* access it during the duration of a build.

* ``disable`` the builder after starting a build so that it doesn't
  automatically trigger the reset when the build finishes.

.. note::

   You should wait until you see some output in the build log before you
   ``disable`` the builder, otherwise the build might not get dispatched
   properly.


Disable a builder
~~~~~~~~~~~~~~~~~

You need to have the ubuntu-archive-tools installed.

.. code-block:: sh

    $ git clone https://git.launchpad.net/ubuntu-archive-tools
    $ sudo apt install python3-launchpadlib python3-ubuntutools


For example, you want to debug the ``lcy02-amd64-004`` instance.

.. code-block:: sh

    ❯ ./manage-builders -l qastaging -b qastaging-lcy02-amd64-004 --disable
    Updating 1 builders.
    * qastaging-lcy02-amd64-004
    Changed: 1. Unchanged: 0.


You can look up the builder name on https://qastaging.launchpad.net/builders or
via ``manage-builders -l qastaging``.


SSH into the builder
~~~~~~~~~~~~~~~~~~~~

Once you are ready to access a builder, follow these steps:

1. SSH into bastion ``ssh launchpad-bastion-ps5`` and switch to the
   ``stb-vbuilder-qastaging`` user by running ``sudo -iu stg-vbuilder-qastaging``.

2. Juju ssh into the ``vbuilder-manage`` for the region your builder is, for
   example ``juju ssh vbuilder-manage-bos03/leader``.

3. Switch to the ``ppa`` user by running ``sudo -iu ppa``.

4. SSH into builder instance. For example, to access the ``bos03-amd64-004``
   builder, you should run ``ssh
   ubuntu@qastaging-bos03-amd64-004.vbuilder.qastaging.bos03.scalingstack``.
   This builder address can be found when click on the builder on
   https://qastaging.launchpad.net/builders.

From there, you can check the ``launchpad-buildd`` logs in
``/var/log/launchpad-buildd/`` or run commands within the builder.

The build itself should be done within a container within the builder. If you
need to look into the container, you can ``lxc list`` to list the lxc
containers present in the builder, and then run ``lxc shell`` to start a shell
session from within the container.


Clean-up
~~~~~~~~

Once you have finished, please remember to enable the builder again.

.. code-block:: sh

    ❯ ./manage-builders -l qastaging -b qastaging-lcy02-amd64-004 --enable
    Updating 1 builders.
    * qastaging-lcy02-amd64-004
    Changed: 1. Unchanged: 0.
