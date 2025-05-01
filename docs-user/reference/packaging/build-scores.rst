Prioritising builds
===================

When you upload a source package to Launchpad, it assigns the package a
priority -- a "score" -- and then uses that score to decide when the
package should be sent to Launchpad's
`build-farm <https://launchpad.net/builders>`__.

Launchpad calculates the score based on various attributes (described
below). The higher the score, the sooner the build is dispatched to one
of the available build machines.

There are separate build queues for
`distributions <https://launchpad.net/ubuntu/+builds>`__ and PPAs (PPA →
View package details → View all builds).

How Launchpad calculates the score
----------------------------------

Launchpad uses the following attributes of a package to calculate its
priority:

-  target `pocket <Glossary#pocket>`__ -- e.g. security
-  target `component <Glossary#component>`__ -- e.g. universe
-  source urgency -- defined by the packager
-  package sets containing the package
-  archive containing the package

Launchpad adds up the scores from each category to decide the build's
priority.


Target pocket
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Pocket
     - Score
   * - -backports
     - 0
   * - \<release&gt;
     - 1500
   * - -proposed
     - 3000
   * - -updates
     - 3000
   * - -security
     - 4500


Target component
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Component
     - Score
   * - multiverse
     - 0
   * - universe
     - 250
   * - restricted
     - 750
   * - main
     - 1000
   * - partner
     - 1250


Source urgency
^^^^^^^^^^^^^^

A packager can specify the urgency of their source package. Launchpad takes this into account.

.. list-table::
   :header-rows: 1

   * - Urgency
     - Score
   * - low
     - 5
   * - medium
     - 10
   * - high
     - 15
   * - emergency
     - 20


Package sets
^^^^^^^^^^^^

Package sets are used in distributions to apply properties such as upload permissions to groups of packages. A package set may have a "relative build score" bonus assigned to it in the Launchpad database, and a package receives the maximum of the bonuses for any of the package sets that contain it. These bonuses don't apply to PPA builds. Currently, package sets in the Ubuntu distribution that are used to build images receive bonuses as follows:

.. list-table::
   :header-rows: 1

   * - Package set
     - Score
   * - core
     - 50
   * - desktop-core
     - 50
   * - edubuntu
     - 50
   * - kubuntu
     - 50
   * - lubuntu
     - 50
   * - mythbuntu
     - 50
   * - ubuntu-desktop
     - 50
   * - ubuntu-server
     - 50
   * - ubuntustudio
     - 50
   * - xubuntu
     - 50


Archives
^^^^^^^^

Builds destined for private PPAs are given a higher priority.

.. list-table::
   :header-rows: 1

   * - Privacy status
     - Score
   * - public
     - 0
   * - private
     - 10000


Builds destined for copy archives (used for test rebuilds of the Ubuntu primary archive) are given a lower priority.

.. list-table::
   :header-rows: 1

   * - Copy archive?
     - Score
   * - yes
     - -2600
   * - no
     - 0

Archives may also have a "relative build score" bonus assigned to them
in the Launchpad database.

Other
~~~~~

Builds for sources targeted to the *translations* section don't get any
package bonuses, meaning they will be scored at the base score for the
archive and processed after all other builds for that archive.

Translation template builds get a score of 2515.

Source package recipe builds get a score of 2510 plus any relative build
score for their target archive.

`Live filesystem <LiveFilesystem>`__ builds get a score of 2510, plus
any relative build score for their source archive, plus any relative
build score for their live filesystem.

Snap builds get a score of 2510 plus any relative build score for their
source archive.

OCI recipe builds get a score of 2510.