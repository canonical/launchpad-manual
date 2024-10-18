Building and publishing Launchpad Development LXD Images
========================================================

A rebuild of images are are required if we introduce new external dependencies in `lp:lp-source-deps`. Also, its recommended to rebuild the image atleast once every month so that the launchpad clone in the image is relatively updated. Currently, we only build Launchpad LXD Dev Images for Focal (amd64). As there are no community LXD servers
or Launchpad team's self hosted servers to publish the LXD images. We are currently using Google Drive to 
build and publish images. 

Launchpad uses `LXD Image Builder <https://github.com/canonical/lxd-imagebuilder>`_ to build LXD images. The image file can be found at the `lpdev-image.yaml <https://git.launchpad.net/launchpad/tree/lpdev-image.yaml>`_ in
the Launchpad repository. 

Build Process
-------------

Make sure you have ``LXD Image Builder`` installed. Follow the installation process 
`here <https://canonical-lxd-imagebuilder.readthedocs-hosted.com/en/latest/howto/install/#installing-from-package>`_. 

.. code-block:: bash

    make build-lxd-image

Publishing Steps
----------------

Above command will output a ``tar.xz`` file that should be replaced with the existing image file on `Google Drive <https://drive.google.com/file/d/1jn_w2Uu_sVVMP9UVY-ut4aN1LDPSeIJh/view?usp=drive_link>`_. 

Notes
-----

The current LXD image only runs the basic web application. Future plan is to have `Codehosting <https://dev.launchpad.net/Code/HowToUseCodehostingLocally>`_ 
and `Soyuz <https://dev.launchpad.net/Soyuz/HowToUseSoyuzLocally>`_ as a part of this image. 
