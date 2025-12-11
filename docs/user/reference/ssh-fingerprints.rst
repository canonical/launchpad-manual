.. _ssh-fingerprints:

SSH fingerprints
================

.. include:: /includes/important_not_revised_help.rst

This page lists the SSH fingerprints of Launchpad's various SSH
endpoints. It is a stopgap measure until we have signed DNS records.


.. list-table::
   :header-rows: 1

   * - Host
     - Key type
     - Fingerprints
   * - git.launchpad.net
     - RSA
     - `MD5:df:b0:16:7e:55:54:96:58:79:85:ba:e2:c3:72:d9:09`
   * - 
     - 
     - `SHA256:UNOzlP66WpDuEo34Wgs8mewypV0UzqHLsIFoqwe8dYo`
   * - upload.ubuntu.com
     - RSA
     - `MD5:79:57:63:97:d3:d3:be:b6:6d:da:81:d0:73:29:80:48`
   * - 
     - 
     - `SHA256:FN8sNU/MMmyvw/xtY5sAzkLGmkVQt2QpGZcwsHoBzjc`
   * - ppa.launchpad.net
     - RSA
     - `MD5:6b:03:de:98:33:25:23:18:a6:46:b3:47:22:cd:54:f2`
   * - 
     - 
     - `SHA256:MGq+4hxD7RduVTcfwlwwboZnsgJC6SL/NltM8ye+gNg`


We also provide some staging endpoints over SSH. If you are using these, be aware that they may go down without notice and that they offer no guarantees of data persistence (that is, anything you upload there may be deleted without notice at any time).

.. list-table::
   :header-rows: 1

   * - Host
     - Key type
     - Fingerprints
   * - git.qastaging.paddev.net
     - RSA
     - `MD5:1a:29:54:09:ee:6a:67:69:8a:77:31:21:37:a3:9d:c1`
   * - 
     - 
     - `SHA256:Jv7EmXKEEizRZ5t62cmyY4Fd7nuVChl+3wWmLG+qv0k`
