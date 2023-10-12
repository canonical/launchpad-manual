================================
Applying database schema changes
================================

Whenever changes are made to the database schema,
these changes need to be applied to the databases in use.

In order to apply changes to e.g. the *test template database* you need to run:

.. code-block:: bash

    database/schema/upgrade.py -d launchpad_ftest_template
    database/schema/security.py -d launchpad_ftest_template


To migrate all of Launchpad's databases in a standard development setup:

.. code-block:: bash

    for db in launchpad_empty launchpad_dev_template launchpad_dev launchpad_ftest_template launchpad_ftest_playground; do
        database/schema/upgrade.py -d "$db"
        database/schema/security.py -d "$db"
    done


A more heavyweight approach is the following command:

.. note::

    Running this command will erase and rebuild everything.

.. code-block:: bash

    make schema


If you only want to rebuild the test template database,
please run the following command:

.. code-block:: bash

    make -C database/schema test
