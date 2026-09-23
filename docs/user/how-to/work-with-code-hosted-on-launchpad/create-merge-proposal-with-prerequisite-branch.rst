.. meta::
   :description: Propose a branch for merging while using a separate branch
      as a prerequisite for a cleaner diff.

.. _create-merge-proposal-with-prerequisite-branch:

Create a merge proposal with a prerequisite branch
==================================================

When your branch builds on a teammate's branch that has not yet merged, proposing
it for review normally shows both your changes and your teammate's in the same
diff. Marking the teammate's branch as a *prerequisite* keeps their changes out of
your diff, so reviewers see only your work. Launchpad describes the field this way:
"If the source branch is based on a different branch, you can add this as a
prerequisite. The changes from that branch will not show in the diff."

This guide covers Git repositories. It assumes you are already comfortable
creating merge proposals; if not, start with
:ref:`create-and-manage-a-merge-proposal`.

Before you start
----------------

- Your source branch and your teammate's branch are both pushed to Launchpad in
  the same project repository.
- Your source branch is based on the teammate's branch — your commits sit on top
  of theirs.

Propose the merge with a prerequisite
-------------------------------------

.. tab-set::

    .. tab-item:: Web interface

        #. Go to your source branch's page under
           `code.launchpad.net <https://code.launchpad.net>`_.
        #. Select :guilabel:`Propose for merging into another branch`.
        #. Choose the branch you want to merge into as the target, for example
           ``main``.
        #. Set :guilabel:`Prerequisite Git branch` to your teammate's branch. Its
           changes will be excluded from the diff.
        #. Optionally add a description and request a reviewer, then propose the
           merge.

    .. tab-item:: Web service API

        Create the proposal with ``launchpadlib``, passing the teammate's branch
        as ``merge_prerequisite``:

        .. code-block:: python

            from launchpadlib.launchpad import Launchpad

            lp = Launchpad.login_with("my-app", "production", version="devel")

            repo = lp.git_repositories.getByPath(
                path="~you/project/+git/project")
            source = repo.getRefByPath(path="refs/heads/add-login-form")
            target = repo.getRefByPath(path="refs/heads/main")
            prerequisite = repo.getRefByPath(path="refs/heads/refactor-auth")

            mp = source.createMergeProposal(
                merge_target=target,
                merge_prerequisite=prerequisite,
                needs_review=True,
            )
            print(mp.web_link)

Confirm the diff excludes the prerequisite
------------------------------------------

Open the new proposal and check its review diff: only the files you changed
appear. The files changed on the prerequisite branch are absent.

To confirm the same through the API — reusing the ``mp`` and ``prerequisite``
objects from the :guilabel:`Web service API` example above — read the proposal's
diff summary. It maps each changed file to its ``(added, removed)`` line counts,
and lists only your files:

.. code-block:: python

    >>> mp.preview_diff.diffstat
    {'login.py': (12, 0)}

Launchpad also links your proposal from the prerequisite branch's page as a
dependent landing. The link remains until your proposal reaches a final state
(for example, merged or rejected).

.. code-block:: python

    >>> [d.web_link for d in prerequisite.dependent_landings]
    ['https://code.launchpad.net/~you/project/+git/project/+merge/123456']

.. seealso::

    - :ref:`create-and-manage-a-merge-proposal`
