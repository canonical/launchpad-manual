====================
Contributing changes
====================

This guide shows you how to contribute a change to Launchpad.

Discuss the change
------------------

To begin with, it is usually helpful to discuss the change you'd like to make,
in a `bug`_, in the `launchpad-users`_, or `launchpad-dev`_ mailing lists,
or on IRC (``#launchpad-dev`` on ``irc.libera.chat``).

.. _bug: <https://bugs.launchpad.net/launchpad>
.. _launchpad-users: <https://launchpad.net/~launchpad-users> 
.. _launchpad-dev: <https://launchpad.net/~launchpad-dev>

Get the Launchpad source
----------------------------

Once you have decided on the change to be made, clone the repository.

.. code-block:: bash

    git clone https://git.launchpad.net/launchpad

Make your changes
-------------------

Create a branch from a reasonable point, such as ``master``.

.. code-block:: bash

    git checkout -b my-change

Make your changes on the branch. Be sure to test them locally by setting up a
local `Launchpad development instance`_.

.. _Launchpad development instance: <https://launchpad.readthedocs.io/en/latest/how-to/running.html>

Run the pre-commit hook
-----------------------

If you followed the instructions to `set up and run Launchpad`_, you should
already have ``pre-commit`` installed and have the ``pre-commit`` git hook
`installed`_. If not, complete these steps before proceeding.

.. _set up and run Launchpad: <https://launchpad.readthedocs.io/en/latest/how-to/running.html#>
.. _installed: <https://launchpad.readthedocs.io/en/latest/how-to/running.html#installing-the-pre-commit-hook>

Push your changes
--------------------

Once you are happy with your changes, stage and commit them, and then push to a
personal repository.

Next, you need to share your changes with the Launchpad maintainers, but you
probably don't have permissions to push to the ``master`` branch of the
Launchpad codebase. To share your changes with the Launchpad maintainers, you
need to push your commit to a personal git repository.

Create a merge proposal
-----------------------

Once your commit has been pushed to a personal git repository, you can follow
the direct link in the post-push message to create a merge proposal.
Alternatively, in a web browser, visit 

.. code-block:: bash

    https://code.launchpad.net/~<username>/+git

Remember to replace your username in the URL.

Navigate to the personal repository to which you pushed your changes, and then
to the branch containing your commit.

Select ``Propose for merging``, provide a reasonable commit message, and
description of your changes.

What comes next?
----------------

Once you have created a merge proposal, a Launchpad maintainer will inspect
your commit and approve or reject the changes. There may be a comments that
require you to make amendments to your proposed changes, which you can do by
repeating this workflow. However, once your changes are approved, your changes
will be merged into the ``master`` branch of the Launchpad code base!
