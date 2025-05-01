Translating your project
========================

While development usually takes place in English, free software is used
by people in hundreds of different languages across the globe.

Launchpad applies two of the great benefits of the open source
development model to translating your software:

-  anyone can translate and/or suggest translations
-  translations are easily shared between projects.

Importantly, Launchpad's simple web interface provides a friendly
environment in which non-technical people can help translate your
software, while its support of the popular GNU Gettext file formats
makes it easy to integrate their work into your project.

Licensing
---------
.. important::
    We require that all translations made in Launchpad are BSD licensed.
    This does not apply to translations imported from elsewhere. Read more
    about translation licensing.

Getting started
---------------

You need to do three things before people can use Launchpad to translate
your project:

1. Enable translation by following the Change details link on your
   project's overview page and selecting Translations for this project
   are done in Launchpad.
2. Upload a translation template and any existing translation files to
   the series you want to translate.
3. Choose a permissions policy - i.e. decide who can make what sorts of
   changes to your translations.

Let's take a look at those in more detail.

Preparing your software for translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launchpad uses GNU gettext's file formats to import and and export
translations:

-  ``.pot``: a template that includes the English text that you want
   people to translate. `What's this? </../POTemplates>`__
-  ``.po``: translations for one language in a human-readable and
   editable form.
-  ``.mo``: a compiled binary form of a .po file.

You can find out more about these file formats and using GNU gettext in
the `Gettext manual <http://www.gnu.org/software/gettext/manual/>`__.

.. tip::
    You may also find `Malcolm Tredinnick's Gnome internationalisation
    guide <http://www.gnome.org/~malcolm/i18n/>`__ useful, although some
    of the Gnome policies mentioned in that guide are now out of date.

To make your project available for translation, you must upload at least
one .pot translation template file. This file tells Launchpad which
English strings you want to make available for translation.

Further information
-------------------

Let us now look at how to `get your translation templates into
Launchpad <Translations/YourProject/ImportingTemplates>`__.