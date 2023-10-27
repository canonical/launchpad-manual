Submitting a Patch to launchpad
===============================

.. include:: ../includes/important_not_revised.rst

Below we describe the process of getting a code change into Launchpad.

You should

- [[Getting|have the Launchpad sources]]
- be able to [[Running|build and run]] Launchpad
- and be familiar with the [[StyleGuides|coding style guidelines]].

Note that by **patch**, we just mean a code change, not an actual patch file
meant for the `patch`_ program.
In Launchpad, patches are typically delivered as Git branches hosted on
Launchpad itself; see below for details.

.. _patch: http://en.wikipedia.org/wiki/Patch_(Unix)

1. Before making your change, you need to talk about it first to a Launchpad
   developer. The easiest way there is to ask the person listed as the on-call
   reviewer (OCR) in the [[irc://irc.libera.chat/launchpad-dev|#launchpad-dev]]
   IRC channel on ``irc.libera.chat``.
   That "pre-implementation chat" will make sure that you have all things
   covered. If your proposal involves UI changes, you might even want to make
   screenshots or a [[ScreenCasts|screencast]].
2. Make sure you've installed the :ref:`pre-commit git hook <pre-commit>`.
   This performs various style and static analysis checks on your commits.
3. Make sure your change is about one single thing, say, a specific bugfix, and
   that all the revisions for it are committed on your Git branch.
4. Push the branch up to your Launchpad user account.
   Run this with your local copy of the branch as your current directory:
   ``git push <remote> <branch name>``
5. [[Testing|Run tests]] on your branch.
   If the tests don't pass, go back to hacking, commit new changes, re-push,
   and re-test. Repeat until the branch passes.
6. Please send in your `contributor agreement`_.
   We can't accept the change without a contributor agreement.
7. Propose your branch for merging, by going to
   https://code.launchpad.net/~<username>/launchpad/+git/launchpad/+ref/bugfix123
   and click on **Propose for merging into another branch**.
   (The repository to merge into is `lp:launchpad`, the branch is `master`.)
8. If there's a bug report for your branch, make sure the bug is linked to the
   branch. If there isn't, file a bug, and link that to the branch.
9. The Launchpad developers will get notified of the merge proposal and review
   it when time permits.
10. Once the reviewer approves the change, they'll take care of
    [[LandingChanges|merging your changes]].
11. Once the branch lands and is deployed to qastaging, test it there,
    verifying that the change works as expected and doesn't introduce any
    regressions. See [[PolicyAndProcess/QAProcess]].

.. _contributor agreement: http://www.canonical.com/contributors
