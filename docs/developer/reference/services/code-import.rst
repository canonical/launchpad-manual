Code import
===========

Short description
-----------------
Import system for code hosted outside of Launchpad.

Detailed description
--------------------
To be added.

Documentation
-------------
* Not available.

Git repositories
----------------
* `lp-codeimport <https://git.launchpad.net/lp-codeimport>`_

Bug trackers
------------
* https://bugs.launchpad.net/lp-codeimport

Deployment
----------
* To be added.

Log files
---------
The code importer service is a devops-managed service,
that means we can directly access it, even on production.

Production
~~~~~~~~~~

* log into ``launchpad-bastion``
* run ``sudo -iu prod-launchpad-codeimport``
* ssh into one of the units via ``juju ssh lp-codeimport-bionic/0``

Staging
~~~~~~~

To be added.

Monitoring
----------

Not available.

Common support cases
--------------------

See `Launchpad's playbook for support rotation <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/fix-stuck-code-imports/>`_

More information
----------------
-
