.. meta::
   :description: Coding conventions and service reference for Launchpad developers.

Reference
=========

Launchpad contributors are expected to follow certain coding standards. You'll
also need technical reference material for services that make up the Launchpad
platform when making contributions.

Code conventions
----------------

Launchpad follows established conventions for Python, CSS, tests, and bug
tagging. These standards are enforced during code review.

- :ref:`Python style guide <python-style-guide>`
- :ref:`Tests style guide <tests-style-guide>`
- :ref:`CSS style guide <css-style-guide>`
- :ref:`Tagging bugs about Launchpad <tagging-bugs-about-launchpad>`

Services
--------

Launchpad is composed of many services that handle builds, code hosting,
signing, translations, mirroring, and more.

Build-related
~~~~~~~~~~~~~

- :ref:`Build farm <build-farm-reference>`
- :ref:`Signing service <signing-service>`
- :ref:`Fetch service <fetch-service>`
- :ref:`Buildbot <buildbot-reference>`

Email
~~~~~

- :ref:`Launchpad and email <email-reference>`

Git-related
~~~~~~~~~~~

- :ref:`Git hosting <git-hosting-reference>`
- :ref:`Code import <code-import-reference>`

Translation
~~~~~~~~~~~

- :ref:`Automatic translations tarball exports <automatic-translations-export>`

Ubuntu-related
~~~~~~~~~~~~~~

- :ref:`Mirror prober <mirror-prober-reference>`
- :ref:`Ubuntu mirrors index <ubuntu-mirrors-index>`

Mailing lists (archived)
~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad mailing lists are no longer active, but the archives remain
accessible.

- :ref:`Launchpad public mailing lists archives <mailing-lists-archives>`

   
.. toctree::
   :hidden:

   python
   tests
   css
   bug-tags
   services/build-farm
   services/signing
   services/fetch-service
   services/buildbot
   services/automatic-translations-export
   services/mirror-prober
   services/ubuntu-mirrors-index
   services/git-hosting
   services/code-import
   services/mailing-lists-archives
   email

   

