
.. _create_job_to_publish_artifacts:

==============================
Create job to publish artifact
==============================

Often we need to publish our project's artifacts so they can be accessed by
other entities. When building a charm with the ``launchpad-base layers``, for
example, you will want your code to be published in Swift as a tarball, so
that the right version of your code is downloaded when building the charm.

We also want the artifact building to be automated. This can be achieved by
having `Jenkins <https://jenkins.ols.canonical.com/online-services/>`_ jobs
building your artifact on code merge.


-------------
Steps to take
-------------

1. **Open an IS ticket to create Swift credentials for your new project**

   * Your new `IS ticket <https://portal.admin.canonical.com/requests/new>`_
     should go into the
     `Launchpad queue <https://portal.admin.canonical.com/q/launchpad/>`_, have
     a title along the lines of `"Swift credentials for <project name> builds"`
     and have information along the lines of:

        `"We need a new Swift user and a project whose credentials we'll
        use in a Jenkins job to build deployment artifacts and publish them to
        Swift. The user can be named 'stg-<project name>-builds'
        and the project 'stg-<project name>-builds_project'."`

     Open this ticket as early as possible since it might take a while until
     IS can go through it (if you need to speed up the turnaround, you might
     want to prioritize the ticket).


2. **Create 'build-tarball' and 'publish-tarball' commands in your project's
   Makefile**

   * The ``build-tarball`` command should rebuild the virtual environment anew,
     create a wheel with all the necessary dependencies, and then build a
     tarball into a given path (``build/<commit-id>/<name-of-tar>.tar.gz`` for
     example) - see existing examples in the Launchpad suite!

   * For the publishing, copy ``publish-to-swift.py`` script (found in a few
     Launchpad projects including Launchpad itself) to your project's
     directory. The ``publish-tarball`` command should be dependent on
     ``build-tarball`` and should run the ``publish-to-swift`` script - again
     see existing examples.

3. **Create or update jenkins job to run the publishing command**

   * Check if there is already a file for your project within the
     `ols-jenkaas <https://code.launchpad.net/ols-jenkaas>`_ repo in the
     ``/jobs`` folder. If there isn't, create one based on an existing one.

   * The important sections to make the job publish your tarball are the
     ``build-command`` - it should run your ``make publish-tarball`` command -
     and the ``jobs`` list, which should have at least the
     ``{name}-build-charm`` and ``trigger-{name}-build-charm-on-changes``.

4. **Get the new credentials into Jenkins**

   * Someone responsible for Jenkins (ask IS or your team who that person is)
     will need to add the new credentials IS created to your Jenkins jobs.
   * To get the new credentials that IS created, you should SSH into
     ``launchpad-bastion-ps5``, assume the new role created by IS, and there
     will be a ``README`` file with some guidelines. You'll see there that you
     can simply run ``load_creds openstack`` to load your credentials into
     environment variables. To share them with the person responsible,
     ask them what they might need. The most relevant credentials are
     ``OS_USERNAME``, ``OS_TENANT_NAME`` and ``OS_PASSWORD``.
