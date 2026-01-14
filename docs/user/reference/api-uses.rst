.. _table-of-applications-using-the-api:

Table of applications using the API
===================================
.. include:: /includes/important_not_revised_help.rst


Below are programs that use the :ref:`Launchpad APIs <launchpad-web-services-api>` (usually through the :ref:`launchpadlib <get-started-with-launchpadlib>` Python interface) that you can use as examples if you're starting out with Launchpad API programming. See also the :ref:`API Examples <use-the-python-api>` page, which contains code snippets specifically meant as examples, the `Clients <https://blog.launchpad.net/tag/api-clients>`_ page (into which this page should probably be merged), and the `Launchpad Extensions (lpx) <https://launchpad.net/lpx>`_ project group.

.. list-table::
   :header-rows: 1

   * - Program
     - Purpose
     - Notes
   * - `Launchpadlib "contrib" scripts <https://launchpad.net/launchpadlib/>`_
     - Various scripts shipped with Launchpadlib, meant both as examples and as real-world tools.
     - In particular, see `lp-bug-ifier.py <http://git.launchpad.net/launchpadlib/tree/contrib/lp-bug-ifier.py?id=d637505d4f12a2da0f974639e779bbcc6bad87e4>`_ (expands raw bug numbers to show the bug summaries as fetched from Launchpad)
       and `close_bugs_from_commits.py <https://git.launchpad.net/launchpadlib/tree/contrib/close_bugs_from_commits.py?id=d637505d4f12a2da0f974639e779bbcc6bad87e4>`_ (the name is self-explanatory).
   * - `bughugger <https://launchpad.net/bughugger>`_
     - Py Gtk Client for Ubuntu bugs in Launchpad. Currently supports listing bugs by team, user, and package. Supports plugins for changing bugs.
     - Still in development, join ~bughuggers
   * - `apport <http://launchpad.net/apport>`_
     - A crash detection system that automatically generates reports with debugging information from crashed programs and provides UI frontends for handling these reports.
     - See the script `apport-collect <https://git.launchpad.net/apport/tree/debian/local/apport-collect?id=02996dc1f74c1241e5e9f459ec2cff40ae68a175>`_, which adds apport data to existing bug reports.
   * - `ubuntu-dev-tools <http://wiki.ubuntu.com/UbuntuDevTools>`_
     - A collection of useful tools that Ubuntu developers use to make their packaging work a lot easier (bug filing, packaging preparation, package analysis, etc).
     - See the `manage-credentials <https://git.launchpad.net/ubuntu-dev-tools/tree/manage-credentials?id=da7a71e54f86e4cf17ed140d23a5ace308c5a98c>`_, `requestsync <https://git.launchpad.net/ubuntu-dev-tools/tree/requestsync?id=da7a71e54f86e4cf17ed140d23a5ace308c5a98c>`_, `massfile <https://git.launchpad.net/ubuntu-dev-tools/tree/massfile?id=da7a71e54f86e4cf17ed140d23a5ace308c5a98c>`_, `lp-set-dup <https://git.launchpad.net/ubuntu-dev-tools/tree/doc/lp-set-dup.1?id=af1d20f51e193fb033eca290b548e1bceac54ace>`_, `grab-attachments <https://git.launchpad.net/ubuntu-dev-tools/tree/doc/grab-attachments.1?id=af1d20f51e193fb033eca290b548e1bceac54ace>`_, and `hugdaylist <https://git.launchpad.net/ubuntu-dev-tools/tree/doc/hugdaylist.1?id=af1d20f51e193fb033eca290b548e1bceac54ace>`_ scripts. They're all sharing the `ubuntutools/lp/libsupport.py <https://git.launchpad.net/ubuntu-dev-tools/tree/ubuntutools/lp/libsupport.py?id=0c211c1bc74bd1dfaba4a1a94bf5117b5f50fbb5>`_ library, which might be a good place to start.
   * - `ubuntu-qa-tools <https://launchpad.net/ubuntu-qa-tools>`_
     - A collection of tools used by the Ubuntu QA Team (like ubuntu-dev-tools, but for QA).
     - See the `ml-fixes-report.py <https://git.launchpad.net/ubuntu-qa-tools/tree/bugs-mailinglist/ml-fixes-report?id=c87e8dbc3d41d473f88a427c8577ed1337f3b7ac>`_, `ml-team-fixes-report.py <https://git.launchpad.net/ubuntu-qa-tools/tree/bugs-mailinglist/ml-team-fixes-report?id=c87e8dbc3d41d473f88a427c8577ed1337f3b7ac>`_, `b-tool <https://git.launchpad.net/ubuntu-qa-tools/tree/mutt-scripts/b-tool>`_, `package-bugs-gravity.py <https://git.launchpad.net/ubuntu-qa-tools/tree/bug-report-framework/package-bugs-gravity.py>`_, `team-reported-bug-tasks.py <https://git.launchpad.net/ubuntu-qa-tools/tree/bug-report-framework/team-reported-bug-tasks.py?id=dae76011154e314d580524a05f7c93a5af974d49>`_, and `team-assigned-bug-tasks.py <https://git.launchpad.net/ubuntu-qa-tools/tree/bug-report-framework/team-assigned-bug-tasks.py?id=0442ea1433da36344f87e194934a8b74dd2521da>`_ scripts.
   * - `ubuntu-archive-tools <https://code.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/>`_
     - A couple of small tools used by the Ubuntu archive administration team. Likely to grow as the Soyuz API gets richer.
     - Thanks to Colin Watson for pointing this one out.
   * - `loco-directory <https://launchpad.net/loco-team-portal>`_
     - LoCo Team organisation site
     - 
   * - `MeMaker <http://launchpad.net/memaker>`_
     - Uses python-launchpadlib to update users mugshot on Launchpad.net.
     - 
   * - `OpenHatch <http://openhatch.org/>`_
     - A website for talking about your Free Software contributions and finding new ways to contribute
     - We use launchpadlib to convert email addresses into lp.net usernames, and we pull information about your project experiences from your lp.net user page.
   * - `Laika <https://launchpad.net/laika>`_
     - "a guide dog for launchpad" -- prints a summary of the bugs you touched this week
     -
