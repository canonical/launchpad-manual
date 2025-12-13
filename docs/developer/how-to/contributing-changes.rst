.. _contributing-changes:

Contributing changes
====================

This guide shows you how to contribute a change to Launchpad.

Discuss the change
------------------

To begin with, it is usually helpful to discuss the change you'd like to make,
in a `bug`_ or :ref:`directly with the Launchpad team <get-help>`.

.. _bug: https://bugs.launchpad.net/launchpad

Fork the Launchpad repository
-----------------------------

Navigate to the Launchpad project page and go to the "Code" tab.
https://code.launchpad.net/launchpad

Click "Fork it to your account" to create a copy of the project in your
Launchpad account.

Assuming you have added your SSH keys to launchpad, you can then clone your fork
of the repository:

.. code-block:: bash

    git clone git+ssh://~<your-username>@git.launchpad.net/~<your-username>/launchpad
    cd launchpad

Add the Launchpad repository as a remote
----------------------------------------

This will be useful to pull in changes from the main Launchpad repository.

.. code-block:: bash

    git remote add launchpad git+ssh://git.launchpad.net/launchpad

Make your changes
-----------------

Create a branch from a reasonable point, such as ``master``.

.. code-block:: bash

    git checkout -b <descriptive-branch-name>

Make your changes on the branch. Be sure to test them locally by setting up a
local :doc:`Launchpad development instance <running>`.

When it comes to commit messages, please follow these guidelines:

Commit title
~~~~~~~~~~~~

* Short, but descriptive
* Uses imperative wording, e.g. "Add character limit to bug title's summary
  field"
* Always starts with a capitalized word
* No dot at the end


Commit body
~~~~~~~~~~~
* Gives more context about the motivation of the change
* Line length should not exceed 72 characters for better readability, with the
  exception for hyperlinks
* Could contain a reference to a Launchpad bug, e.g. `LP: #2086655`


Run the pre-commit hook
-----------------------

If you followed the instructions to :doc:`set up and run Launchpad <running>`,
you should already have ``pre-commit`` installed and have the
:ref:`pre-commit git hook <pre-commit>` installed. If not, complete these steps
before proceeding.

Push your changes
--------------------

Once you are happy with your changes, stage and commit them, and then push to
your fork.

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

Once you have created a merge proposal, a Launchpad maintainer will inspect your
merge proposal and approve or reject the changes. There may be comments that
require you to make amendments to your proposed changes, which you can do by
repeating this workflow. However, once your changes are approved, your changes
will be merged into the ``master`` branch of the Launchpad code base!

Once your changes are merged into the ``master`` branch, they get deployed to
the QA staging site automatically. You can QA your changes there:
https://qastaging.launchpad.net/ 
