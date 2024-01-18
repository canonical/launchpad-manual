Mirror prober
=============

Description
-----------

The mirror prober script checks the Ubuntu `CD mirrors`_ and the
`archive mirrors`_ configured in Launchpad and updates their status based on
the results of the health checks. It is run via a cron job on the
``launchpad-scripts`` unit.

.. _CD mirrors: https://launchpad.net/ubuntu/+cdmirrors
.. _archive mirrors: https://launchpad.net/ubuntu/+archivemirrors

Log files
---------

The ``{{ logs_dir }}/mirror-prober.log`` file (where ``logs_dir`` is usually
``/srv/launchpad/logs``) contains the generic logs for each run of the mirror
prober.

When a mirror fails some checks, an email is sent to its owner's email address
with the relevant detailed logs from the failed run. These log lines are not
present in the above log file. But they can be accessed by the Launchpad team
and admins via the Launchpad web interface by opening the Launchpad page for
the mirror (can be found under the appropriate mirror listing page) and
clicking on the ``Prober logs`` link in the right sidebar.

Release-time changes
--------------------

See https://wiki.canonical.com/InformationInfrastructure/OSA/LPHowTo/ManualCdImageMirrorProber.
