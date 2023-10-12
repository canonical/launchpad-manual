==============================
Restarting services on Dogfood
==============================

When applying manual changes, it may be necessary to restart services.

Instead of :doc:`restarting all services <resurrect-dogfood>`, it is much
faster to restart individual services.

Restarting the launchpad web application and librarian
======================================================

.. code-block:: bash

    launchpad@labbu:~$ make -C /srv/launchpad.net/codelines/current initscript-stop initscript-start

Restarting launchpad-buildd
===========================

.. code-block:: bash

    launchpad@labbu:~$ /srv/launchpad.net/buildd-manager restart
