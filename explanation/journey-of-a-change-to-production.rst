=========================================================================
The journey of a Launchpad change from a developer's branch to production
=========================================================================

##########
Characters
##########

* The Launchpad developer.
* Launchpad's branches.
* Launchpad itself.
* Jenkins jobs (https://jenkins.ols.ps5.canonical.com).
* Buildbot (http://lpbuildbot.canonical.com).
* Deployable (https://deployable.ols.canonical.com).
* Launchpad qastaging and staging environments.
* Scripts from the ``lp:launchpad-bastion-scripts`` repository.
* Juju and mojo
* Fragile Launchpad jobs
* Launchpad production environment

===========
The journey
===========

* **What type of change do I want to contribute to Launchpad? Does this involve
  any database schema changes?**

  Launchpad has 4 master branches, each with its own purpose and role (for more details, see :doc: `branches </explanation/branches>`_). If the change
  inolves making database schema changes along with some related code changes, the
  two have to done separately.

  The database changes should be targetting the ``db-devel`` branch whereas the code
  changes need to target the ``master`` branch. This is because database changes
  can be destabilising to other work, so we isolate them into a separate branch.
  Since Launchpad has a large database and codebase with strict uptime requirements,
  we want to deploy changes to only one of these at a time and this separation
  helps that as well.

* **If I need to separate the code and database changes, how do I get them in the
  same place to test them together?**

  The database changes need to go through a different journey to end up in the ``master``
  branch where the code changes get merged to. So it is important to start with the
  database schema changes first, get them reviewed and merged to the ``db-devel`` branch.
  Some types of database changes are applied through cold patches (with downtime) and other
  types of database changes are applied through hot patches. There are some differences
  between these and let us focus on the cold patches for the time being.

* **So what happens after the database schema changes submitted in a merge proposal, reviewed, and
  approved?**

  Once a database patch is approved and the status of the corresponding merge proposal is set
  to "Approved", a `Jenkins trigger <https://jenkins.ols.ps5.canonical.com/job/trigger-launchpad/>`_
  runs a `Jenkins job <https://jenkins.ols.ps5.canonical.com/job/launchpad/>`_ that checks for
  unmerged merge proposals that are approved, and merges them to their target branch. So this
  job will merge the approved database merge proposal. The Jenkins jobs are defined in the
  `ols-jenkaas-jobs <https://git.launchpad.net/ols-jenkaas-jobs>`_ repository.

* **Now my changes are merged, how can I deploy them to production?**

  There are multiple steps/processes that need to happen before a database patch can be
  deployed to production. Now that the database patch has been merged to the ``db-devel``
  branch, the ``lp-db-devel-focal`` job on buildbot runs the full Launchpad test suite
  on the ``db-devel`` branch. Once the tests pass, there is a cron job (TODO: add more details)
  that runs on the buildbot master unit which checks for new commits that have completed
  a successful buildbot run and merges them to the ```db-stable`` branch.

  Once this is done, the new commits to the ``db-stable`` branch that have not yet been
  deployed to production show up on the Deployable page, https://deployable.ols.canonical.com/projects/launchpad-db.

  There is yet another Jenkins job on the OLS Jenkins instance that checks for new commits
  to the ``db-stable`` branch and builds a new Launchpad payload for the latest revision in
  the ``db-stable`` branch, and publishes to Swift, at a well-known location whose path contains
  the hash of the commit that the tarball was built for.

* **How can I test my database schema changes before attempting to deploy them to production?**

  Launchpad as 2 pre-production environments, ``qastaging`` and ``staging``. The former is primarily
  used for testing code changes whereas the latter is used for testing the database changes.

  Launchpad is deployed using Juju charms using ``mojo``, a convenience wrapper around Juju that provides
  a lot of useful functionality. The ``mojo`` configuration for deploying Launchpad to various environments
  is defined in the ``lp:launchpad-mojo-specs`` repository, under the ``lp`` subdirectory. The ``bundle.yaml``
  file in that directory is a Jinja2 template that gets rendered to an appropriate Juju bundle.yaml for each
  environment. This ``bundle.yaml`` file contains 2 different ``build_label`` values - the hash of the ``stable``
  branch commit that is deployed to production and also the hash of the ``db-stable`` branch commit that is
  deployed to production.

  There is an ``auto-upgrade-staging`` script in the ``lp:launchpad-bastion-scripts`` repository that
  runs periodically on the launchpad bastion as the ``stg-launchpad`` user. It finds the latest
  undeployed commit in the ``db-stable`` branch and attempts to deploy it to the staging Launchpad environment.
  The scripts logs its output to a file like with a name like ``~/logs/2024-10-11-staging.log``.

  The Launchpad charms have a ``build_label`` configuration option, which accepts the hash of the
  commit to be deployed. The ``auto-upgrade-staging`` script adds local overrides for the production build label
  values and replaces them with the latest commit in the ``db-stable`` branch. It then attempts to
  deploy that using ``mojo``.

  The Launchpad mojo spec performs that Launchpad deployment in 3 stages. You can learn more about these stages,
  which applications are deployed in each stage and the reasons for doing so in
  https://git.launchpad.net/launchpad-mojo-specs/tree/lp/predeploy.

  Once this deployment completes successfully, all the Launchpad units in the staging environment have the latest
  changes from the ``db-stable`` branch. But the new database patches are not applied by the ``auto-upgrade-staging``
  script because its responsibility stops with updating the code.

  There is another script in the ``launchpad-bastion-scripts`` repository, ``staging-restore/staging_restore.sh``,
  which has a cron job in the bastion, that invokes it with an argument ``full``. This script does a lot of things
  including running the database update to apply any unapplied patches. It logs its output to a file with a name
  like ``~/logs/2024-10-11-staging_restore.log``.

  After your patch has been applied, you can find the time it took to apply it on staging from the above log file.
  This is very important to check and it should be under 10s.

  You can then proceed to the ``launchpad-db`` deployable queue and mark your database patch commit as deployable.
  Also mark all the auto-merge commits deployable. Since a database deployment should only deploy at most one
  patch, only verify and mark the commits till the first patch in the queue deployable. Additional patches, if any,
  should be deployed separately.

* **Can I deploy my patch to production now?**

  Yes. For that you have to follow the instructions in https://wiki.canonical.com/InformationInfrastructure/OSA/LaunchpadRollout#Fastdowntime_db_update. But before you do that
  here is a high-level explanation of how things are deployed in production and the process.

  In production, all units except the ``launchpad-db-update`` unit run the commit specified in the ``build_label`` commit
  without the ``-db`` suffix, that points to a commit from the ``stable`` branch. The ``launchpad-db-update`` unit runs
  code corresponding to the commit in the ``build_label`` configuration option with the ``-db`` suffix and this commit is
  from the ``db-stable`` branch.

  So before we can apply the new DB patch, we need to update the code on the ``launchpad-db-update`` unit to a commit on the
  ``db-stable`` branch that contains DB patch. This is done in the
  https://wiki.canonical.com/InformationInfrastructure/OSA/LaunchpadRollout#Prepare_code step.

  Then after performing the subsequent steps in that documentation, we run the pre-flight checks to ensure that there
  are no fragile Launchpad jobs running (examples: database backup, ftpmaster and PPA publishers, librarian-gc). Once
  the pre-flight checks pass, we apply the pending database patch by running the command that invokes the ``db-update``
  action on the production ``launchpad-db-update`` unit.

  When this command has finished execution, you will see log output indicating that the patch was applied and how long
  it took to apply.

  Proceed with the remaining steps in the ``fastdowntime`` deployment documentation and complete them. One of the last
  steps involves manually merging the deployed database commit back to the ``master`` branch. This is the step that
  brings the database patch changes back to the ``master`` branch where we target the code changes.

  Once this merge is done, ``lp-devel-focal`` buildbot run happens and if it passes, the merged changes get merged to
  the ``stable`` branch by the same cron job running on the ``buildbot`` master node.

* **So we merged the database changes from** ``db-stable`` **to** ``master`` **which brings the database patch to the** ``master``
  **branch. But how do we get the latest code changes to the** ``db-*`` **branches?**

  There is a periodic merge of the code changes from the ``stable`` branch back to the ``db-devel`` branch, which makes its
  way to the ``db-stable`` branch after a successfull buildbot run.

  **TODO:** Find and document what job does this.
