.. _how-to-import-project-translation-templates:

Import your project's translation templates
===========================================

.. include:: /includes/important_not_revised_help.rst

Before anyone can help translate your project, you need to tell
Launchpad which English strings appear in your software's interface.

You do this by importing one or more GNU gettext ``.pot`` template files.
If you're unfamiliar with ``.pot`` files or GNU gettext in general, `see
the gettext
manual <http://www.gnu.org/software/gettext/manual/gettext.html>`__.

You can importing translation templates by `Manually uploading .pot files <#manual-translation-template-imports>`_ 
using the web interface.

Name template
-------------

Since a template file does not carry any metadata, all information about
it must be derived from its path.

Launchpad needs this metadata to either create a new template entry in
Launchpad Translations or to match the file to an existing entry. The
metadata consists of the translation domain and the template name. The
latter is derived from the former which in turn is extracted from the
path.

These are the ways to specifiy the translation domain, the first match
will be used:

1. In the file name itself: ``domain.pot`` or ``po/domain.pot``, etc.
2. If the file name is generic (one of messages.pot, template.pot or
   untitled.pot), in the containing directory: ``domain/messages.pot``
   or ``po/domain/messages.pot``
3. Or in the module directory: ``domain/po/messages.pot`` (only ``po`` is
   recognized as an intermediate directory in the path).

Upload translation template imports
-----------------------------------

You can also upload your template -- or an archive containing several template 
files -- through Launchpad's web interface.

Visit your project's translations overview page and click the link for
the ``trunk`` series.

Ensure a successful import
--------------------------

Whenever someone imports a file for your project's translations,
Launchpad will hold it in a queue. If it's an update to existing file,
Launchpad will review and automatically approve it.

If the file is new, you -- as the project's translations maintainer --
will need to review it manually.

You can help ensure your files are imported by checking that:

-  there isn't already a translation effort in Launchpad for that
   project
-  you have permission from the upstream project, if that's not you
-  In the tarball, give each template its own directory so the system can see 
   what directories you want them in.

There are also some common problems that can cause a template file
import to fail:

-  Make sure each of the message IDs -- i.e. the English strings -- is
   unique.
-  Use real English strings -- for example ``Save the file`` --
   rather than identifiers, such as ``save_msg_z339``.

Launchpad will email you to let you know if your import is a success or
a failure.

Manual review
~~~~~~~~~~~~~

The first time you import a template, or a translation whose language or
template are not clear, you'll need to review it manually. To do this,
you need to be the maintainer or owner of the project and to follow the
"Import queue" link on your project's translations overview page.

When you're reviewing your project's translations import queue, you're
looking for a number of potential problems:

-  an update to an existing template that's been renamed and so shows up
   as a new template: delete the misnamed template and re-upload with
   the correct name
-  a template with anything other than English strings: delete and
   upload a template with English strings
-  a template or translations file that you never want to have in your
   project, even if the same person uploads it again: select ``Blocked``.
   Launchpad will remember that you don't want it imported.

If a troublesome file is imported, you'll have to re-try with a clean
version of the file.

After that first import, Launchpad will automatically approve subsequent
imports of that file.
