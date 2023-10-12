===========================
Importing an Ubuntu package
===========================

It may be necessary to import an Ubuntu package into the local Launchpad instance
for testing - the UCT import script requires the package mentioned in a CVE file
to be present before it can create a vulnerability corresponding to the CVE.

This can be done using ``debmirror`` and the ``scripts/gina.py`` script. Install
the ``debmirror`` package, if it is not installed already.

Create a directory to store the partial mirror and perform a sync.

.. code-block:: bash

    $ mkdir /tmp/gina_test_archive
    $ cd /tmp/gina_test_archive
    $ # This syncs just the focal amd64 packages starting with 'bash'
    $ debmirror -v --method=http --arch=amd64 -d focal --keyring=/usr/share/keyrings/ubuntu-archive-keyring.gpg --exclude='.*' --include='/bash' /tmp/gina_test_archive

Configure the mirror path in ``lib/lp/services/config/schema-lazr.conf`` by adding the following section

.. code-block:: ini

    [gina_target.focal]
    root: /tmp/gina_test_archive
    components: main
    distro: ubuntu
    distroseries: focal
    pocketrelease: focal
    source_only: true

The value for the ``root`` key must match path in which the partial mirror was
created above. The ubuntu release used in the ``debmirror`` command must match
the values specified in the above configuration file. The package to be imported
must belong to the component specified above in the Ubuntu repositories.

Run all the Launchpad services including the librarian in a separate session.

.. code-block:: bash

    $ cd ~/launchpad/launchpad
    $ make run

Run the ``scripts/gina.py`` script to import the packages from the partial mirror.

.. code-block:: bash

    $ cd ~/launchpad/launchpad
    $ ./scripts/gina.py focal  # where 'focal' is the release used in the previous steps.


The script will run and print a lot of errors for the packages missing in the partial mirror.
These errors can be ignored. Once it finishes, check its output to verify that the ``bash``
package, which is used in this example, has been imported and uploaded to the librarian.
If there are no errors importing the ``bash`` package, the package should now be available in
the local Launchpad instance.
