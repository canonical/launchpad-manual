.. _building-live-filesystems:

Building live filesystems in Launchpad
======================================

Launchpad supports building :ref:`live filesystems <live-file-systems>` using 
the ``livecd-rootfs`` package in Ubuntu. 

LiveFS and LiveFSBuild
----------------------

Launchpad has the LiveFS and LiveFSBuild objects to facilitate building of live
filesystems. These are visible on the "devel" version of the webservice as 
`livefs <https://launchpad.net/+apidoc/devel.html#livefs>`_ and 
`livefs_build <https://launchpad.net/+apidoc/devel.html#livefs_build>`_ 
respectively. 

LiveFS objects specify the general metadata for an image type (for instance, 
there is a LiveFS for Kubuntu in Ubuntu Utopic, and a LiveFS for Ubuntu Touch 
in Ubuntu trusty); they are created by the (hidden) ``Person:+new-livefs`` 
page, or by the `livefses.new <https://launchpad.net/+apidoc/devel.html#livefses-new>`_ 
webservice method. 

LiveFSBuild objects identify a single build of a LiveFS, which must nominate an
archive, DistroArchSeries, and pocket, and may also add additional items of 
metadata which take effect for just that build; they are created by the ``livefs.requestBuild`` 
webservice method.

The archive attached to a LiveFSBuild is a source archive, not a target archive. 
That is, it specifies the archive that packages in the live filesystem image 
should come from. In the common case, this is just the Ubuntu primary archive, 
but it may also be a PPA, in which case both the primary archive and that PPA 
(and any archive dependencies it lists) will be used as a source of packages. 
Since this is a source archive, there is no requirement for the user requesting 
the build to have upload access to the archive. (At present, ``launchpad-buildd`` 
and ``livecd-rootfs`` are not quite smart enough to work out all the details of 
this just from the archive parameter to ``livefs.requestBuild``, and typically 
need help in the form of an ``extra_ppas`` entry in the metadata_overrides 
dictionary. `ubuntu-cdimage <https://code.launchpad.net/+branch/ubuntu-cdimage>`_ 
knows how to deal with this.)

Live filesystems security
-------------------------

There are some security issues surrounding live filesystem builds. Firstly, 
they are a very easy way to consume lots of time on the Launchpad build farm, 
so only members of the `launchpad-livefs-builders <https://launchpad.net/~launchpad-livefs-builders>`_ 
team can create new LiveFS or LiveFSBuild objects. 

Secondly, building a live filesystem involves executing code from packages in 
the source archive. Therefore, in order to build live filesystems on 
devirtualized builders (which, occasionally, support architectures not 
supported by virtualized builders, but have no effective sandboxing, so may 
only be used by trusted people), both the LiveFS parameters and the source 
archive must be devirtualized.

Devirtualized builders are builders that are not reset between builds. They use
physical hardware, typically because virtualization of an architecture isn't 
available yet or performant enough.