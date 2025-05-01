Translating your software
=========================

This section contains specific information about translating software into
your language. It contains details about what strings should be
translated and what not, what are plural forms and other things you
should be aware while translating software using Launchpad Translations
(Rosetta) or any other tool.

This guide does not include hint and tips about using Launchpad
Translations (Rosetta) as a translation tool. For such information
please read
`Translations/StartingToTranslate <Translations/StartingToTranslate>`__.

List of language-specific guidelines
------------------------------------

.. info::
    Before reading your language specific guide, please take a moment and
    read this general translation guide first

You are free to translate this guide and include it into your language
specific guide. You can use this information as a starting point for
developing the guidelines for your language.

To assure the translations quality for your language, it is recommended
to ask new translators to follow the information from the guidelines for
your language, or in case it is not ready yet, to point them to this
guide.

Basic rules for checking translations quality
---------------------------------------------

Below are listed some common sense rules to follow during the
translation work in order to improve the translation quality:

-  Pay attention to all section from the guidelines and always keep in
   touch with other translators

.. raw:: html

   <!-- end list -->

-  When you have translated a string, read it again and see if there are
   any error or the translations sound right in your language.

.. raw:: html

   <!-- end list -->

-  If the translated string does not make sense for you (or your
   mother/father), definitely it is wrong and you should redo/rephrase
   it.

.. raw:: html

   <!-- end list -->

-  If it feasible, always ask another team member to review your
   translations.

.. raw:: html

   <!-- end list -->

-  Translations consistency is an important aspect of translation
   quality.

.. raw:: html

   <!-- end list -->

-  Terminology dictionary

.. raw:: html

   <!-- end list -->

-  Before allowing new members in your team make sure they have
   previously done good translations and are aware of the team
   translation guide

Plural forms
------------

While the English language has 2 plural forms, it might happen that your
language has more or less than 2 plural forms.

Dealing with plural forms is one of the first question/problems for new
translators. It is recommended that your guidelines include information
and examples about the usage of plural forms in your language.

Example

::

   Romanian has 3 plural forms:

   Original text:
   msgstr[0] %d thing
   msgstr[1] %d things
   msgstr[2] %d things

   Translation:
   msgstr[0] %d lucru
   msgstr[1] %d lucruri
   msgstr[2] %d de lucruri

Menu accelerators / shortcuts
-----------------------------

Different development languages and frameworks use different ways to
signify which key within a string should be used as a keyboard shortcut.
Very often, if you see an underscore (e.g. Save \_As) or ampersand (e.g.
Print previe&w) at the beginning or within a word, it may well be a
keyboard shortcut.

Ensuring you have a unique shortcut for each function is important and
you should, at the very least, view the software in action and draw up a
list of the shortcuts you plan to use before you start translating. You
should place the underscore, ampersand or whichever other control
character directly in front of the letter you want to use as the
shortcut. If you have a program interface with the same fast access
character in different options/tabs/checkboxes/etc., you will have to
press the shortcut several times in the keyboard to walk through all of
them.

For other information about the accelerators in different languages,
refer to http://bazaar-vcs.org/BzrTranslations/Tips

Examples of menu accelerators:

::

   _File
   New &Tab
   ~Downloads

Translating DocBook (XML) files
-------------------------------

You can translate XML files using Launchpad Translations, by converting
the xml to a pot file, using xml2po, and then importing it in Rosetta.

When translating XML files please make sure you are aware of the
following things:

XML tags are case sensitive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using xml2po and then po2xml, xml tags and attributes are case
sensitive: Example:

::

   Original: See the <ulink url="http://ubuntustudio.org/">
   Correct: Vea el <ulink url="http://ubuntustudio.org/">
   Wrong: Vea el <UlinK Url="http://ubuntustudio.org/">

menuchoice tag
~~~~~~~~~~~~~~
"menuchoice" tag should include only "guibutton \| guiicon \| guilabel
\| guimenu \| guimenuitem \| guisubmenu \| interface" tags. Don't
include other tags or text outside of these tags.

Example:

::

   Original: <menuchoice><guimenu>Applications</guimenu><guisubmenu>Multimedia</guisubmenu><guimenuitem>Movie Player</guimenuitem></menuchoice>
   Correct: <menuchoice><guimenu>Apliaciones</guimenu><guisubmenu>Multimedia</guisubmenu><guimenuitem>Reproductor de películas</guimenuitem>
   Wrong: <menuchoice><guimenu>Apliaciones</guimenu><guisubmenu>Multimedia</guisubmenu>Reproductor de <guimenuitem>películas</guimenuitem>

What should not be translated
-----------------------------

This section contains general information about strings that should not
be translated and how to identify them.

Also to help you with identifying string that should not be translated,
software developers usually add comments describing the intend of the
text and tips about translating it. Always check the comments attached
to each string.

Data placeholders and variable names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In many development languages, a developer can insert data into a string
by using a placeholder such as **%s** or **%d**. You may also see more
complex variations, such as **%(variablename)s**, **$name** or
**${name}**. Copy these variables and placeholders exactly as you see
them (including the ending *s*), placing them in the exact order in
whichever part of the string makes most sense in the target language.

If you're in doubt, ask another translator for advice.

Examples:

::

   Original: I found $name ethernet device.
   Wrong: S-a găsit $cevanume dispozitiv ethernet
   Right: S-a găsit $name dispozitiv ethernet

   Original: Delete %(name)s ?
   Wrong: Ștergeți %(cevanume)le?
   Wrong: Ștergeți %(cevanume)s?
   Wrong: Ștergeți %(name)?
   Right: Ștergeți %(name)s?

Formatting/XML tags
~~~~~~~~~~~~~~~~~~~

You may see HTML/XML tags, such as , used to format text in a string.
Copy these tags exactly as you find them and apply them to the relevant
part of the text, remembering to close the tags as appropriate. You may
also see other tags, such as XML, and should treat them the same way.

Examples:

::

   Original: <strong>File name</strong>
   Wrong: <puternic>Nume fișier</puternic>
   Right: <strong>Nume fișier</strong>

Also you should not translate the xml tags attibutes and their values
(if you translate their values, make sure you know what you are doing
and check the developers comments). Examples:

::

   Original: <link linkend="desktop-themes">
   Right: <link linkend="desktop-themes">
   Wrong: <link linkend="temi del desktop">

Program parameters
~~~~~~~~~~~~~~~~~~

Command line parameters should not be translated.

Example

::

   Original: "The command line options are:\n"
             "       --quick         speeds up the processing\n"
             "       --slow          slows everything down."
   Wrong:    "Opțiunile comenzii sunt:\n"
             "       --repede         grăbește procesarea\n"
             "       --încet          încetinește totul."
   Right:    "Opțiunile comenzii sunt:\n"
             "       --quick         grăbește procesarea\n"
             "       --slow          încetinește totul."

TRUE/FALSE, GTK constants
~~~~~~~~~~~~~~~~~~~~~~~~~

Strings like "TRUE" , "FALSE" or gtk constants like "gtk-ok",
"gtk-cancel" or "toolbar-icon" should not be translated.

In many cases the presence of such string in a translations files is a
bug and the software developers should be informed about it and asked to
remove those strings.

GCONF configuration keys
~~~~~~~~~~~~~~~~~~~~~~~~

Examples:

::

   Original: The port which the server will listen to if the 'use_alternative_port' key is set to true.
            Valid values are in the range from 5000 to 50000.
   Wrong:   Portul pe care să asculte serverul în cazul în care cheia „folosește_port_alternativ” este activată.
            Valorile valide sunt între 5000 și 50000.
   Right:   Portul pe care să asculte serverul în cazul în care cheia „use_alternative_port” este activată.
            Valorile valide sunt între 5000 și 50000.

Context text
~~~~~~~~~~~~

In some old GNOME translations you might encounter translations context
encoded into the original string. For more information please see:
https://leofontenelle.wordpress.com/2007/12/01/context-in-gnome-translations/

Examples:

::

   Original: "Orientation|Top"
   Wrong: "Orientare|Sus"
   Wrong: "Orientation|Sus"
   Right: "Sus"

If you see such text please file a bug and inform the software
developers about the existence of context.

Translation statistics
----------------------

Throughout Launchpad Translations, statistics are shown for
translations. These are intended to give an overview of the status, so
that translators can easily see which translations are done and which
ones might need some work.

Here is an example of how statistics are shown for a translation
template in a particular language in Ubuntu:

Color meanings in the Status column
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on their status translation statistics can show different
colors to indicate each particular status of the strings. Here is what
the colours in the Launchpad Translation statistics mean:

-  Translated strings:

   -  **Green**: the translation imported from the upstream project and
      the one in Launchpad are identical.
   -  **Blue**: changed in Launchpad. The translation was imported from
      an upstream project, but translator chose to change it in
      Launchpad. The changed string will override the upstream one and
      be used in the distributed translations. Translators should keep
      these modifications to a minimum, and manually send them back to
      upstream if necessary.
   -  **Purple**: newly translated in Launchpad. The string is only
      translated in Launchpad. Translations imported from upstream did
      not have a translation for the string.

-  Untranslated strings:

   -  **Red**: untranslated. These strings have neither been translated
      in the upstream project nor in Launchpad

Lifecycle
~~~~~~~~~

During the lifecycle of translations, and while translators do their
work, there are some different paths in which the colours can change.
Here is a description of the most common scenarios:

-  **Red > Purple > Green**. In this scenario, the string was
   untranslated (Red), the translator translated it in Launchpad and
   there was no translation upstream (Purple). In the next translation
   import, the upstream translation has been done and coincides with the
   Launchpad one. This was because either an upstream translator made
   exactly the same translation or because the translator sent the
   translations back to upstream.

.. raw:: html

   <!-- end list -->

-  **Red > Purple > Blue > Green**. The string was untranslated (Red),
   the translator translated it in Launchpad and there was no
   translation upstream (Purple). In the next translation import, the
   upstream translation has been done and is different to the Launchpad
   one. This was probably because there was no communication between the
   upstream translator and the downstream one: the latter did not send
   his/her changes back to upstream, so upstream didn't know someone had
   already translated this somewhere else and translated it again, but
   differently. The way to get this translation to green is for the two
   translators to agree in a common translation, and either change it in
   Launchpad or upstream, depending on which one they might want to
   adopt.

.. raw:: html

   <!-- end list -->

-  **Red > Green**. The translation has been done upstream and it has
   been imported into Launchpad.

.. raw:: html

   <!-- end list -->

-  **Green > Blue**. A translator deliberately overrode an upstream
   translation. Upstream and Launchpad translations differ. These should
   be kept to a minimum, if necessary at all.

Running a localization team
---------------------------

Suggestions for sections included in your guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below are some ideas, hints, for some information that could be included
into the guidelines for your language:

-  A section describing the current focus for translations. What
   packages should be translated, their priority, due date... etc

.. raw:: html

   <!-- end list -->

-  Create or provide a communication channel for all translators. It can
   be a forum, mailing list, IRC channel. The main usage of this channel
   is to support team work, ask for help or suggestions.

.. raw:: html

   <!-- end list -->

-  Provide information about other team working on translations, links
   to other upstream projects. Try to keep in touch/sync with their
   work.

.. raw:: html

   <!-- end list -->

-  Decide what grammatical mode or tense is used when translating into
   your language.

.. raw:: html

   <!-- end list -->

-  Decide grammatical person and if you are going to use a formal or
   informal approach when translating software. T-V distinction.

.. raw:: html

   <!-- end list -->

-  Decide a common set of terminology or dictionary to be used by all
   translators. This will help creating uniform translations.

.. raw:: html

   <!-- end list -->

-  A section, or a dedicated page, containing examples of common errors,
   together with an explanation of the error and the suggested solution

.. raw:: html

   <!-- end list -->

-  A section, or a dedicated page, containing examples of strings that
   should not be translated.

Common/Best practice
~~~~~~~~~~~~~~~~~~~~

Below you will find a set of common practices for running a team

-  Don't forget about other translators or translations groups. In many
   cases you or your are not the only one doing translation in the free
   software ecosystem. Always keep in touch with that other teams are
   doing and make sure the translation teams for your language are
   translating free software using the same "language". Try to create or
   join a communication channel channel common to all translation teams
   for your language and use it for talking about important aspect that
   affect all translations.

.. raw:: html

   <!-- end list -->

-  Define a procedure for accepting new team members.

   -  

      -  The acceptance level may vary according to the percentage of
         already finished translations. For languages with few
         translators and translations already done team acceptance could
         be lower than in the case of a language with many translators,
         translations made and the presence of GTP, OpenOffice , etc
         upstream translation projects.
      -  Before accepting a member you may ask him/her to provide some
         translation. If the translations are great you may accept the
         new member. Otherwise giving feedback about why the translation
         are not good is a great help. Try to use a forum, mailinglist
         or IRC channel for giving feedback to potential new members.

.. raw:: html

   <!-- end list -->

-  Create a webpage/wikipage for the translations guide. This guide
   should contain:

   -  

      -  First rule: "If a translation does not make sense for you /
         your grandmother, definitely it is wrong!".
      -  Second rule: "Make your translation useful and adapt to the
         context. Don't follow always the original text". Like for
         example "Tile children" may sound funny in many languages so
         try "Arrange windows as tile". The original text is not always
         the correct one.
      -  a common terminology or a link to a common terminology
         dictionary or glossary. Don't forget about
         `open-tran.eu <http://open-tran.eu>`__ . You can also install
         `the glossary used by Romanian
         teams <http://www.i18n.ro/glosar>`__ (`here is the
         code <http://diacritice.svn.sourceforge.net/viewvc/diacritice/trunk/>`__)
      -  information about what should be translated and what not
      -  specific rules for translating into your language
      -  a list of frequent errors.
      -  explaining the plural form for your language and how to use
         them
      -  how you should translate menu accelerators / shortcuts
      -  inform the translators about other translation project and how
         we should cooperate and work together

.. raw:: html

   <!-- end list -->

-  Make sure you have a good communication channel for all members of
   the team or subteam. Try to reach all communication types:
   mailinglist, forum, IRC channel.

.. raw:: html

   <!-- end list -->

-  Let Launchpad know about your translation guide

.. raw:: html

   <!-- end list -->

-  Create a webpage / wiki where people could find general information
   about your team, such as:

   -  short and long term team goal
   -  new membership acceptance conditions
   -  translation guide
   -  common terminology (ex a link to a glossary, terminology list,
      dictionary)
   -  how to get in contact with the team (team contact or team members)

.. raw:: html

   <!-- end list -->

-  Make sure the team act as a team.

   -  Keep the team members up to date with the latest actions
   -  keep in contact with team members and try to collect feedback and
      status
   -  guide new members and help them get along with the team and
      translation work
   -  try to recruit new members into your translation team.

.. raw:: html

   <!-- end list -->

-  From time to time take a look at what other people are doing. In many
   cases you are not the only team/person translating software in your
   language.

Next steps
----------

Find more about joining and creating `translations groups and
teams <Translations/Groups>`__