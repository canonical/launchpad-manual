.. meta::
   :description: Coding conventions and service reference for Launchpad developers.

Reference
=========

Launchpad is composed of a monolith plus different services with distinct
functions such as handling builds, code hosting, signing, translations,
mirroring, and more. As a contributor working on any part of Launchpad, you
are expected to follow certain conventions and standards in your work.

Build-related services
----------------------
Build-related services descriptions and resources.

- :ref:`Build farm <build-farm-reference>`
- :ref:`Signing service <signing-service>`
- :ref:`Fetch service <fetch-service>`
- :ref:`Buildbot <buildbot-reference>`

Code imports and hosting
------------------------
Code hosting and code import resources.

- :ref:`Git hosting <git-hosting-reference>`
- :ref:`Code import <code-import-reference>`

Translation
-----------
Schedule of automatic translations tarball exports from Launchpad.

- :ref:`Automatic translations tarball exports <automatic-translations-export>`

Interactive testing of Email processing
---------------------------------------
Email processing configuration options and testing.

- :ref:`Launchpad and email <email-reference>`

Ubuntu-related services
-----------------------
Scanning for Ubuntu mirrors and checking their health. 

- :ref:`Mirror prober <mirror-prober-reference>`
- :ref:`Ubuntu mirrors index <ubuntu-mirrors-index>`

Mailing lists (archived)
------------------------

Launchpad mailing lists are no longer active, but the archives remain
accessible.

- :ref:`Launchpad public mailing lists archives <mailing-lists-archives>`

Authentication
--------------

Mechanisms for authenticating to Launchpad's API.

- :ref:`Hardware-bound API tokens <hardware-bound-api-tokens-reference>`

Code conventions
----------------

Launchpad follows established conventions for Python, CSS, tests, and bug
tagging. These standards are enforced during code review.

- :ref:`Python style guide <python-style-guide>`
- :ref:`Tests style guide <tests-style-guide>`
- :ref:`CSS style guide <css-style-guide>`
- :ref:`Tagging bugs about Launchpad <tagging-bugs-about-launchpad>`


.. toctree::
   :hidden:

   hardware-bound-api-tokens
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

   

