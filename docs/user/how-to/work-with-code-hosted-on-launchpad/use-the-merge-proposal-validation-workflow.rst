.. meta::
   :description: Step-by-step guide to automatically building Debian source
      packages in a PPA and running autopkgtests from a merge proposal on a
      git-ubuntu repository.

.. _use-merge-proposal-validation-workflow:

Use the merge proposal validation workflow
==========================================

Use this workflow to automatically build the Debian source package for your
proposed change in a PPA and run autopkgtests on it, straight from a merge
proposal against a git-ubuntu repository. Instead of building and uploading the
package to a PPA and triggering tests by hand, you open a merge proposal and
Launchpad does it for you.

This guide shows how to trigger the workflow, tune it with parameters, and act
on the results.

For background on what the workflow does and how it works, see
:ref:`Merge proposal validation workflow <merge-proposal-validation-workflow>`.

.. note::

   This feature is being rolled out gradually. During the initial rollout it is
   enabled per distribution through feature flags and limited to an allowlist of
   users, so it may not yet be available for your repository.

Before you begin
----------------

Make sure that:

- Your change targets the **default branch of a distribution source package**
  repository.
- The merge proposal, source, and target repositories are all **public**. The
  workflow never runs for private branches or repositories.
- The distribution is enabled for validation and, during the rollout, your
  account is on the allowlist.

Trigger the workflow
--------------------

1. Push your branch to Launchpad.
2. :ref:`Create a merge proposal <create-and-manage-a-merge-proposal>` against
   the target git-ubuntu repository.

That is all you need to do. As soon as the merge proposal is created, Launchpad
automatically:

1. Creates a new PPA named ``mp-<id>-<attempt>`` that **you** own.
2. Builds the source package from your proposed branch and uploads it to that
   PPA.
3. Waits for the packages to build and publish.
4. Triggers autopkgtests on every architecture that built successfully.

If you push more commits to the proposed branch, new builds and autopkgtests are
triggered automatically.

Configure the workflow with parameters
--------------------------------------

Some builds and tests need extra options that cannot be inferred automatically.
You can provide these as ``<key>: <value>`` lines at the end of the merge
proposal description. For example:

.. code-block:: text

   This merge proposal fixes the foo crash on startup.

   Autopkgtest-All-Proposed: True
   Autopkgtest-Trigger: bar/1.2-3

For the full list of supported keys and their meanings, see
:ref:`Merge proposal workflow parameters <merge-proposal-workflow-parameters>`.

.. tip::

   To opt a merge proposal out of the workflow once the feature is fully
   released, set ``Activate-Workflow: False`` in the description.

Follow the status
-----------------

The current status of the workflow is shown at the top of the merge proposal
page and updates as each step completes (queued, building, uploading, failed, or
success for builds, and the test results for autopkgtests).

Act on the results
------------------

You can control the workflow directly from the merge proposal page. These
actions are available to the merge proposal registrant, the source repository
owner, and anyone with edit permissions on the target repository.

- **Retry tests** – resubmit the autopkgtests, for example after a transient
  infrastructure failure.
- **Rebuild** – produce a new source build (with a new version suffix) into the
  same PPA and run fresh tests once the builds succeed. Use this after pushing
  changes that need a clean rebuild.
- **Cancel** – cancel pending jobs and dispatched builds.

Because you own the PPA, you can also retrigger builds and manage the archive
directly from its PPA page.

Clean up
--------

PPAs created by the workflow are not removed automatically. Keep any archive you
still need, or delete it yourself from the PPA page when you are done.

See also
--------

- :ref:`Merge proposal validation workflow <merge-proposal-validation-workflow>`
- :ref:`Merge proposal workflow parameters <merge-proposal-workflow-parameters>`
- :ref:`Create and manage a merge proposal <create-and-manage-a-merge-proposal>`
