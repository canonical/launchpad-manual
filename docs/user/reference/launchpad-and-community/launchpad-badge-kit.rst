.. meta::
   :description: Launchpad badge kit reference for adding and displaying badges.

.. _launchpad-badge-kit:

Launchpad badges
================

.. include:: /includes/important_not_revised_help.rst

If you or your project uses `Launchpad <https://launchpad.net>`__,
display one of these badges to let people know!

Trademark and usage policy
--------------------------

Launchpad ™ is a trademark of Canonical Ltd. You are encouraged to use these images to refer to your
use of the Launchpad.net services. Canonical may revoke your permission
to use these images if you make modifications to the images or use them
incorrectly (e.g., on a project that does not use Launchpad.net).

.. image:: ../../../user/images/badges/Launchpad_120px_badge.png
      :alt: Launchpad Badge 1
      :width: 120px

.. image:: ../../../user/images/badges/Launchpad_160px_badge.png
   :alt: Launchpad Badge 2
   :width: 160px

.. image:: ../../../user/images/badges/Launchpad_200px_badge.png
   :alt: Launchpad Badge 3
   :width: 200px

.. image:: ../../../user/images/badges/Launchpad_250px_badge.png
   :alt: Launchpad Badge 4
   :width: 250px



How to display a badge
----------------------

Insert HTML like the following into the page where you want to display
the badge, replacing ``FILL_ME_IN`` with either a project name or a
Launchpad username (if a username, remember to include the ``~``. The default width of
160px is good for most contexts, but you can choose another pixel width
from the list above or make a custom image from the `scalable SVG
file <http://media.launchpad.net/lp-badge-kit/launchpad-badge.svg>`__ if
necessary.

::

      <a href="https://launchpad.net/FILL_ME_IN" style="border: none;" 
      ><img src="http://media.launchpad.net/lp-badge-kit/launchpad-badge-w160px.png"
            alt="Launchpad logo" style="border: none;"/></a>