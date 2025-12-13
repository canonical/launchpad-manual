Mirror prober
=============

Description
-----------

The mirror prober script checks the Ubuntu `CD mirrors`_ and the
`archive mirrors`_ configured in Launchpad and updates their status based on
the results of the health checks. It is run via a cron job on the
``launchpad-scripts`` unit only in the production environment.

.. _CD mirrors: https://launchpad.net/ubuntu/+cdmirrors
.. _archive mirrors: https://launchpad.net/ubuntu/+archivemirrors

Log files
---------

When a mirror fails some checks, an email is sent to its owner's email address
with the relevant detailed logs from the failed run. These mirror-specific logs
can be accessed by the Launchpad team and admins via the Launchpad web
interface by opening the Launchpad page for the mirror (can be found under the
appropriate mirror listing page - see the links in the previous section) and
clicking on the ``Prober logs`` link in the right sidebar.

The ``mirror-prober.log`` file on the ``launchpad-scripts`` unit contains the
generic, non-mirror-specific logs for each run of the mirror prober.

Production
~~~~~~~~~~

From the ``stg-launchpad`` account on ``launchpad-bastion-ps5.internal``, the
latest mirror prober logs can be accessed by running

.. code-block:: shell-session

    stg-launchpad@launchpad-bastion-ps5:~$ rless scripts.lp.internal::lp-logs/mirror-prober.log

Release-time changes
--------------------

See https://wiki.canonical.com/InformationInfrastructure/OSA/LPHowTo/ManualCdImageMirrorProber.

Common support cases
--------------------

The `Ubuntu Mirror admins`_ handle adding, updating, removing, or deactivating
Ubuntu mirrors. Any errors in the mirror prober logs will require a Launchpad
team member to check the logs and the mirror and confirm whether it is an issue
with the mirror itself or the mirror prober code.

.. _Ubuntu Mirror admins: https://launchpad.net/~ubuntu-mirror-admins
