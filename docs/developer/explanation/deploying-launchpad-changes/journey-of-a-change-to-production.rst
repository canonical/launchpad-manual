=========================================================================
The journey of a Launchpad change from a developer's branch to production
=========================================================================

.. warning::

   This document contains many links that are Canonical-internal and only
   accessible to those who work for Canonical.

##########
Characters
##########

* The Launchpad developer.
* Launchpad's branches.
* Launchpad itself.
* Jenkins jobs.
* Buildbot.
* Deployable.
* Launchpad ``qastaging`` and ``staging`` environments.
* Scripts from the ``lp:launchpad-bastion-scripts`` repository.
* Juju and mojo.
* Fragile Launchpad jobs.
* Launchpad production environment.

###########
The journey
###########

What VCS branches does Launchpad use?
-------------------------------------

The `main Launchpad repository <https://git.launchpad.net/launchpad>`_ has 4
main (or "trunk") branches. These are ``master``, ``stable``, ``db-devel``,
and ``db-stable``. For more details see :ref:`branches <about-launchpad-branches>`.

How to contribute a code change or a database schema change to Launchpad?
-------------------------------------------------------------------------

If the change includes code and database schema changes, both have to be done
separately and target different branches. The database patch needs to be based
on and target the ``db-devel`` branch, whereas the code changes need to be based
on and target the ``master`` branch. This is because database changes can be
destabilising to other work, so we isolate them into a separate branch. Since
Launchpad has a large database and codebase with strict uptime requirements,
we want to deploy changes to only one of these at a time and this separation
helps that as well.

How to test the code and database changes together?
---------------------------------------------------

It is important to get the database patches submitted and merged to the
``db-devel`` branch as early as possible. This is because those changes get
merged to the ``master`` branch only after they are deployed to production
(the details will be explained in a later question) and it is a pre-requisite
to get the code changes merged.

While the database patches make their way to production and to the ``master``
branch, one way to test the code and the database changes together is
to copy the database patch from the ``db-devel`` branch manually and apply
it locally in the development environment to implement and test the
corresponding code changes. Once the database patch is deployed to the
production environment and merged back to the ``master`` branch, the code and
the database changes should be tested together in the ``qastaging``
environment before deploying the code changes to production.

How to deploy the database changes to the production environment?
-----------------------------------------------------------------

The database patches should be submitted to the ``db-devel`` branch and once
they are approved, they get merged by a landing (aka "merging") bot which
performs the merge. The trunk branches of Launchpad have ACLs so that only
the landing bot can push changes to them.

Once the changes are merged to the ``db-devel branch``, the
`Launchpad buildbot <http://lpbuildbot.canonical.com>`_, runs the full
Launchpad test suite on the ``db-devel`` branch and if it passes, the new
changes get merged to the ``db-stable`` branch.

Once this is done, the changes show up on the `launchpad-db deployable page`_
and there is a periodic cron job that automatically deploys the new database
patches, if any, to the `Launchpad staging environment`_.

The `database patch application time  <db-patch-application-time_>`_ can
be checked from the ``staging`` deployment logs. Launchpad has strict
requirements about the patch application time and it should be under
10 seconds.

After confirming the patch application time, the instructions in the
`fastdowntime deployment process documentation`_ can be used to deploy the
database patch to production. Our database deployment policy requires
deploying only one database patch per deployment. If there are multiple patches
to deploy, they should be deployed separately. Since there are some fragile
jobs (for example, the PPA and ``ftpmaster`` publishers, librarian garbage
collector) that shouldn't be interrupted by a database downtime, the deployment
process ensures that there are no such jobs running before applying the patch
with a small downtime. At the end of this process, the database changes will get
merged to the ``master`` branch.

.. _fastdowntime deployment process documentation: https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/launchpad-rollout/launchpad-deployments/database-deployment/
.. _launchpad-db deployable page: https://deployable.ols.canonical.com/project/launchpad-db
.. _Launchpad staging environment: https://staging.launchpad.net
.. _path application times: _

What is the landing bot?
------------------------
When a Launchpad merge proposal is approved and its status is set to
``Approved``, there is a `Launchpad Jenkins trigger`_ that runs and
triggers the `Launchpad merge Jenkins job`_ to merge the changes to
the appropriate target branch. This job is often called as the landing
bot. This and the other Jenkins jobs that we use are defined in the
`ols-jenkaas-jobs repository`_.

.. _Launchpad Jenkins trigger: https://jenkins.ols.ps5.canonical.com/job/trigger-launchpad/
.. _Launchpad merge Jenkins job: https://jenkins.ols.ps5.canonical.com/job/launchpad/
.. _ols-jenkaas-jobs repository: https://git.launchpad.net/ols-jenkaas-jobs

What is buildbot?
-----------------

`Buildbot <https://buildbot.net>`_ is a continuous integration system that we
use for running the Launchpad test suite before promoting the changes in the
``master``, ``db-devel`` branches to the ``stable``, ``db-stable`` branches
(changes to production are deployed from these branches) respectively.

Our deployment of buildbot has 2 or more build configurations defined and these
configurations have names like ``lp-devel-focal`` and ``lp-db-devel-focal``,
where the former runs the test suite on the ``master`` branch (code changes)
and the latter runs the test suite on the ``db-devel`` branch (database
changes).

There is a `buildbot poller script`_ that runs on the buildbot buildmaster and
merges new commits that have completed a successful Launchpad test suite run
into the appropriate stable branch.

.. _buildbot poller script: https://git.launchpad.net/lpbuildbot/tree/buildbot-poll.py

What is deployable?
-------------------

`Deployable <https://launchpad.net/isitdeployable>`_ is the web application that
we use to track each revision of code, whether it is ready to be deployed, and
the details of the commits included in each deployment. There is a
`Launchpad deployable project`_ (tracking the ``stable`` branch) and a
`Launchpad DB deployable project`_ (tracking the ``db-stable`` branch.)

.. _Launchpad deployable project: https://deployable.ols.canonical.com/project/launchpad
.. _Launchpad DB deployable project: https://deployable.ols.canonical.com/project/launchpad-db

The deployable page lists the commits in the corresponding stable branch that
haven't been deployed to the production environment. To deploy a specific
commit, that commit and all its ancestors that are listed in that page should
be tested by a Launchpad engineer (usually the author of the commit) in the
``staging`` or ``qastaging`` environments and marked as deployable using the
button under each commit.

Then during the deployment process, a deployment request is created on this
web application to track the commits that are included in that deployment. And
after the deployment is completed, the deployment request is marked as deployed.

The deployment requests on this application are solely used for tracking and do
not affect the actual deployment process in any way.

What are the Launchpad pre-production environments?
---------------------------------------------------

At the time of writing, Launchpad has 2 pre-production environments,
`staging`_ and `qastaging`_. The ``staging`` environment is primarily used to
test the database changes whereas the ``qastaging`` environment is used to
test the code changes. These are deployed on a Canonical ProdStack environment
and the Launchpad team members have shell access to these environments via the
VPN.

We have cron jobs in the Launchpad bastion environment to automatically deploy
new changes in the ``db-stable`` branch to the ``staging`` environment and
new changes in the ``stable`` branch to the ``qastaging`` environment. These
jobs are added to the ``stg-launchpad`` user's crontab and the scripts used
in these jobs are present in the `launchpad-bastion-scripts repository`_.

Shell access to these environment is available after connecting to the VPN,
logging in to the Launchpad bastion, and switching to the ``stg-launchpad``
user. This user has access to the ``staging`` and ``qastaging`` Juju models.

Even though these environments are mainly used by the Launchpad team, there are
other Canonical teams (IS, Store, Kernel, for example) that use these
environments in limited ways too.

.. _staging: https://staging.launchpad.net
.. _qastaging: https://qastaging.launchpad.net
.. _launchpad-bastion-scripts repository: https://git.launchpad.net/launchpad-bastion-scripts

.. _db-patch-application-time:

How to check the database patch application time in the ``staging`` environment?
--------------------------------------------------------------------------------

The automatic deployment and application of the database patches to the
``staging`` environment is done using the `auto-upgrade-staging script`_,
which uses `mojo <https://mojo.canonical.com>`_ and the `Launchpad mojo specs`_
to do its job, and the `staging_restore.sh script`_. These scripts are run
periodically as cron jobs under the ``stg-launchpad`` account on the Launchpad
bastion.

The database patch application times can be found from files in the ``~/logs``
directory with a name like ``2024-11-17-staging_restore.log``. If the database
patch application failed with an error, it is possible to apply it manually
by running the ``preflight`` juju action on the ``staging``
``launchpad-db-update`` unit to verify that there are fragile jobs running and
then running the ``db-update`` juju action to apply the patch. The output of
the ``db-update`` juju action will show the patch application time.

.. _auto-upgrade-staging script: https://git.launchpad.net/launchpad-bastion-scripts/tree/auto-upgrade-staging
.. _Launchpad mojo specs: https://git.launchpad.net/launchpad-mojo-specs
.. _staging_restore.sh script: https://git.launchpad.net/launchpad-bastion-scripts/tree/staging-restore/staging_restore.sh

What is the ``fastdowntime`` deployment process?
------------------------------------------------

Deploying cold database patches to the production Launchpad database requires
having a very short downtime (usually < 10 seconds). That is why the process
to deploy such cold database patches is called ``fastdowntime``. For details
about hot and cold database patches, see :ref:`Live Patching <live-database-patching>`.


How do code changes in the ``stable`` branch get added to the ``db-stable`` branch?
-----------------------------------------------------------------------------------

The same buildbot poller script takes care of periodically merging the latest
changes in the ``stable`` branch to the ``db-devel`` branch. Then the changes
get tested on buildbot before they get merged to the ``db-stable`` branch.

As mentioned in the explanation of the database deployment process, the changes
in the ``db-stable`` branch get submitted for merge to the ``master`` branch
by a Launchpad developer after deploying a database patch. Once the merge
proposal gets approved and merged, buildbot runs the test suite and if it
passes, the changes then get merged to the ``stable`` branch.

How does a Launchpad branch get deployed?
-----------------------------------------

When a change is merged to the ``master`` branch, there is a
`launchpad-build-charm Jenkins job`_ that builds a Launchpad deployment tarball
of the latest commit in that branch and publishes it to a well-known bucket
on the ProdStack SWIFT storage. All the Launchpad charms use these tarballs
to deploy the Launchpad source and its dependencies.

Similarly, there is a `launchpad-build-db-charm Jenkins job`_ that builds a
tarball of the latest commit in the ``db-devel`` branch and publishes it to
SWIFT.

In the production environment, all the Launchpad units except the
``launchpad-db-update`` unit run the tarball of a specified commit in the
``stable`` branch. The ``launchpad-db-update`` unit runs the tarball of the
latest commit in the ``db-stable`` branch because it is used to apply the
database patches.

In the ``staging`` environment, all the Launchpad units run the tarball of the
latest commit in the ``db-stable`` branch and in the ``qastaging`` environment,
all the Launchpad units run the tarball of the latest commit in the ``stable``
branch. Due to this, database changes can be deployed to the qastaging
environment only after they have been merged to the ``master`` after the
production deployment and promoted to the ``stable`` branch after a successful
buildbot run.

The database changes have to be deployed in the ``qastaging`` environment
manually by following a process similar to the production ``fastdowntime``
deployment.

.. _launchpad-build-charm Jenkins job: https://jenkins.ols.ps5.canonical.com/job/launchpad-build-charm/
.. _launchpad-build-db-charm Jenkins job: https://jenkins.ols.ps5.canonical.com/job/launchpad-build-db-charm/

How does the Launchpad deployment process work?
-----------------------------------------------

Launchpad is deployed to a Canonical ProdStack environment using Juju charms
and ``mojo``. We use the ``lp`` spec in the `launchpad-mojo-specs repository`_
to define the Juju bundle (see ``lp/bundle.yaml``) used to deploy the Launchpad
stack.

For deploying changes to the pre-production environments, we directly invoke
the ``mojo run`` command from the ``stg-launchpad`` account on the Launchpad
bastion. This is usually only needed when the automatic deployment cron jobs
did not work. Since this account has access to both the staging and qastaging
environments, we have to source either ``.mojorc.staging`` or
``.mojorc.qastaging`` before running ``mojo run``. Alternatively, we can also
prefix environment-specific commands with ``in-model staging`` or
``in-model qastaging`` to run them in the context of that environment.

For deploying changes to the production environment, we use the
``upgrade-production`` command from the ``stg-launchpad`` account on the
Launchpad bastion to invoke the appropriate ``mojo`` commands on the production
bastion that only IS have access to.

.. _launchpad-mojo-specs repository: https://git.launchpad.net/launchpad-mojo-specs

How to deploy code changes to the production environment?
---------------------------------------------------------

The code changes must be made on a branch based on the ``master`` branch
and a merge proposal with the changes must be submitted to the ``master``
branch.

If the code changes require some related database changes, those must be
deployed to production and merged back to the ``master`` branch before
the code changes can be merged to the ``master`` branch.

Similar to the process for deploying the database patch, there is a landing
bot to merge the approved code merge proposals to the ``master`` branch.
After that, buildbot runs the full Launchpad test suite on the ``master``
branch and if it passes, the new changes get merged to the ``stable`` branch.

Once this is done, the changes show up on the `launchpad deployable page`_
and there is a periodic cron job that automatically deploys the new changes
in the ``stable`` branch to the ``qastaging`` environment.

The code changes must be tested and verified in the ``qastaging`` environment
the related commits must be marked as deployable in the deployable site.

Then the changes can be deployed to the production environment by following the
instructions in the `nodowntime deployment process documentation`_.

.. _launchpad deployable page: https://deployable.ols.canonical.com/project/launchpad
.. _nodowntime deployment process documentation: https://canonical-launchpad-admin-manual.readthedocs-hosted.com/en/latest/howto/launchpad-rollout/launchpad-deployments/code-deployment/

What is the ``nodowntime`` deployment process?
----------------------------------------------

Code changes can be deployed to the Launchpad production environment without
causing any user-visible downtime. That is why the process is called the
``nodowntime`` deployment process. This is achieved by deploying the new code
on all the Launchpad units and performing a coordinated rolling restart of the
Launchpad appserver units.
