Known source build limitations
==============================

Here are the significant limitations that we anticipate affect a large
number of users:

-  Code Imports does not support submodules, because Bazaar does not yet
   support them (Bug
   `#402814 <https://bugs.launchpad.net/bzr/+bug/402814>`__).
-  If bzr cannot merge the packaging branch into the base branch (e.g.
   due to parallel imports), the "nest" command must be used. If the
   "nest" command is used, the packaging branch must be the contents of
   the debian directory (rather than **containing** a debian directory).
   (Bug
   `#627119 <https://bugs.launchpad.net/launchpad-code/+bug/627119>`__)
-  Builds of private branches are not currently supported. (Bug
   `#607895 <https://bugs.launchpad.net/launchpad-code/+bug/607895>`__)
-  Import fails with infinite recursion through
   \_reconstruct_manifest_and_flags_by_revid (Bug
   `#519709 <https://bugs.launchpad.net/launchpad-code/+bug/519709>`__)
-  Launchpad disallows valid CVS module of '.' from being imported (Bug
   `#594294 <https://bugs.launchpad.net/launchpad-code/+bug/594294>`__)

`Other bugs for recipe
builds <https://bugs.launchpad.net/launchpad-code/+bugs?field.tag=recipe>`__