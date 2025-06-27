Release Notes
=============

June 2025
+++++++++
27 June

- The `bzr` codebrowse interface (`loggerhead`) has been disabled and all codebrowse
  URLs will receive a '404 Not Found' response status code. Accessing `bzr`
  repositories using the `bzr` CLI tool via HTTP and SSH continues to work.

17 June

- Removed bzr codebrowse links on all pages that had them. This is in
  preparation for the upcoming shutdown of the loggerhead bzr codebrowse
  interface.

May 2025
++++++++
12 May

- New snaps, OCI recipes, and PPAs no longer build for i386 `by default <https://blog.launchpad.net/general/build_by_defaultfalse-for-i386>`_.
- Added new `webhook scopes <https://help.launchpad.net/API/Webhooks>`_ for merge proposal events.

5 May

- Adoption of `craft-platforms <https://canonical-craft-platforms.readthedocs-hosted.com/en/latest>`_:   supports multi-base platforms syntax for Charm builds and short-form platforms syntax for Snap builds in recipe configurations.
