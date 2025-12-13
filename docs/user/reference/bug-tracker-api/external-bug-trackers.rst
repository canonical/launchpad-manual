.. _interoperability-with-external-bug-trackers:

Interoperability with external bug trackers
===========================================

.. include:: /includes/important_not_revised_help.rst


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
     - Savane
     - `GitHub <https://github.com/>`_
     - `GitLab <https://gitlab.com/>`_
     -
   * - Plugin for two-way comms
     - :ref:`Yes <use-the-bugzilla-plugin>`
     - :ref:`Yes <use-the-trac-plugin>`
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
     - :ref:`BugZilla plugin <use-the-bugzilla-plugin>`
     - WN
     - Yes
     - :ref:`Trac plugin <use-the-trac-plugin>`
     - WS
     -
     -
     -
     -
     -
     -
   * - Comment pushing
     - :ref:`BugZilla plugin <use-the-bugzilla-plugin>`
     - WN
     - NI
     - :ref:`Trac plugin <use-the-trac-plugin>`
     - WS
     -
     -
     -
     -
     -
     -
   * - Bug importing
     - NI :ref:`BugZilla plugin <use-the-bugzilla-plugin>`
     - WN
     - Yes
     - NI :ref:`Trac plugin <use-the-trac-plugin>`
     - WS
     -
     -
     -
     -
     -
     -
   * - Bug forwarding
     - NI :ref:`BugZilla plugin <use-the-bugzilla-plugin>`
     - WN
     - NI
     - NI :ref:`Trac plugin <use-the-trac-plugin>`
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
