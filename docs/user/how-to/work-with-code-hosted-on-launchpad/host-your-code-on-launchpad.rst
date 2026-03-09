.. meta::
   :description: Guide to hosting your project's code on Launchpad with Git 
      repositories.

.. _host-your-project-code-on-launchpad:

Host your project's code on Launchpad
=====================================

You can host your project's source code using Launchpad and Git. If you're new
to Git, or distributed version control in general, take a look at this
`Git tutorial <https://gitimmersion.com/>`_ first.

When you push a Git branch to Launchpad, it's usually associated with a project
that's also registered in Launchpad. Other people can pull your Git branch,
modify it, and push their own version back to Launchpad for everyone to see.

This guide shows you how to:

-  tell the world your project uses Launchpad to host its source code,
-  push your first Git branch to Launchpad,
-  set that branch as your project's development focus -- i.e. ``trunk``,
-  hand the branch over to a team, so several people can commit code to
   it.

.. note::

    Launchpad is free of charge for :ref:`open source projects <project-eligibility>`.
    To host non-open code on Launchpad, check out this doc on :ref:`consumer hosting <consumer-hosting>`.

Enable code hosting for your project
------------------------------------

First, :ref:`add your project to Launchpad <how-to-register-your-project>`.

Once you've done that, visit your project's overview page. There, you'll find a
``Configuration progress`` section in the right-hand column. Click ``Code`` and
either select an existing branch or set up a new one.

Push a Git branch to your project
------------------------------------

You can push and pull code in Launchpad directly from the terminal after
`adding your SSH key to Launchpad <https://launchpad.net/people/+me/+editsshkeys>`_.

To push your branch, open your terminal, checkout to your Git branch, set up the
remote, and push:
::

   git remote add origin git+ssh://username@git.launchpad.net/~username/project-name
   git push -u origin branch-name

-  ``username``: your Launchpad ID, which is the portion of `your profile page <https://launchpad.net/people/+me>`_ 
   URL that begins with the tilde (~)
-  ``project-name``: the name of the project in Launchpad
-  ``branch-name``: whatever name you want to give to your branch, such as
   ``trunk``, ``main``, or ``experimental``

Replace ``project-name`` with your project's Launchpad ID. The ID is the
final part of your project overview page's URL. For example, ``launchpadlib``
in `<https://launchpad.net/launchpadlib/>`_.

See your branch in place
------------------------

Once Git has pushed your branch to Launchpad, Launchpad will scan the
revisions in your branch and:

-  list the repository on both `your own code overview page <https://code.launchpad.net/people/+me>`_ 
   and that of the project,
-  enable other people to download the branch and create their own version of
   it,
-  make the full revision history available in the ``Code`` tab.

Let several people commit to the branch
---------------------------------------

If you want to allow more people to push code to the branch, you'll need to
:ref:`create a team <creating-and-running-launchpad-teams>` and make that team 
the branch's owner.

Go to your project's code page, select the repository you want to change,
select ``Change repository details``, change ``Owner`` to the new team, and
save the changes.

Next steps
----------

You're now hosting your project's code in Launchpad! Anyone can download your
code, make some changes, and upload their branch for listing on your project's
code page. Other people can also propose merging their branches into your trunk
or any other branch associated with your project.

Read the full guide to :ref:`working with merge proposals <create-and-manage-a-merge-proposal>`.
