Porting builders to newer Ubuntu versions
=========================================

QA Migration & Deployment
-------------

There are following steps to porting builders to newer Ubuntu versions.

- Porting `launchpad-buildd <https://code.launchpad.net/~launchpad/launchpad-buildd/>`_ and its dependencies to work on the target Ubuntu version. You can follow `lp-buildd rtd docs <https://launchpad-buildd.readthedocs.io/en/latest/how-to/developing.html>`_ to develop and publish on buildd-staging PPA. 
    - Apart from the deb dependencies defined in `debian/control <https://git.launchpad.net/launchpad-buildd/tree/debian/control?h=noble>`_ in `launchpad-buildd <https://code.launchpad.net/~launchpad/launchpad-buildd/>`_, you would also need deb packages of target ubuntu version for ``bzr-builder``, ``git-recipe-builder`` and ``quilt``.
    - These dependencies are defined in `charm-launchpad-buildd-image-modifier <https://git.launchpad.net/charm-launchpad-buildd-image-modifier/tree/files/scripts/setup-ppa-buildd#n111>`_

- Update the ``gss_series`` variable in `launchpad-mojo-specs <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/tree/vbuilder/bundle.yaml?h=vbuilder>`_. Run ``mojo run`` to deploy the config changes. 
    - PS: We use ``vbuilder`` branch for build farm mojo specs.
    - You don't have to update the builder config to target Ubuntu version at this step. We first have to build an image and then update the builder configs.  

- Next step is to rebuild images. Currently `launchpad-mojo-specs <https://code.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private>`_ `(vbuilder branch)` uses 2 charms to rebuild images & sync images. You can trigger a rebuild by following: `testing-on-qastaging <https://launchpad-buildd.readthedocs.io/en/latest/how-to/deployment.html#testing-on-qastaging>`_. 
    - `charm-glance-simplestreams-sync <https://git.launchpad.net/~launchpad/charm-glance-simplestreams-sync>`_ provides a `sync-images` action that downloads the configured base images and calls a hook to run the image modifier charm. 
    - `charm-launchpad-buildd-image-modifier <https://git.launchpad.net/charm-launchpad-buildd-image-modifier/tree/files/scripts>`_ has scripts that creates a qemu COW VM image for builders with all the needed dependencies and configuration. 

- Update the builder config to use target Ubuntu version `launchpad-mojo-specs <https://git.launchpad.net/~launchpad/launchpad-mojo-specs/+git/private/tree/vbuilder/bundle.yaml?h=vbuilder>`_. Use ``mojo run`` to deploy the config changes.

- You can either wait for builders to reset and pick the new image or reset them using `ubuntu archive tools <https://git.launchpad.net/ubuntu-archive-tools>`_

.. code-block:: sh

    ./manage-builders -l qastaging --disabled -a riscv64  --reset

Notes & Helpful links
---------------------

- With Ubuntu Noble, ``lxd`` is no longer a part of the base image and has to be installed at runtime via systemd service. Refer this `MP <https://code.launchpad.net/~tushar5526/charm-launchpad-buildd-image-modifier/+git/charm-launchpad-buildd-image-modifier/+merge/470811>`_ that installs ``lxd`` at runtime if not available. `launchpad-buildd <https://code.launchpad.net/~launchpad/launchpad-buildd/>`_ uses ``lxd`` to run builds. 

- `Setting up a user on QA staging <https://documentation.ubuntu.com/launchpad/en/latest/how-to/manage-users>`_

- `Debugging build farms <https://documentation.ubuntu.com/launchpad/en/latest/how-to/debug-buildfarm-builder/>`_

- Any update to charms has to be deployed using 

.. code-block:: sh
    
    juju upgrade-charm <unit> <charm-location>


