.. _launchpad-web-services-api:

Launchpad web services API
==========================

.. include:: /includes/important_not_revised_help.rst

The Launchpad website lets you learn about and manage bugs, projects,
questions, and other artefacts of software development. These same
objects are gradually being exposed through a web service, so that you
can access them from scripts, applications, or other websites, in
addition to accessing them through the Launchpad website. The service is
designed around the principles of REST, with the goals of simplicity and
transparency.

-  If you're the end-user of an application like Ground Control, you don't need to know about the API at all: you just need to know :ref:`how to integrate your Launchpad account with a third-party application <use-the-python-api>`.

-  :ref:`launchpadlib` is the official Python client
   library for Launchpad's web service.

    ::

        >>> me = launchpad.me
        >>> me.display_name = 'My new display name'
        >>> me.lp_save()

-  Developers who aren't Python programmers, or who are interested in
   the inner workings of the web service, should read :ref:`the hacking document <developing-the-launchpad-project>`.

    ::

        PATCH /beta/+me HTTP/1.1
        Host: api.launchpad.net
        Content-type: application/json

        { "display_name" : "My new display name" }

-  See our directory of :ref:`code that uses the Launchpad APIs <table-of-applications-using-the-api>` for examples. Also, we have a page of :ref:`example code <use-the-python-api>`.

-  If you're writing your own interface to Launchpad, instead of using
   launchpadlib, you'll need to know how `OAuth <http://oauth.net/>`_
   works. :ref:`Signing Requests <sign-web-requests>` explains how to
   walk your end-users through the process of getting a set of OAuth
   credentials that you can use to make Launchpad web service requests
   on their behalf.

-  The `reference documentation <http://launchpad.net/+apidoc/>`_
   describes every published object and operation in a language-neutral
   form.

Find out more:

.. toctree::
   :maxdepth: 1

   Sign web requests <launchpad-web-signing>
   Webhooks <webhooks>

Further reading
---------------
For more information on this topic, check out our in-depth explanation of the 
:ref:`Launchpad web service <launchpad-web-service>`.