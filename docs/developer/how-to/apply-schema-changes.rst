.. _apply-database-schema-changes:

================================
Applying database schema changes
================================

Whenever changes are made to the database schema,
these changes need to be applied to the databases in use.

To migrate all of Launchpad's databases in a standard development setup
to have the latest schema changes:

.. code-block:: bash

    for db in launchpad_empty launchpad_dev_template launchpad_dev launchpad_ftest_template launchpad_ftest_playground; do
        database/schema/upgrade.py -d "$db"
        database/schema/security.py -d "$db"
    done


A more heavyweight approach is the following command:

.. note::

    Running this command will erase all databases and rebuild everything.

.. code-block:: bash

    make schema


If you only want to rebuild the test template database,
please run the following command:

.. code-block:: bash

    make -C database/schema test

If you only want to apply one specific patch for testing purposes, you can
run the following command:

.. code-block:: bash

    psql launchpad_dev -1 -f <your-patch>.sql

This comment will apply file (``-f``) ``<your-patch>.sql`` as a single
transaction (``-1``) to the database named ``launchpad_dev``.
