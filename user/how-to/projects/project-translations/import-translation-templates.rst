Import your project's translation templates
===========================================

Before anyone can help translate your project, you need to tell
Launchpad which English strings appear in your software's interface.

You do this by importing one or more GNU gettext ``.pot`` template files.
If you're unfamiliar with ``.pot`` files or GNU gettext in general, `see
the gettext
manual <http://www.gnu.org/software/gettext/manual/gettext.html>`__.

You can choose from two methods of importing translation templates:

.. tip::
    Automatic and ongoing imports of your templates, and
    optionally also `translation
    files <Translations/YourProject/ImportingTranslations>`__, from a
    Bazaar branch you specify - or `manually upload .pot files <#manual>`__
    using the web interface.

Push the branch to Launchpad
----------------------------

You can run concurrent separate translation efforts for each
`series <Projects/SeriesMilestonesRelease>`__ of your project. For now,
let's work with the ``trunk`` series that Launchpad created by default
when you registered your project.

If you've already set a default branch for your trunk series, you can
skip straight to ``Enabling automatic template imports``.

**Step 1:** Open a terminal and change directory to your Bazaar branch.

.. note::
    Don't worry if your Bazaar branch is empty. If you're new to
    Bazaar and Launchpad Code Hosting, `see our quick-start <Code/QuickStart>`__.

**Step 2:** Push your Bazaar branch to Launchpad:

::

   bzr push lp:~your-id/your-project/trunk

Of course, you need to replace the relevant parts of that line with your
own Launchpad user id, the project name and, if it isn't ``trunk``, the
series name.

Once Bazaar has pushed the branch to Launchpad, Launchpad will
automatically associate it with the ``trunk`` series.

Enable automatic template imports
---------------------------------

Now you need to tell Launchpad to automatically import any translation
templates, and subsequent changes to those templates, that it finds in
the series' default branch.

**Step 1:** Visit the translations overview page for the series and
click ``Settings``.

**Step 2:** Next, select ``Import template files``, then click ``Save
settings``.

We can ignore the other option for now, as that's explained in our
`Importing
translations <Translations/YourProject/ImportingTranslations>`__
article.

Once you've completed both stages, Launchpad will schedule its first
import to take place within the next 15 minutes.

Add and update templates
------------------------

To update or add a template all you need to do is commit the template
file to the branch.

Launchpad's branch scanner will find the templates and then add them to
the import queue. Once approved, the template will appear in the
translation tab for the product series.

.. important:
You should follow our `translations import policy <Translations/ImportPolicy>`__
when creating and adding your templates.

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
-  for uploads through the web interface, you upload templates in a
   tarball, so the system can see what directories you want them in;
   give each template its own directory.

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

Automatic approval
~~~~~~~~~~~~~~~~~~

One of the big advantages of importing templates directly from your
series default Bazaar branch is that your templates stand a better
chance of automatic approval.

To assure automatic approval, these conditions must be met:

-  The translation domain must be specified in the path (as described
   above).
-  The resulting template name must either match the name of a template
   in Launchpad Translations, or,
-  If the template is to be added, no template entry must exist in
   Launchpad Translations that does not have a matching template file in
   the branch.

The latter condition is there to avoid creating new template entries
when in reality the existing template entry was to be renamed. This and
any other case will not be approved automatically and must be reviewed
by one of the Launchpad team.

**Exception:** In the simple case of having only one template file in
the branch and one entry in Launchpad Translations, these two are always
matched and the translation domain attribute of the Launchpad
Translations entry is updated with whatever the file name provides. The
template name is never updated as it identifies the template in the UI
and is also used in URLs.

Manual translation template imports
-----------------------------------

If you prefer, you can also upload your template -- or an archive
containing several template files -- through Launchpad's web interface.

Visit your project's translations overview page and click the link for
the ``trunk`` series.

Next steps
----------

If you're likely to make translations elsewhere, you can have Launchpad
`automatically
import <Translations/YourProject/ImportingTranslations>`__ them from the
same Bazaar branch.