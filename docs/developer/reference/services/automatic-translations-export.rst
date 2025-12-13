
Automatic translations tarball exports
======================================

This page documents the schedule of automatic translations tarball exports from
Launchpad to be used as a source to
`langpack-o-matic <https://launchpad.net/langpack-o-matic>`__ to create the
Ubuntu language packs.

Status
------

For the live status on the language pack builds, have a look
at macquarie.canonical.com/~langpack/crontab (XXX URL needs to be updated).

Current export schedule
-----------------------

Note: these are the *starting* days of the exports. The cron jobs to
start generating the language-pack tarballs start on these days. Then
langpack-o-matic picks them up the next day.

-  Export starts: **10:30 UTC**
-  Build starts: **10:30 UTC** next day

+-----------+-------------------+----------------------+--------------------+
| Weekday   | Launchpad Exports | Language Pack Builds | Notes              |
+===========+===================+======================+====================+
| Monday    | Jammy             |                      |                    |
+-----------+-------------------+----------------------+--------------------+
| Tuesday   | Focal             | Jammy (archive)      |                    |
+-----------+-------------------+----------------------+--------------------+
| Wednesday |                   | Focal (PPA)          |                    |
+-----------+-------------------+----------------------+--------------------+
| Thursday  | Bionic            |                      | Ubuntu Release day |
+-----------+-------------------+----------------------+--------------------+
| Friday    | Resolute          | Bionic (PPA)         |                    |
+-----------+-------------------+----------------------+--------------------+
| Saturday  | Noble             | Resolute             |                    |
+-----------+-------------------+----------------------+--------------------+
| Sunday    |                   | Noble (PPA)          |                    |
+-----------+-------------------+----------------------+--------------------+


Notes
-----

-  Launchpad crontabs are managed by the
   `launchpad-scripts <https://charmhub.io/launchpad-scripts>`_ charm.
-  The old timing (was 22:00 UTC) used to be chosen so we hit the times
   when we usually expect the lowest load. Most of the translation work
   happens in Europe, South America and Asia, and 22:00 UTC should mean
   less load on LP due to translation activity. With DB slaves, though,
   this is probably not something we should worry about.
-  The new timing (10:30 UTC) was chosen to be after the new
   fastnodowntime window at 10:00 - 10:05 UTC during which the database
   will shortly be unavailable. This would break the export run and has
   to be avoided (`bug
   849829 <https://bugs.launchpad.net/launchpad/+bug/849829>`__).
-  Currently full language exports take much longer than expected,
   approaching 24h (`bug
   684664 <https://bugs.launchpad.net/launchpad/+bug/684664>`__)
