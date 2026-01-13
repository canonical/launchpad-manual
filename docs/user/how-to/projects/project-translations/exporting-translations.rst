.. _how-to-export-translations:

Export translations
===================

.. include:: /includes/important_not_revised_help.rst

You can export your project's translations from Launchpad by requesting a 
one-off download through the web interface.

Requesting a one-off download
-----------------------------

You can request a ``.po`` or ``.mo`` file for any one or all of the languages
for which your project has translation efforts.

-  **Download all translations**: use the download link on the
   translations overview page for the relevant series of your project -
   e.g. https://translations.launchpad.net/silva
-  **Download translation for one language**: use the download link on
   that language's overview page - e.g.
   https://translations.launchpad.net/silva/trunk/+pots/silva/nl/+translate

Requesting a partial export
---------------------------

If you don't want to download a full PO file, you can request an export
of only those strings that have changed in Launchpad since the
translations were last imported. This is useful if you run an upstream
project that has its own translation effort and is also translated using
Launchpad for the Ubuntu distribution.

When you are on the web page for the PO file in question, select
``Download`` from the grey menu bar. You will be presented with the option
to choose the file format for the download - either ``PO format``, or ``MO
format``, or ``Changes from packaged translations in partial PO format``.
Choose the latter option for a partial export.

:ref:`Read more about partial exports <exporting-partial-gettext-PO-files>`.

Next steps
----------

Launchpad offers git hosting for your projects. Let's take a look at how you 
can :ref:`host code on Launchpad <host-your-project-code-on-launchpad>`.
