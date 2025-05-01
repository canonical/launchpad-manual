Preparing to translate
======================

You can use Launchpad to help translate free software, both directly
with upstream projects, (such as
`Limewire <https://translations.launchpad.net/limewire>`__), and also as
packages in distributions such as
`Ubuntu <https://translations.launchpad.net/ubuntu>`__.

When you're deciding what to translate, think about the following:

-  Can you work on the upstream project, rather than the distribution
   package?
-  Do you know and understand the software well enough to know the
   context of the strings you need to translate?
-  Are you familiar with the translation standards you'll need to stick
   to?

To learn about the processes and standards that a project applies to its
translations, you should get in touch with the translation team that
manages its localization into your language. Most projects work with a
translation group - an umbrella organization of many teams - who look
after translation quality control. Each translation group assigns teams
to look after particular languages.

.. note:: 
    You don't need to join that team in order to make
    translations: they exist to review translations.

You can find out which translation team to speak to by:

1. checking which translation group is associated with the project -
   visit the project's translations overview page, e.g.
   https://translations.launchpad.net/silva
2. visiting that translation group's overview page and reading its teams
   list.

Once you're in contact with the team, they'll tell you about their
standards and how to stay in touch with them through mailing lists, IRC
meetings and so on.

Licensing your translations
---------------------------

One of Launchpad's terms of use is that you agree to license all your
translations using the BSD license. This means that the translations you
make are compatible with as many open source licenses as possible.
There's more on this in our `translations licensing
FAQ <Translations/LicensingFAQ>`__.

When to translate distribution packages
---------------------------------------

Ubuntu and other operating systems (distributions) use Launchpad to
translate the software that they provide to their users. These
distributions take work from upstream projects and modify it, usually in
subtle ways, to make it suitable for their system and users.

**Only when** you understand the rules, standards, and complexities of
translating that particular package and you know why the distribution
translation needs to differ from the upstream one, should you translate
a distribution's package of a project

If the software you want to translate is available to translate both
directly as an upstream project (whether inside Launchpad or not) and as
a distribution package within Launchpad, you should talk to the upstream
project and the relevant Ubuntu translations team to see where your help
is most needed.

If you choose to translate Ubuntu packages, you may find the Ubuntu
community's `guide to translating
Ubuntu <https://wiki.ubuntu.com/TranslatingUbuntu>`__ helpful.

Where to start
--------------

Once you've been in touch with the relevant translation team, to learn
their standards etc, you can start translation straight away. You don't
need any special software or, in most cases, special permissions: all
you need are `your Launchpad account <YourAccount>`__, your web browser
and your translation skills!

When you're ready to get started, you need to tell Launchpad `which
languages you want to work
with <https://launchpad.net/people/+me/+editlanguages>`__. Next, choose:

-  **upstream project:** which line of development to translate; usually
   it'll be whichever is selected by default when you visit the
   project's translations overview page but check with the project
-  **distributions, such as Ubuntu:** which package you're going to
   translate.

Launchpad makes it easy to choose a distribution package by showing
which packages are most in need of your help.|

Red represents untranslated strings, whereas green, purple and blue
represent translated strings; Launchpad uses different colors for
translated strings to help you distinguish where and when the
translation was made.

Making your first translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click on the package or project language that you want to translate and
you'll see that each original English string has a section of the page.
Let's take a look at the `Esperanto translation of Ubuntu's xulrunner
package <https://translations.launchpad.net/ubuntu/hardy/+source/xulrunner-1.9/+pots/xulrunner/eo/+translate>`__.

In this example, you can see:

-  the original English string
-  a note on the string's context, to help you translate it more
   intelligently
-  any current translation
-  automatic suggestions: Launchpad looks through its database of
   millions of translated strings to see if that English string has been
   translated into Esperanto elsewhere
-  a text box, in case a new or altered translation is necessary
-  a note about which file the string appears in.

If you find a string that hasn't been translated or that you are certain
has been translated incorrectly, you should

Dealing with unusual characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many cases, your translation will be a straight conversion from
English to the target language. However, from time to time you may come
across unusual characters and character sequences. These are usually
variables, formatting or keyboard shortcuts.

How you handle them in your translation depends on what they are:

-  **Formatting:** you may see HTML, such as ``\`\``, used to format
   text in a string. Copy these tags exactly as you find them and apply
   them to the relevant part of the text, remembering to close the tags
   as appropriate. You may also see other tags, such as XML, and should
   treat them the same way.
-  **Data placeholders and variables:** in many development languages, a
   developer can insert data into a string by using a placeholder such
   as ``%s`` or ``%d``. You may also see more complex variations,
   such as ``%(variablename)s``, ``$name`` or ``${name}``.
   Copy these variables and placeholders exactly as you see, placing
   them in whichever part of the string makes most sense in the target
   language. If you're in doubt, ask another translator for advice.
-  **Keyboard shortcuts:** different development languages and
   frameworks use different ways to signify which key within a string
   should be used as a keyboard shortcut. Very often, if you see an
   underscore (e.g. ``Save \_As``) or ampersand (e.g. ``Print
   previe&w``) at the beginning or within a word, it may well be a
   keyboard shortcut. Ensuring you have a unique shortcut for each
   function is important and you should, at the very least, view the
   software in action and draw up a list of the shortcuts you plan to
   use before you start translating. You should place the underscore,
   ampersand or whichever other control character directly in front of
   the letter you want to use as the shortcut.

If you're unsure, speak to someone from the relevant translation team;
they'll be glad to help.

Further resources
-----------------

Read the `general translation guidelines <Translations/Guide>`__ and
know how to organize a localization team.