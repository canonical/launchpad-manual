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

.. _disable-builder:

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

.. _cowboy-builder:

Cowboy builder
~~~~~~~~~~~~~~

.. tip::

   Either :ref:`disable<disable-builder>` or switch to manual every
   builder in the same architecture except one, and make the cowboy on that
   builder only. Otherwise, the location of the next triggered build will be
   randomized.

Once you are inside the builder, 

1. Switch to the package directory of lp-buildd with ``cd 
   /usr/lib/python3/dist-packages/lpbuildd/``.
   
2. Make the changes you want with ``sudo`` access, e.g. ``sudo vim
   binarypackage.py``.

3. Once you're done making changes, restart the launchpad-buildd systemd service
   with ``sudo systemctl restart launchpad-buildd``

This will restart the service with your changes included. Running any build
on that specific builder will run the cowboyed changes with it.

.. note::
   The cowboyed changes to the builder will be deleted in the next "cleaning"
   stage of the builder. A "cleaning" stage can be triggered by finished
   builds or disable-then-enable calls. Each subsequent cowboyed build will
   require re-application of the cowboy changes in an identical manner.

Preserve ``.deb`` build schroots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not every build type uses ``lxc`` containers as the build environment.
Some, such as ``.deb`` builds use schroot sessions for this purpose.
Furthermore, unlike ``lxc`` containers, schroot sessions are by default
are configured to be cleaned-up when the build finishes, irrespective of
the build result. 

This deletion is done through an unmounting operation within our
``launchpad-buildd`` codebase. As a result, we need to cowboy a builder to
preserve the schroot session inside.

1. First, follow the ":ref:`cowboy-builder`" section and enter into the 
`binarypackage.py`, with:

.. code-block:: sh

   sudo vim /usr/lib/python3/dist-packages/lpbuildd/binarypackage.py

1. Overwrite the ``iterateReap_SBUILD`` method at the end of the file to
``return`` immediately.
   
.. code-block:: sh

   def iterateReap_SBUILD(self, success):

      return # Here

      # Ignore the rest
      subprocess.call(["sudo", "rm", "-f", self.schroot_config_path])

      self._state = DebianBuildState.UMOUNT
      self.doUnmounting()

3. Restart the launchpad-buildd service with:

.. code-block:: sh

   sudo systemctl restart launchpad-buildd

4. Run the build and eventually :ref:`disable the builder <disable-builder>`.
5. Within the builder once the build finishes, or during it, call:

.. code-block:: sh

   sudo schroot -l

6. Copy the schroot ID and enter into that schroot session with:

.. code-block:: sh

   sudo schroot --run-session -c <session-id>

Clean-up
~~~~~~~~

Once you have finished, please remember to enable the builder again.

.. code-block:: sh

    ❯ ./manage-builders -l qastaging -b qastaging-lcy02-amd64-004 --enable
    Updating 1 builders.
    * qastaging-lcy02-amd64-004
    Changed: 1. Unchanged: 0.
