Debug Build Farm
================

Access a builder in qastaging
-----------------------------

The builders are ephemeral, meaning they fully reset after a build.
Therefore, to access the builder, one should either:

* access it during the duration of a build.

* set the builder to ``manual`` after starting a build so that it doesn't
  automatically trigger the reset when the build finishes.


Set a builder to manual
~~~~~~~~~~~~~~~~~~~~~~~

This requires permissions granted by being part of the ``~admins`` team.
To anoint yourself to be part of that team in qastaging, see
:doc:`./manage-users`.

1. Go to https://qastaging.launchpad.net/builders.

2. Click on the builder you want to set to manual.

3. Click the "Switch to manual-mode" button.


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

From there, you can check the ``launchpad-buildd`` logs in
``/var/log/launchpad-buildd/`` or run commands within the builder.

The build itself should be done within a container within the builder. If you
need to look into the container, you can ``lxc list`` to list the lxc
containers present in the builder, and then run ``lxc shell`` to start a shell
session from within the container.
