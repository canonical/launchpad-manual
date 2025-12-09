Buildbot
========

Short description
-----------------

`Buildbot <https://github.com/buildbot/buildbot>`__ is a Python-based
continuous integration testing framework that we use to run tests,
manage stable branches for Launchpad. We use `Buildbot
0.8.12 <https://docs.buildbot.net/0.8.12/>`__ in production currently.
You can access our hosted instance at http://lpbuildbot.canonical.com

Detailed description
--------------------

There are the following main components in the Launchpad Buildbot
setup. 

1. `lpbuildbot <https://code.launchpad.net/lpbuildbot>`__:
   This contains the ``master.cfg`` file and the related Python code
   which powers the
   `buildmaster <https://docs.buildbot.net/0.8.12/manual/introduction.html>`__
   in our buildbot setup. There is a public git branch and a 
   `private production branch <https://code.launchpad.net/~launchpad/lpbuildbot/+git/production>`_,
   which contains secrets related to our
   production deployment. We add changes to the public branch via merge
   proposals and then merge them back to the private “production” branch
   before deployment. In the ``master.cfg`` file, we have defined all
   the necessary configurations (schedulers, workers, job steps) for
   buildbot. 

   1. The buildmaster has a custom ``buildbot-poll.py`` cron script
      which is responsible for merging the commits within the main Launchpad repository in the
      ``master``/``db-devel`` branches, that have completed a successful
      buildbot run, to the ``stable``/``db-stable`` branches
      respectively. It also periodically merges the changes from the
      ``stable`` branch to the ``db-devel`` branch, which then
      propagates to the ``db-stable`` branch after a successful buildbot
      run. For this, the secrets to push to these branches are present in the buildmaster
      unit.

 

2. `Buildbot Worker Charm and Deb
   Package <https://launchpad.net/~launchpad/lpbuildbot-worker/+charm/lpbuildbot-worker>`__:
   This repository contains the code for the
   `buildslave <https://docs.buildbot.net/0.8.12/manual/introduction.html>`__
   which is deployed using the `lpbuildbot-worker
   charm <https://charmhub.io/lpbuildbot-worker/>`__ and the
   `lpbuildbot-worker debian
   package <https://code.launchpad.net/~launchpad/+archive/ubuntu/ppa/+packages?field.name_filter=buildbot-worker&field.status_filter=published&field.series_filter=>`__.
   Recipes to build these are present on the `lpbuildbot-worker
   project <https://launchpad.net/lpbuildbot-worker>`__ in Launchpad.

   1. Working directories for jobs runs for vanilla images and flavors
      can be found at ``/var/lib/buildbot/slaves`` 

Documentation
-------------

- `InformationInfrastructure/OSA/LPHowTo/Buildbot - <https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/builder/work-with-buildbot/>`__

Git repositories
----------------

- https://code.launchpad.net/lpbuildbot-worker

- https://launchpad.net/~launchpad/lpbuildbot-worker/+charm/lpbuildbot-worker

Deployment
----------

To get shell access to Launchpad Buildbot deployment. You can follow the
following steps. 

1. SSH into your bastion account.

2. Run ``sudo -iu stg-launchpad-buildbot`` or you can also run ``pe`` and select the corresponding number ID of the buildbot
   account. 

3. ``juju status``

PS: There are no Staging, QAStaging environments for Buildbot so please
execute steps with caution as Buildbot downtime can cause a lot of
issues. 

We use mojo to manage our deployments. You can find the spec for
buildbot at
`launchpad-mojo-specs <https://git.launchpad.net/launchpad-mojo-specs/tree/lp-buildbot/bundle.yaml>`__.
**NOTE**: The spec is incomplete and the local changes made by previous
engineers needs to be migrated to it. There is a  `branch in
progress <https://code.launchpad.net/~lgp171188/launchpad-mojo-specs/+git/launchpad-mojo-specs/+merge/478047>`__
that adds the missing units in the spec. 

- **Buildbot Master**: At the moment, the buildbot master is deployed
  manually using a vanilla ubuntu charm. The necessary packages and
  configurations are created manually. The actual process is running as
  a systemd service called ``buildmaster``. 

::

   systemctl status buildmaster.service

- **Buildbot Worker:** For worker units, the deployment process looks as
  follows:

  - For charms, you can build and upload the charm to Charmhub via the
    charm recipe. You can deploy a new charm version via the mojo
    specs. 

  - However the helper scripts to create new images, clean up containers
    etc. are placed at ``/usr/bin``\ via the `lpbuildbot-worker debian
    package <https://git.launchpad.net/lpbuildbot-worker/tree/debian/install>`__.
    You can either update the package manually or ``apt-upgrade``
    happens only on charm upgrades

::

   systemctl status buildslave.service

Log files
---------

Buildbot Master Logs: 
^^^^^^^^^^^^^^^^^^^^^^

::

   # Master runs as a twisted server and the logs can be found at
   tail -f /srv/buildbot/lpbuildbot/twistd.log

Buildbot Slave Logs:
^^^^^^^^^^^^^^^^^^^^

::

   # To track charm upgrade status, you can see the logs via
   tail -f /var/log/juju/unit-buildbot-worker*.log

   # Worker logs can be found at
   tail -f /var/lib/buildbot/slaves/twistd.log

Monitoring
----------

Buildbot runs are logged at `Launchpad
Buildbot <https://chat.canonical.com/canonical/channels/launchpad-buildbot>`__
channel on Mattermost. If a build fails, you can navigate to the build log
of your build and review the summary to identify the cause of the failure.
If you suspect the build is failing due to flakiness of the test
infrastructure and not your changes, you can `restart the build
<http://lpbuildbot.canonical.com/force>`__.
