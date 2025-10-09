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
   * - `Launchpadlib "contrib" scripts <http://bazaar.launchpad.net/~lazr-developers/launchpadlib/trunk/files/head%3A/contrib>`_
     - Various scripts shipped with Launchpadlib, meant both as examples and as real-world tools.
     - In particular, see `lp-bug-ifier.py <http://bazaar.launchpad.net/~lazr-developers/launchpadlib/trunk/annotate/head%3A/contrib/lp-bug-ifier.py>`_ (expands raw bug numbers to show the bug summaries as fetched from Launchpad), `close_bugs_from_commits.py <http://bazaar.launchpad.net/~lazr-developers/launchpadlib/trunk/annotate/head%3A/contrib/close_bugs_from_commits.py>`_ (the name is self-explanatory), and the `lpscripts.py <http://bazaar.launchpad.net/~lazr-developers/launchpadlib/trunk/annotate/head%3A/contrib/close_bugs_from_commits.py>`_ convenience library they both use.
   * - `bughugger <https://launchpad.net/bughugger>`_
     - Py Gtk Client for Ubuntu bugs in Launchpad. Currently supports listing bugs by team, user, and package. Supports plugins for changing bugs.
     - Still in development, join ~bughuggers
   * - `bzr-eclipse <http://blog.launchpad.net/api/launchpad-plugin-for-eclipse-using-the-launchpad-api>`_
     - A Bazaar plugin for Eclipse, that talks to the Launchpad/Bazaar integration using launchpadlib.
     - The developer says: "The API is straightforward to learn, also if you can use launchpadlib it's far easier, just start the python interactive interpreter, import launchpadlib and start prototyping your app :)"
   * - `Tarmac <http://launchpad.net/tarmac>`_
     - "The Launchpad Landing Strip": an automatic branch lander for the Bazaar branches hosted on Launchpad. Tarmac uses the Launchpad API to manage a development focus branch's proposed merges. It will automatically merge approved branch merge proposals and push them back up to Launchpad.
     - 
   * - `apport <http://launchpad.net/apport>`_
     - A crash detection system that automatically generates reports with debugging information from crashed programs and provides UI frontends for handling these reports.
     - See the script `apport-collect <http://bazaar.launchpad.net/%7Eubuntu-core-dev/apport/ubuntu/annotate/head%3A/debian/local/apport-collect>`_, which adds apport data to existing bug reports.
   * - `ubuntu-dev-tools <http://wiki.ubuntu.com/UbuntuDevTools>`_
     - A collection of useful tools that Ubuntu developers use to make their packaging work a lot easier (bug filing, packaging preparation, package analysis, etc).
     - See the `manage-credentials <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/manage-credentials>`_, `requestsync <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/requestsync>`_, `massfile <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/massfile>`_, `lp-set-dup <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/lp-set-dup>`_, `grab-attachments <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/grab-attachments>`_, and `hugdaylist <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/hugdaylist>`_ scripts. They're all sharing the `ubuntutools/lp/libsupport.py <http://bazaar.launchpad.net/%7Eubuntu-dev/ubuntu-dev-tools/trunk/annotate/head%3A/ubuntutools/lp/libsupport.py>`_ library, which might be a good place to start.
   * - `ubuntu-qa-tools <https://launchpad.net/ubuntu-qa-tools>`_
     - A collection of tools used by the Ubuntu QA Team (like ubuntu-dev-tools, but for QA).
     - See the `ml-fixes-report.py <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/bugs-mailinglist/ml-fixes-report.py>`_, `ml-team-fixes-report.py <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/bugs-mailinglist/ml-team-fixes-report.py>`_, `b-tool <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/mutt-scripts/b-tool>`_, `package-bugs-gravity.py <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/bug-report-framework/package-bugs-gravity.py>`_, `team-reported-bug-tasks.py <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/bug-report-framework/team-reported-bug-tasks.py>`_, and `team-assigned-bug-tasks.py <http://bazaar.launchpad.net/%7Eubuntu-bugcontrol/ubuntu-qa-tools/master/files/head%3A/bug-report-framework/team-assigned-bug-tasks.py>`_ scripts.
   * - `ubuntu-archive-tools <http://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/files>`_
     - A couple of small tools used by the Ubuntu archive administration team. Likely to grow as the Soyuz API gets richer.
     - Thanks to Colin Watson for pointing this one out.
   * - `loco-directory <http://bazaar.launchpad.net/~loco-directory-dev/loco-directory/trunk/files>`_
     - LoCo Team organisation site
     - See, e.g., `/loco_directory/includes/launchpad.py <http://bazaar.launchpad.net/~loco-directory-dev/loco-directory/trunk/annotate/head%3A/loco_directory/includes/launchpad.py>`_ or `/loco_directory/teams/management/commands/lpupdate.py <http://bazaar.launchpad.net/~loco-directory-dev/loco-directory/trunk/annotate/head%3A>`_
   * - `MeMaker <http://launchpad.net/memaker>`_
     - Uses python-launchpadlib to update users mugshot on Launchpad.net.
     - 
   * - `OpenHatch <http://openhatch.org/>`_
     - A website for talking about your Free Software contributions and finding new ways to contribute
     - We use launchpadlib to convert email addresses into lp.net usernames, and we pull information about your project experiences from your lp.net user page.
   * - `Laika <https://launchpad.net/laika>`_
     - "a guide dog for launchpad" -- prints a summary of the bugs you touched this week
     -
