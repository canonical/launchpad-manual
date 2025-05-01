Import your project's translations
==================================

.. toctree::
    :hidden:
    :maxdepth: 2

    Import your project's translation templates <import-translation-templates>
    Exporting translations <exporting-translations>
    
Just as with translation templates, you can import translation files
(``.po``) in two ways:

-  from your series' default Bazaar branch
-  or by uploading a tarball of templates and translation files through
   the web interface.

If you already have your translation files in a Bazaar branch (or `git
branch, or CVS or Subversion
repository <https://help.launchpad.net/Code/Imports>`__), you may find
that to be the easiest source for importing your translation files.

Imports from a Bazaar branch
----------------------------

You can ask Launchpad to automatically import your translation templates
from your project's official Bazaar branches hosted in Launchpad.

You can make either one-off or continuous imports of translation files
in a Bazaar branch. Which you choose will most likely depend on whether
you expect to make frequent translations outside of Launchpad.

-  **Continuous**: on your project's translations settings page choose
   ``mport template and translation files`` to automatically import any
   ``.po`` that are in the branch, whenever Launchpad imports ``.pot`` files
   from the branch.
-  **One off:** go to the ``Request Bazaar Import`` page to request a
   one-time import of all ``.pot`` and ``.po`` files in the branch.

Activating automatic translation imports for Bazaar branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First off, you -- the project owner -- need to link each project series,
for which you want to automatically import translation templates, to its
Bazaar branch. When a project is registered in Launchpad, its ``trunk``
series is created by default.

1. Visit the project series overview page and click ``Link to branch``.
2. Next, select the branch and click ``Update``.

If you've previously linked the series to a branch, you can skip
straight to enabling automatic template imports.

1. Visit the translations overview page for the series and click
   ``Settings``.
2. Next, select ``Import template files``, then click ``Save settings``.

The other available setting is explained further below under
:literal:`Importing translations`.

The order in which you complete the two stages does matter to an extent:
the ``Translations Settings`` form shows you the branch associated with
the series, making it easier to confirm that you've selected the branch.

Once you've completed both stages, Launchpad will schedule its first
import to take place within the next 15 minutes.

Adding and updating templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update or add a template all you need to do is commit the template
file to the branch.

Launchpad's branch scanner will find the templates and then add them to
the import queue. Once approved, the template will appear in the
translation tab for the product series.

Naming templates
^^^^^^^^^^^^^^^^

Since a template file does not carry any metadata, all information about
it must be derived from its path. The metadata is needed to either
create a new template entry in Launchpad Translations or to match the
file to an existing entry. The metadata consists of the translation
domain and the template name. The latter is derived from the former
which in turn is extracted from the path.

These are the ways to specifiy the translation domain, the first match
will be used:

1. In the file name itself: ``domain.pot`` or ``po/domain.pot``, etc.
2. If the file name is generic (one of messages.pot, template.pot or
   untitled.pot), in the containing directory: ``domain/messages.pot``
   or ``po/domain/messages.pot``
3. Or in the module directory: ``domain/po/messages.pot`` (only ``po`` is
   recognized as an intermediate directory in the path).

The template name is derived from the domain by replacing underscores
(_) with dashes (-).

Automatic approval
^^^^^^^^^^^^^^^^^^

One of the big advantages of importing templates directly from your
series Bazaar branch is that your templates may be automatically
approved.

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
by a queue admin.

**Exception:** In the simple case of having only one template file in
the branch and one entry in Launchpad Translations, these two are always
matched and the translation domain attribute of the Launchpad
Translations entry is updated with whatever the file name provides. The
template name is never updated as it identifies the template in the UI
and is also used in URLs.

Importing translations
~~~~~~~~~~~~~~~~~~~~~~

There are two ways to get translation files (``.po``) imported into
Launchpad from your branch.

1. On the ``Settings`` page choose ``Import template and translation files``
   to import ``.po`` files in addition to ``.pot`` files whenever they are
   updated in the branch.
2. Or go to the ``Request Bazaar Import`` page to request a one-time
   import of all ``.pot`` and ``.po`` files in the tree.

One time upload of a tarball
----------------------------

Visit your project's translations overview page and click the link for
the ``trunk`` series. Upload a tarball containing your translation files
``preserving directory structure``.

Naming translation files
------------------------

In order to ensure automatic approval and subsequent import of the
translation files, two rules need to be followed, just like when
uploadding tarballs (See a sample directory layout
`here <Translations/ImportPolicy>`__).

1. Place the files in the same directory as the template for which they
   are meant. Each template and its translation files must have its own
   directory. This rules out the first naming option for templates that
   was mentioned above.
2. Name the files according to the language code of the language they
   contain. So for Spanish translations use ``es.po``.

In addition to that the normal `instructions for uploading translation
files <Translations/YourProject>`__ apply.

Avoiding common problems
------------------------

Your translations stand a better chance of an automatic, and therefore
near instant, import if you follow these guidelines:

-  Ensure consistent formatting: for example, if ``%d`` appears in an
   original English string, make sure it's also in each language's
   equivalent.
-  Use consistent paths within your tarball: locate all your .po
   translation files under the same directory structure.
-  Name individual language .po files using the ISO language code, such
   ``fr.po`` for French. Only append the country code in the following
   circumstances:

   -  variants of international English: for example, ``en_GB.po``
   -  Brazillian Portuguese: ``pt_BR.po`` (Brazillian Portuguese),
      as opposed to ``pt.po`` for European Portuguese
   -  Chinese: traditional ``zh_TW.po`` and simplified
      ``zh_CN.po``

How Launchpad prioritises imported translation strings
------------------------------------------------------

To help ensure the best quality translations end-up in Ubuntu, Launchpad
prioritises translation strings differently depending on where they were
made.

In general, a translation made in Launchpad will take precedence over a
translation imported from upstream, meaning that most imports will only
overwrite a string if it also was an import.

There are, though, two important exceptions:

* The first time that the translation of a string, in a particular language,
  is imported into Launchpad, it will take precedence over any existing
  translation made in that language in Launchpad.
* If an imported string matches the translation already made in Launchpad.
  This means that the translation will now be overwritten by any subsequent
  imports, if they differ. However, making a change to the translation in
  Launchpad would reset it to take precedence over imported strings.``

Next steps
----------

Launchpad can help you safeguard the quality of the translations you use
in your project. Choose a `review
policy <Translations/YourProject/PermissionPolicies>`__ for your
project's translations.