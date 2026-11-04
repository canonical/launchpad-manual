.. meta::
   :description: Understand how Launchpad automatically builds and tests your
      merge proposals against git-ubuntu repositories.

.. _merge-proposal-validation-workflow:

Merge proposal validation workflow
==================================

Getting a change into Ubuntu with ``git-ubuntu`` traditionally involves a long
sequence of manual steps: create a PPA, do a source build, upload it, wait for
the packages to build and publish, trigger autopkgtests on every architecture,
and only then propose the merge and iterate until everything passes.

The merge proposal validation workflow automates the build, upload and testing
steps so that they happen for you as soon as you open a merge proposal. Instead
of preparing everything by hand before requesting a review, you create the merge
proposal first and Launchpad takes care of the rest.

.. note::

   This feature is being rolled out gradually. During the initial rollout it is
   enabled per distribution through feature flags and limited to an allowlist of
   users, so it may not yet be available for your repository.

What the workflow does
----------------------

When you create a merge proposal against the default branch of a distribution
source package repository, Launchpad automatically:

1. Creates a new PPA owned by you (the merge proposal registrant).
2. Builds the source package from the proposed branch and uploads it into that
   PPA.
3. Waits for the packages to build and publish.
4. Triggers autopkgtests on all architectures that built successfully.

If you push new commits to the proposed branch, new builds and autopkgtests are
triggered automatically. Throughout the process, the current status is reported
back to you directly on the merge proposal page.

Why this approach
-----------------

The workflow is built directly into Launchpad rather than as an external
service. This tight integration lets Launchpad create the PPA on your behalf,
hook into native events such as merge proposal creation and build status
changes, and surface status and controls as first-class elements of the merge
proposal UI instead of relying on comments or external tooling.

How it works
------------

The workflow is driven by Launchpad's native subscription mechanism and a small
set of internal jobs.

Trigger and eligibility
~~~~~~~~~~~~~~~~~~~~~~~~

Creating a merge proposal starts the workflow, but only when all of the
following are true:

- The target repository is the default repository for a distribution source
  package.
- The merge proposal, source, and target repositories are all public.
- The distribution is enabled for validation (via a feature flag).
- During the initial rollout, the registrant is on the allowlist.

If any of these checks fail, the workflow does not run. Private branches or
repositories never trigger the workflow.

Launchpad also watches for state changes. If the merge proposal becomes
``Merged``, ``Rejected``, or ``Superseded``, or is deleted, all running builds
and tests are cancelled and the external autopkgtest watches are removed.

Creating the PPA
~~~~~~~~~~~~~~~~

A new public PPA is created with a name of the form ``mp-<id>-<attempt>`` and is
owned by you. Because you own it, you can retrigger builds and manage the PPA
directly in the UI. All supported architectures and the proposed pocket are
enabled by default, and the PPA uses the standard default size.

Building the source package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad builds the source package from the proposed git branch using a new
build type, reconstructing the original tarball where necessary and uploading
the result into your PPA. Each build appends a unique, timestamped suffix to the
changelog version so that repeated builds can be published to the same archive
without version clashes. As the build moves through its stages (queued,
building, uploading, failed, or success), the status is recorded and shown on
the merge proposal page.

Running and collecting autopkgtests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a binary is published, Launchpad submits an autopkgtest run for the built
package (plus any additional triggers you specified) to the autopkgtest
infrastructure. Because autopkgtest runs can take anywhere from minutes to days,
results are collected by a cron-based poller rather than by a long-running job.
The poller periodically fetches the status of each pending run and updates the
merge proposal accordingly.

Status and interactions
~~~~~~~~~~~~~~~~~~~~~~~~

The overall status is displayed at the top of the merge proposal page, and you
can act on it directly:

- **Retry tests** resubmits the autopkgtests.
- **Rebuild** produces a new source build (with a new version suffix) into the
  same PPA and runs fresh tests once the builds succeed.
- **Cancel** cancels pending jobs and dispatched builds.

These controls are available to the merge proposal registrant, the source
repository owner, and anyone with edit permissions on the target repository.

Cleanup
~~~~~~~

PPAs created by the workflow are not automatically removed. Because you own
them, you can keep archives you still need or delete them yourself at any time.

See also
--------

- :ref:`Create and manage a merge proposal <create-and-manage-a-merge-proposal>`
- :ref:`Continuous integration <continuous-integration>`
- :ref:`Use the merge proposal validation workflow <use-merge-proposal-validation-workflow>`
- :ref:`Merge proposal workflow parameters <merge-proposal-workflow-parameters>`
