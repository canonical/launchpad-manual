Export translations
===================

Just as with `importing
templates <Translations/YourProject/ImportingTemplates>`__ and
`translations <Translations/YourProject/ImportingTranslations>`__, there
are two ways to export your project's translations from Launchpad:

-  by asking Launchpad to make regular commits to a Bazaar branch you
   specify
-  or requesting a one-off download through the web interface.

Committing translations to a Bazaar branch
------------------------------------------

Launchpad can produce a regular snapshot of your translations and commit
it to a Launchpad-hosted Bazaar branch of your choice. Using this export
method, you can always find a reasonably fresh export of your
translations in the same place, and download it automatically, without
any asynchronous requests.

It also means that large numbers of developers or translators can get
regular, fresh updates of the translation files.

Enabling
~~~~~~~~

The first thing you need is a branch. It doesn't have to be a branch
directly associated with your project, but you do have to be the owner,
or a member of the team that owns the branch, and it must be hosted
directly on Launchpad.

.. tip::
    Not sure how to upload a branch to Launchpad?
    `See our guide <Code/UploadingABranch>`__.|\|

At the moment, `team-owned branches don't work as
expected <https://bugs.launchpad.net/rosetta/+bug/407260>`__. To work
around this, make yourself the owner of the branch, set it as the
translations branch, and then make the team the owner of the branch
again.

Now, visit the overview page for the series you're translating, select
the ``Translations`` tab and then click ``Settings``.

On the ``Settings`` page, scroll down to the ``Export translations to
branch`` section and set the branch where you want Launchpad to commit
translations.

If you leave the project at any time, Launchpad will still export the
translations to the same branch. It is up to the then project owners to
change the destination branch.

Launchpad overwrites existing translation files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Launchpad commits translation files to your branch once a day. You
should note that Launchpad does not "edit" the translation files by
adding new strings.

.. warning::
    The export **brutally overwrites** any previous versions of the
    files in your branch.

In the file that Launchpad writes, translations may have changed but
messages may also appear in a different order, or with different
comments, and so on.

So, do not expect files that you can merge back into the originals
without any further work! The Launchpad database and Bazaar have
completely different views of this data.

Directory layout
^^^^^^^^^^^^^^^^
In the branch, each translation file will have a normalised name
(``de.po`` for a German translation, ``zh_CN.po`` for Simplified Chinese,
``eo.po`` for Esperanto, and so on). Each translation sits in the same
directory where its template was located on import.

If you have multiple templates, make sure that they have different
directory paths, or the translation files for one will overwrite those
for the other! It was already recommended practice to give each template
its own directory.

Templates are not exported.

Disabling
~~~~~~~~~

If you want to disable the exports, go back to the *Settings* page for
that series' translations, then click the "pencil" icon next to the
branch name. There you can select a different branch or simply clear the
input field.

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

Partial exports
---------------

If you don't want to download a full PO file, you can request an export
of only those strings that have changed in Launchpad since the
translations were last imported. This is useful if you run an upstream
project that has its own translation effort and is also translated using
Launchpad for the Ubuntu distribution.

Requesting a partial export
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you are on the web page for the PO file in question, select
``Download`` from the grey menu bar. You will be presented with the option
to choose the file format for the download - either ``PO format``, or ``MO
format``, or ``Changes from packaged translations in partial PO format``.
Choose the latter option for a partial export.

`Read more about partial exports <Translations/YourProject/PartialPOExport>`__.

Next steps
----------

Launchpad works with Bazaar to host, mirror and catalogue to branches of
your project's code. It can even import git, Subversion and CVS
repositories into Bazaar branches. Let's take a look at `hosting code
with Launchpad <Code>`__.
