.. meta::
   :description: Guide to hosting your project's code on Launchpad with Git 
      repositories.

.. _host-your-project-code-on-launchpad:

Host your project's code on Launchpad
=====================================

You can host your project's source code on Launchpad using Git. If you're new
to Git, take a look at this `Git tutorial <https://gitimmersion.com/>`_ first.

When you push a Git repository to Launchpad, it is associated with a project
registered in Launchpad. Other people can then clone it, make changes, and push
their own branches back to Launchpad.

This guide shows you how to:

-  tell the world your project uses Launchpad to host its source code,
-  push your first Git repository to Launchpad,
-  hand the repository over to a team so that several people can push code to
   it.

.. note::

    Launchpad is free of charge for :ref:`open source projects <project-eligibility>`.
    To host non-open code on Launchpad, check out this doc on :ref:`consumer hosting <consumer-hosting>`.

Enable code hosting for your project
-------------------------------------

First, :ref:`add your project to Launchpad <how-to-register-your-project>`.

Once you've done that, visit your project's overview page. There, you'll find a
``Configuration progress`` section in the right-hand column. Click ``Code`` and
either select an existing repository or set up a new one.

Push a Git repository to your project
--------------------------------------

You can push and pull code from Launchpad directly from the terminal. If you
haven't already, `add your SSH key to Launchpad <https://launchpad.net/people/+me/+editsshkeys>`_ first.

To push your repository to Launchpad, open your terminal, navigate to your
local Git repository, add the Launchpad remote, and push:

::

   git remote add origin git+ssh://username@git.launchpad.net/~username/project-name
   git push -u origin branch-name

-  ``username``: your Launchpad ID, which is the portion of
   `your profile page <https://launchpad.net/people/+me>`_ URL that begins
   with the tilde (``~``)
-  ``project-name``: the Launchpad ID of your project; this is the final part
   of your project overview page's URL, e.g. ``launchpadlib`` in
   `<https://launchpad.net/launchpadlib/>`_
-  ``branch-name``: the name of the branch you want to push, such as ``main``

See your repository in Launchpad
----------------------------------

Once the push completes, Launchpad will scan the repository and:

-  list it on both `your own code overview page <https://code.launchpad.net/people/+me>`_
   and your project's code page,
-  allow other people to clone the repository and create their own branches,
-  make the full commit history available under the ``Code`` tab.

Let several people push to the repository
------------------------------------------

If you want to allow more than one person to push to the repository, you'll
need to :ref:`create a team <creating-and-running-launchpad-teams>` and make
that team the repository's owner.

Go to your project's overview page (``https://launchpad.net/project-name``).
Under ``Project information``, click the edit icon next to ``Maintainer``. In
the form that opens, set ``Maintainer`` to the team you created and save.

Next steps
----------

You're now hosting your project's code on Launchpad. Anyone can clone your
repository, make changes, and push their own clone's branch for listing on your
project's code page. Other people can also propose merging their branches into
your default branch or any other branch in your repository.

Read the full guide to :ref:`working with merge proposals <create-and-manage-a-merge-proposal>`.
