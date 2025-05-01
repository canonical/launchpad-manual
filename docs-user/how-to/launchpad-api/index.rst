Launchpad web services API
==========================

The Launchpad website lets you learn about and manage bugs, projects,
questions, and other artefacts of software development. These same
objects are gradually being exposed through a web service, so that you
can access them from scripts, applications, or other websites, in
addition to accessing them through the Launchpad website. The service is
designed around the principles of REST, with the goals of simplicity and
transparency.

-  If you're the end-user of an application like Ground Control, you
   don't need to know about the API at all: you just need to know `how
   to integrate your Launchpad account with a third-party
   application <API/ThirdPartyIntegration>`__.

.. raw:: html

   <!-- end list -->

-  `launchpadlib <API/launchpadlib>`__ is the official Python client
   library for Launchpad's web service.

.. raw:: html

   <!-- end list -->

::

      >>> me = launchpad.me
      >>> me.display_name = 'My new display name'
      >>> me.lp_save()

-  Developers who aren't Python programmers, or who are interested in
   the inner workings of the web service, should read `the hacking
   document <API/Hacking>`__.

.. raw:: html

   <!-- end list -->

::

      PATCH /beta/+me HTTP/1.1
      Host: api.launchpad.net
      Content-type: application/json

      { "display_name" : "My new display name" }

-  See our directory of `clients <Clients>`__ and `code that uses the
   Launchpad APIs <API/Uses>`__ for examples. Also, we have a page of
   `example code <API/Examples>`__.

.. raw:: html

   <!-- end list -->

-  If you're writing your own interface to Launchpad, instead of using
   launchpadlib, you'll need to know how `OAuth <http://oauth.net/>`__
   works. `Signing Requests <API/SigningRequests>`__ explains how to
   walk your end-users through the process of getting a set of OAuth
   credentials that you can use to make Launchpad web service requests
   on their behalf.

.. raw:: html

   <!-- end list -->

-  The `reference documentation <http://launchpad.net/+apidoc/>`__
   describes every published object and operation in a language-neutral
   form.

.. toctree::
   :hidden:
   :maxdepth: 2

   Access web services <launchpad-web>
   Sign web requests <launchpad-web-signing>
   Webhooks <webhooks>

