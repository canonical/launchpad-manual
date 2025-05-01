
Interoperability with external bug trackers
===========================================

You can link bug reports in Launchpad to reports in tracked elsewhere.

This table shows you what level of interoperability Launchpad has with which external tracker.

.. list-table:: 
   :header-rows: 1

   * - Function
     - `Bugzilla <http://www.bugzilla.org/>`_
     - `Roundup <http://roundup.sourceforge.net/>`_
     - `Debbugs <http://www.debian.org/Bugs/>`_
     - `Trac <http://trac.edgewall.org/>`_
     - `Mantis <http://www.mantisbt.org/>`_
     - `SourceForge <http://sourceforge.net/>`_
     - `Request Tracker <http://bestpractical.com/rt>`_
     - `GForge <http://gforge.org/>`_
     - Savane
     - `GitHub <https://github.com/>`_
     - `GitLab <https://gitlab.com/>`_
   * - Plugin for two-way comms
     - `Yes <https://help.launchpad.net/Bugs/BugzillaPlugin>`_
     - `Yes <https://help.launchpad.net/Bugs/TracPlugin>`_
     -
     -
     -
     -
     -
     -
     -
     -
     -
   * - Add bug watch
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
   * - Status syncing
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     - Yes
     -  
     - Yes
     - Yes
   * - Comment importing
     - `Plugin <https://help.launchpad.net/Bugs/BugzillaPlugin>`_
     - WN
     - Yes
     - `Plugin <https://help.launchpad.net/Bugs/TracPlugin>`_
     - WS
     -
     -
     -
     -
     -
     -
   * - Comment pushing
     - `Plugin <https://help.launchpad.net/Bugs/BugzillaPlugin>`_
     - WN
     - NI
     - `Plugin <https://help.launchpad.net/Bugs/TracPlugin>`_
     - WS
     -
     -
     -
     -
     -
     -
   * - Bug importing
     - NI `plugin <https://help.launchpad.net/Bugs/BugzillaPlugin>`_
     - WN
     - Yes
     - NI `plugin <https://help.launchpad.net/Bugs/TracPlugin>`_
     - WS
     -
     -
     -
     -
     -
     -
   * - Bug forwarding
     - NI `plugin <https://help.launchpad.net/Bugs/BugzillaPlugin>`_
     - WN
     - NI
     - NI `plugin <https://help.launchpad.net/Bugs/TracPlugin>`_
     - WS
     -
     -
     -
     -
     -
     -


Key
---

* Yes \= We have this today  
* ND \= Needs discussion  
* WN \= Upstream work needed  
* WS \= Upstream work scoped  
* UD \= Under Development  
* NI \= Possible already upstream but needs Launchpad implementation  
* Plugin \= Available through a Launchpad-provided plugin for the upstream tracker
