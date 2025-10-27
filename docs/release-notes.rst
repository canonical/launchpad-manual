Release Notes
=============

October 2025
++++++++++++
27 October 2025

- Webhooks can now be configured on archives for successful or unsuccessful
  source and binary package uploads, and binary build events.

17 October 2025

- Support for the ``core26`` snap base has been enabled and recipes
  can use it.

September 2025
++++++++++++++
1 September

- The 'Use Fetch Service' and 'Fetch Service Policy' options are
  available for charms via the API and the Edit recipe page.

August 2025
+++++++++++
21 August

- The 'Use Fetch Service' and 'Fetch Service Policy' options are
  available for rocks and sourcecraft packages via the APIs.

5 August

- The 'Use Fetch Service' button for snaps has been moved from
  Administer recipe to Edit recipe.

July 2025
+++++++++
30 July

- Update appserver log rotation from daily to hourly
- Fixed `#2032180 The parse-ppa-apache-access-logs.py script should report an error parsing a log line just once <https://bugs.launchpad.net/launchpad/+bug/2032180>`_.

11 July

- Launchpad no longer supports the creation of new mailing lists. For more
  information, please refer to this `announcement
  <https://blog.launchpad.net/general/sunsetting-launchpads-mailing-lists>`_.

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
