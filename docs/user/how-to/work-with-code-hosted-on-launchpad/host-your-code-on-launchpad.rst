.. _host-your-project-code-on-launchpad:

Host your project's code on Launchpad
=====================================

.. include:: /includes/important_not_revised_help.rst

You can host your project's source code using Launchpad and Bazaar. If
you're new to Bazaar, or distributed version control in general, take a
look at the `Bazaar mini-tutorial <http://doc.bazaar-vcs.org/bzr.dev/en/mini-tutorial/index.html>`_
first.

When you push a Bazaar branch to Launchpad, it's usually associated with
a project that's also registered in Launchpad. Other people can then get
hold of your Bazaar branch, modify it, and push their own version back
up to Launchpad for everyone to see.

This guide shows you how to:

-  tell the world your project uses Launchpad to host its source code
-  push your first Bazaar branch up to Launchpad
-  set that branch as your project's development focus -- i.e. ``trunk``
-  hand the branch over to a team, so several people can commit code to
   it.

.. note::

    Launchpad is free of charge for :ref:`open source projects <project-eligibility>`.
    To host non-open code on Launchpad, `read about commercial subscriptions <https://launchpad.net/+tour/join-launchpad#commercial>`_.

Enable code hosting for your project
------------------------------------

First, :ref:`add your project to Launchpad <how-to-register-your-project>`.

When you've done that, visit your your project's overview page. There
you'll find a ``Configuration progress`` section in the right-hand column.
Click ``Configure project branch`` and either select an existing branch or
set up a new one.

Push a Bazaar branch to your project
------------------------------------

Bazaar comes with a plug-in that lets you push to and pull from
Launchpad directly from within Bazaar.

If you haven't already, you need to perform a couple of one-time setup
tasks:

1. `add your SSH key to Launchpad <https://launchpad.net/people/+me/+editsshkeys>`_
2. and then log in to Launchpad from Bazaar by typing ``bzr
   launchpad-login`` in your terminal.

To push your branch up to Launchpad, open your terminal and go to your
Bazaar branch. Next up, type:

::

   bzr push lp:~your-id/project-id/branch-name

-  ``~your-id``: this is your Launchpad id, which is the portion of `your profile page <https://launchpad.net/people/+me>`_ URL that begins with the tilde
-  ``project-id``: the id of the project in Launchpad, which you can find
   at the end of your project's overview page URL
-  ``branch-name``: whatever name you want to give to your branch, such as
   ``trunk``, ``main``, or ``experimental``.

Replace ``project-name`` with your project's Launchpad id. The id is the
final part of your project overview page's URL: e.g. ``bzr`` in
`<https://launchpad.net/bzr>`_.

See your branch in place
------------------------

Once Bazaar has pushed your branch to Launchpad, Launchpad will scan the
revisions in your branch and:

-  list the branch on both `your own code overview page <https://code.launchpad.net/people/+me>`_ and that of the project. To get to each, select the "Branches" tab.
-  enable other people to download the branch and create their own version of it
-  make the full revision history available in the source-code tab.

Set your project's trunk branch
-------------------------------

You can tell Launchpad which of your project's branches is the current
focus of development; i.e. which is the trunk.

Setting a trunk branch is useful to:

-  tell people which branch they should download
-  define which branch Launchpad should provide when someone enters ``bzr branch lp:your-project``
-  act as the default target when someone proposes a merge
-  act as the basis for `stacked branches <http://doc.bazaar-vcs.org/bzr.dev/en/user-guide/index.html#using-stacked-branches>`_.

Visit your project's code overview page and follow the link inviting you
to set a development focus.

Let several people commit to the branch
---------------------------------------

If you want to enable several people to push code to the branch, you'll
need to :ref:`create a team <creating-and-running-launchpad-teams>` and make that the
branch's owner.

Go to your project main page (``https://launchpad/project-name``), select
the ``Branches`` tab, then click the branch nick link you wish to edit to
go to the ``branch overview page``. If you've followed the instructions
above, its nick will be ``lp:your-project``.

Once on the branch's overview page, you'll see an information box on the
right-hand side of the page. Click the pencil icon next to your name in
the ``Maintainer`` section to enter ``Change branch details`` page. Select
from the drop-down menu ``Maintainer`` the team that you want to own the
branch.

Next steps
----------

You're now hosting your project's code in Launchpad. Anyone can download
your code, make their changes and upload their branch for listing on
your project's code page. Other people can also propose there branches
for merging into your trunk, or any other branch associated with your
project.

Read the full guide to :ref:`working with merge proposals <create-and-manage-a-merge-proposal>`.
