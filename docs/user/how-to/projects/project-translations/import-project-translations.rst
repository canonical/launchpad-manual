.. _how-to-import-project-translations:

Import your project's translations
==================================

.. include:: /includes/important_not_revised_help.rst

Just as with translation templates, you can import translation files
(``.po``) by uploading a tarball of templates and translation files through the
web interface.

If you already have your translation files in a git branch, you may find that 
to be the easiest source for importing your translation files.

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

Upload a tarball of your translation files
------------------------------------------

Visit your project's translations overview page and click the link for
the ``trunk`` series. Upload a tarball containing your translation files
``preserving directory structure``.

Avoiding common problems
------------------------

Your translations stand a better chance of a quick import import if you follow 
these guidelines:

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
in your project. Choose a :ref:`review policy <choosing-a-permissions-policy>`
for your project's translations.
