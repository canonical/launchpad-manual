.. _translation-import-policy:

Translation import policy
=========================

.. include:: /includes/important_not_revised_help.rst

When you start using Launchpad to translate a project, you need to
import the project's translation templates. Optionally, you may also
want to import any existing translations.

Launchpad supports GNU Gettext's *.pot* templates and *.po* translation
files.

To make translating in Launchpad run smoothly for everyone, we have a
few rules that you must follow to ensure a successful import of your
templates and translations. Some of these rules are social and cover
things such as whether you have permission from the project to start a
translation effort in Launchpad. The rest of the rules are technical.

Social rules
------------

When you request a new translation template import into Launchpad, you
should make sure of the following:

-  The project is published using an :ref:`open source licence <project-licenses>`, 
   or the project has a valid `commercial subscription <https://launchpad.net/+tour/join-launchpad#commercial>`__.
-  The project leaders are happy to publish translations made in
   Launchpad for their project using the BSD licence.
-  The project is not part of an organisation -- such as GNU or Debian
   -- that already uses another method of translation.
-  You represent the upstream project or you otherwise have permission
   from the project to start a translation effort on Launchpad.
-  If you're creating a new project in Launchpad, it must be generic and
   not specific to translations or a particular language: i.e.
   *myproject* not *myproject-translations*.

Technical rules
---------------

Whenever you upload a template for the first time, your project's
translations maintainer will need to check it manually. After that, it
should get through our automated approval process without problems.
You'll need to check each template uploaded using the following rules:

-  The template must be in GNU Gettext format and its file name end in
   ```.pot``` (see our `guidelines <#guidelines>`__ below for
   directory structure)
-  ```msgid``` strings must be in English, not any other language or
   symbolic identifiers.
-  If there are multiple template files, each should be in a separate
   directory. If you're uploading through the web interface, you can
   upload multiple template files as a tarball. Launchpad can see the
   directory structure inside the tarball. If you upload just a single
   file, all the browser gives us is its name and its contents.

If you are uploading translation files, you should follow these rules:

-  The file must be in GNU Gettext *.po* format.
-  Translation files should be in the same directory as the template to
   which they relate.
-  The translation files should be named for the appropriate language
   code: e.g. *pt_BR.po* Portugese as spoken in Brazil or *fr.po* for
   French as spoken in France. Launchpad only accepts languages that
   have an `ISO 639 code <http://en.wikipedia.org/wiki/ISO_639>`__.

   -  There are two exceptions to this rule: English as spoken in the UK
      must be named *en_GB.po* and Chinese. Chinese exists in Launchpad
      only as three variants: Simplified Chinese (*zh_CN*), Traditional
      Chinese (*zh_TW*) and Hong Kong Chinese (*zh_HK*).

Other useful guidelines
-----------------------

You can learn more about working with translations and templates in
*.po* and *.pot* format by reading the `GNU Gettext
documentation <http://www.gnu.org/software/gettext/manual/gettext.html>`__.

You should also be aware of the following:

-  Launchpad doesn't support translation to language variants (e.g.
   Serbian written in Latin, *sr@Latn*).
-  When naming translation files, you should leave out the country code
   if it is the primary or original country where that language is
   spoken. For example: *pt* for Portuguese, not *pt_PT*.

Sample directory layout
~~~~~~~~~~~~~~~~~~~~~~~

We recommend the standard GNU Gettext directory and file layout:

::

     template1/template1.pot
     template1/es.po
     template1/de.po
     ...
     template2/template2.pot
     template2/es.po
     template2/de.po

Working with upstream projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Thousands of people use Launchpad to translate software into their own
language. Once you open a project for translation in Launchpad, it's
likely that you'll get contributions from members of the Launchpad
translations community.

We want everyone's work in Launchpad Translations to have a chance of
making it into software that people use. That's why we insist that
anyone opening a project in Launchpad for translation must either
represent the upstream project or otherwise have permission from the
project. We'd hate to see people make translations only for them not to
stand a chance of being used in the project.

If you want to open a project for translation in Launchpad, but you're
not already involved in that project, you should get in touch with the
project.

Template for contacting upstream projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to suggest to a project that they use Launchpad to translate
their software, you might find this email template useful.

::

   Dear project maintainer,

   I am interested in translating your application X into the language L, and
   have noticed you don't have an established translation framework.

   I've been translating other programs using Launchpad Translations, a
   web-based translation service provided by Canonical (the primary sponsor of
   Ubuntu). Launchpad makes it easy for people to suggest translations and
   already has a community of thousands of translators.

   With Launchpad, all you'd need to do is publish a "translation template"
   -- in the form of a GNU Gettext .pot file -- via a web form when it best
   suits you (for example, when your next version is feature complete).  Once
   published in Launchpad Translations, it would be made available to the
   community of translators who would be then able to translate it.  When
   you're ready to release your next version, you would request an 'export' of
   all the available translations, which you would get in a tar.gz archive.

   Launchpad Translations is under continuous development, and features are
   being added and improved every month.  It is and will always be free of
   charge for free software projects.  For me, it would make translating your
   application very easy.

   You can learn more about Launchpad Translations at
   <https://launchpad.net/+tour/translation>.

   Thank you,
