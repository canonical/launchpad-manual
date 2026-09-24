.. meta::
   :description: Propose a branch for merging while using a separate branch
      as a prerequisite for a cleaner diff.

.. _create-merge-proposal-with-prerequisite-branch:

Create a merge proposal with a prerequisite branch
==================================================

When your branch builds on changes in another branch that has not been merged,
proposing it for review shows both sets of changes in the same diff. Marking
the first branch as a *prerequisite* keeps those changes out of your diff,
so reviewers see only your work.

This guide assumes you are already familiar with creating merge proposals on
Launchpad; if not, start with :ref:`create-and-manage-a-merge-proposal`.

Before you start
----------------

- You should have a branch that is based on another branch, i.e., the commits
  in it sit on top of the other branch's commits.
- Both branches should already be pushed to Launchpad.
- If you intend to use the Web service API, you must have ``launchpadlib``
  installed.

Propose the merge with a prerequisite
-------------------------------------

.. tab-set::

    .. tab-item:: Web interface

        #. Go to your branch's page under `code.launchpad.net <https://code.launchpad.net>`_.
        #. Select :guilabel:`Propose for merging`.
        #. Choose the branch you want to merge into as the target, for example
           ``main``.
        #. Set :guilabel:`Prerequisite Git branch` to the branch with only the
           first set of changes. Its changes will be excluded from the diff.
        #. Optionally, add a description and pick a reviewer, then propose the
           merge.

    .. tab-item:: Web service API

        To create the proposal with ``launchpadlib``, use ``merge_prerequisite``:

        .. code-block:: python

            from launchpadlib.launchpad import Launchpad

            lp = Launchpad.login_with("my-app", "production", version="devel")

            repo = lp.git_repositories.getByPath(path="~you/project/+git/project")
            source = repo.getRefByPath(path="refs/heads/new-branch")
            target = repo.getRefByPath(path="refs/heads/main")
            prerequisite = repo.getRefByPath(path="refs/heads/prerequisite-branch")

            mp = source.createMergeProposal(
                merge_target=target,
                merge_prerequisite=prerequisite,
                needs_review=True,
                commit_message="Add new feature",
                initial_comment="Depends on prereq-branch landing first.",
            )
            print("Proposal created:", mp.web_link)

Preview your changes
--------------------

When you open the merge proposal on the web UI:

#. Only files edited in the second/dependent branch will be shown
#. In case both branches edit the same file, you may also see changes from the
   prerequisite branch, but they will not be highlighted as having been changed.

You can also verify this using the API:

.. code-block:: python

    >>> mp.preview_diff.diffstat
    {'some_file.py': (12, 0)}

Only files changed in the second branch are returned, and the line counts for
what was added and what was removed only counts changes in the dependent branch.

Launchpad also links your proposal from the prerequisite branch's page as a
dependent landing. The link remains until your proposal reaches a final state
(for example, merged or rejected).

.. code-block:: python

    >>> [d.web_link for d in prerequisite.dependent_landings]
    ['https://code.launchpad.net/~you/project/+git/project/+merge/123456']
