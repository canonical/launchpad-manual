Engineering Overview: Translations
==================================

.. include:: ../includes/important_not_revised.rst

This is for engineers who are already familiar with the Launchpad
codebase, but are going to work on the Translations subsystem.

Use cases
---------

The purpose of Launchpad Translations is to translate programs'
user-interface strings into users' natural languages. To that end it
supports online translation, offline translation, uploads of translation
files from elsewhere, generation and download of translation files,
import from bzr branches, export to bzr branches, exports of language
packs, and so on. Something we're not very good at yet is helping users
bring Launchpad translations back upstream.

We've got two major uses for Translations:

1. Ubuntu and derived distributions.
2. Launchpad-registered projects.

Sometimes we refer to these as the two “sides” of translation in
Launchpad: the *ubuntu side* and the *upstream side.*

Where possible, the two sides are unified (in technical terms) and
integrated (in collaboration terms). But you'll see a lot of cases where
they are treated somewhat differently. Permissions can differ,
organisational structures differ, and some processes only exist on one
side or the other.

At the most fundamental level, the two sides are integrated through:

-  *global suggestions* — "here's a translation that was used /
   suggested elsewhere for this same string"
-  *translations sharing* — individual translations of the same string
   can be shared in multiple places. This is a complex and multi-layered
   affair that you'll see coming back later in this document.

Ubuntu side
~~~~~~~~~~~

In a distribution, translation happens in the context of a source
package. That is, a given ``SourcePackageName`` in a given
``DistroSeries``.

Translations sharing happens within a source package, between different
distribution release series.

Most translations come in from upstream (Debian, Gnome), but we have a
sizeable community of users completing and updating these translations in
Launchpad.

Ubuntu has a team of `translations
coordinators <https://launchpad.net/~ubuntu-translations-coordinators>`__
in charge of this process.

Projects side
~~~~~~~~~~~~~

In a project, translation happens in the context of a project release
series. That is, a ``ProductSeries``.

Translations sharing happens between the release series of a single
project.

Project groups also play a small role in permissions management, but we
otherwise pretend they don't exist.

Structure and terminology
-------------------------

Essentially all translations in Launchpad are based on
`gettext <http://www.gnu.org/software/gettext/manual/>`__. Software
authors mark strings in their codebase as translatable; they then use
the gettext tools to extract these and get them into Launchpad in one of
several ways. We also call the translatable strings *messages.*
Translatable strings are presumed to be in U.S. English (with language
code \`en`).

The top-level grouping of translations is a *template.* A
\`ProductSeries\` or \`SourcePackage\` can contain any number of
templates; typically it needs only one or two for the main program, a
main library that the program is built around, and so on; on the other
hand some projects create a template for each module.

Because of our gettext heritage, we also refer to these templates as
“POTs,” “PO templates,” or “pot files.”

In python terms, think:

::

   productseries.potemplates = [potemplate1]
   potemplate1.productseries = productseries

   sourcepackage.potemplates = [potemplate2]
   potemplate2.sourcepackage = sourcepackage

A template can be on only one “side”; it belongs to a product series or
to a source package, but not both.

Each template can be translated to one or more languages. Again because
of our gettext heritage, translation of a template into a language is
referred to as a *PO file.* A PO file is not just a shapeless bag of
translated messages; it specifically translates the messages currently
found in its template.

In python terms:

::

   potemplate.pofiles = {
       language: pofile,
       }

   pofile.language = language
   pofile.potemplate = potemplate

(A gettext PO file is pretty much the same as a template file. A bit of
metadata aside, the big difference is that a template leaves the
translations blank.)

The currently translatable messages in a template (“pot message sets”)
form a numbered sequence. This sequence defines which messages need to
be translated in the PO files. Messages that are no longer in the
template are *obsolete*; we may still track them but they are no longer
an active part of the template.

In python terms, think:

::

   potemplate.potmsgsets = [potmsgset1]
   potemplate.obsolete_potmsgsets = set([potmsgset2])

Think of a translated string in a PO file as a *translation message.*
This gets a bit more complicated once you start looking at the database
schema, but from the perspective of a PO file it's accurate.

::

   translation_message1.potmsgset = potmsgset1
   translation_message1.language = pofile.language

The actual translation text in a translation message is immutable. A
translation message will be updated with review information and such,
but its “contents” are fixed. From the model's perspective there's no
such thing as *changing* a translated string; that just means you create
or select a different translation message.

A translation message can be *current* in a given PO file, or not. It's
an emergent property of more complex shared data structures. So you can
view a PO file as a customisable “view” on the current translations of a
particular template into a given language.

::

   pofile.current_translation_messages = {
       potmsgset1: translation_message1,
       }

Often a translation message translates a message from a PO file's
template into the PO file's language, but is not current (from the
perspective of that PO file). In that case we consider it a
*suggestion.* We make it easy for users with the right privileges to
select suggestions to become current translations.

::

   pofile.suggestions = {
       potmsgset2: [translation_message2],
       }

Plural forms
~~~~~~~~~~~~

A language can have one or more *plural forms.* These are the forms a
message can take depending on the value of a variable number that is
substituted into the message. For example, English has 2 forms: a
singular (“%d file” for 1) and plural (“%d files” for all other
numbers). Many languages lack this distinction; some are just like
English; some use the singular for the number zero; and some have more
forms, such as Arabic which has 6.

GNU gettext knows how to choose the right form and substitute the
variable in one go. We define a *plural formula* for each language, and
that's what determines which form should be used for which numbers.

Thus sometimes a translatable message that includes a number may
actually consist of 2 strings (one for singular, one for plural).
Similarly a translation message may contain one string per plural form
in the language. Only very few translatable messages need a plural form
though; most translatable messages and translations consist of a single
string each.

Workflow
--------

Everything starts with templates. Usually a project owner or package
maintainer somewhere outside of Launchpad is responsible for producing
these and uploading them to Launchpad. There are a few automated streams
though: Soyuz package builds can produce them. For projects we can
import them from the development branch, and in some cases we can even
generate them from there automatically.

A template is the one thing that absolutely every project must provide
before it can be translated. There is no way to edit a template's
contents in the web UI; it has to be imported as a file.

Once a template has been created, and it contains translatable messages,
people can start translating. They can do this through the web UI, or
they can upload translation files in much the same was as the project
owners can upload template files. Translations can also be imported from
a bzr branch, just like a template.

Depending on the wishes of the project owner, translation can be a
single-stage process (“people enter translations”) or a two-stage
process (“translators enter translations, reviewers check them and
approve the good ones”).

Naturally, translations can be exported. The application will generate
PO files and templates on the fly based on the data in the database. It
can generate individual files, or tarballs for aggregate downloads. On
the Ubuntu side, there is also a mechanism for generating language packs
that is largely independent from the normal export mechanism.

Suggestions and translations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Looking within any given POFile, a POTMsgSet can have any number of
translations, of varying degrees of applicability:

1. At most one \`TranslationMessage\` is its *current* translation. This
   is actually more complex than it seems: it could be shared or
   diverged, and may be current on both translation sides or only on the
   side the POFile is on.
2. Other translations may have been submitted for the same POTMsgSet and
   language, but not be current in this POFile. We call these *local
   suggestions*. Technically, even a previously current translation
   that's been superseded by a better one is considered a suggestion;
   usually we only care about ones that were submitted after the
   incumbent translation was made current.
3. There could be other POTMsgSets elsewhere with the exact same
   translatable string. Any translation messages for those, to the same
   language as our POFile, are called *global suggestions*.

When translating in the UI, a suggestion shows up as a ready-made
translation that you can just select and approve. This, in principle, is
what translation teams do. They review suggestions made by translators.
Translation itself generally requires no special privileges.

A user with review privileges on a given translation can operate in
“reviewer mode,” where everything they enter automatically becomes
current, or in “translator mode” where any translations they enter go
into the system as suggestions.

Global suggestions are one of Launchpad Translations' key features. If
you want to translate the string “Quit” into Japanese for your program,
there are probably only one or two translations that everybody else
uses. Launchpad will show you those so that you don't need to come up
with your own. It's an example of horizontal integration between
projects.

Local suggestions are shared. There is no such thing as a diverged
suggestion. When you enter a suggestion for a given POTMsgSet and
Language, it applies to all POFiles for the same language that share
that same POTMsgSet.

Uploads
~~~~~~~

**TODO:**

-  Templates generally need uploading.
-  Currently privileged.
-  Per series, per template, per PO file.
-  One queue record per user / POFile / ….

Automated uploads
~~~~~~~~~~~~~~~~~

We have a few streams of automated uploads:

-  Templates and translations from distro package builds (*Soyuz
   uploads*).
-  Import of templates and translations from Bazaar branches (*bzr
   integration*).
-  For some projects we support automatic generation of templates from
   source updates, using the build farm (*template generation*).

Some of these streams have their own custom “approval” logic for
figuring out which file should be imported where. This is because
automated processes give us more consistent file paths and such. If the
custom logic fails to match uploads with PO files or templates, the work
is generally left to the import queue gardener.

Soyuz uploads are different in that regard: all its custom logic is
built into the gardener because the two developed hand in hand. Mainly
for this reason, the gardener's approval logic is fiendishly complex.

Permissions and organisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Message sharing
~~~~~~~~~~~~~~~

**TODO:**

-  Why divergence?
-  Why can't messages always track?

Objects and schema
------------------

In a nutshell:

-  A \`POTemplate\` lives in either a \`ProductSeries\` or a
   \`SourcePackage\` (in the database: \`(SourcePackagename,
   DistroSeries)`).
-  A \`POFile\` is the translation of a \`POTemplate\` to a \`Language`.
-  A \`POTMsgSet\` is a translatable message.
-  \`TranslationTemplateItem\` is a linking table. It says which
   \`POTMsgSet`s participate in which \`POTemplate`s.
-  A \`TranslationMessage\` translates a \`POTMsgSet\` to a \`Language\`
   on one translation side, or if diverged, specifically in one
   \`POTemplate`.
-  A \`POMsgID\` holds the text of a translatable string; \`POTMsgSet\`
   refers to it (once for singular, once for plural if appropriate).
-  A \`POTranslation\` holds the text of a translated string;
   \`TranslationMessage\` refers to it (once for every plural form in
   the language).
-  A \`TranslationGroup\` is an organisational structure for managing
   translations.
-  A \`Translator\` is an entry in a \`TranslationGroup\` saying who is
   responsible for a particular \`Language`.
-  A \`POExportRequest\` is an entry in the translations export queue.
-  A \`TranslationImportQueue\` entry is an upload on the translations
   import queue.

Our largest database table is \`TranslationMessage`. Once upon a time it
grew to 300 million rows, but thanks to message sharing it's now a
fraction of that size.

Message sharing
~~~~~~~~~~~~~~~

A single \`POTMsgSet\` (translatable message) can participate in
multiple templates. We then call these templates *sharing templates.*
And that means that a translation message to, say, Italian will be
available in each of those templates' PO file for Italian.

This is where it gets complicated; please fasten your seat belts and
extinguish smoking motherboards.

A translation message can be in one of three sharing states:

1. **Diverged.** The translatable message may be in multiple templates,
   but this particular translation of it is specific to just one of
   those templates.
2. **Shared.** The translation is valid for all the PO files *on this
   translation side* whose templates share the same translatable
   message. Some of those PO files may have diverged translations
   overriding it, but this one is the default.
3. **Tracking.** The translation is not only shared on one translation
   side, but between both translation sides.

We have a design document that specifies how messages in these states respond to changes. We try
to make it easy to move a translation down this list (towards tracking)
and hard to move up the list (towards diverged).

Which message is current?
^^^^^^^^^^^^^^^^^^^^^^^^^

The usage and sharing state of a translation message is recorded as
three data items:

-  “current on the Ubuntu side”
-  “current on the upstream side”
-  “diverged for template X”

(By the way, that leaves some redundant possibilities: a diverged
message can only be current on the side of the template it's specific
to. And a message shouldn't be diverged if it's not current.)

So given a PO file and a translatable message, how do you find the
current translation message? Look for one with:

-  the same language as the PO file,
-  the translatable message you're looking for,
-  its “current” bit set for the side your PO file's template is on, and
-  diverged to your template or, if no message matches, not diverged at
   all.

(On a side note, this is why “simple” translation statistics can be quite
hard to compute.)

Which templates share?
^^^^^^^^^^^^^^^^^^^^^^

There are two separate notions of which templates share. You'd expect
these to be the same thing, but reality gets a bit more complicated:

-  **Sharing templates** have one or more translatable messages in
   common, regardless of how that happened.
-  An **equivalence class** is a set of templates that *should* share
   their messages if possible, regardless of whether they actually do.

Why the difference? Sharing templates is a useful term for reasoning
about data, but as a rule the code doesn't care about them (and would
find it a costly thing to query if it did). But when the application
adds a translatable message to a template X, it does care about
equivalence classes. If another template Y in the same equivalence class
already has the same translatable string, no new message is created; the
existing one from Y is simply added to X.

After that, lots of things can happen: templates can be renamed, moved,
added, deleted; administrators may have to change data by hand. And
that's where differences between "sharing templates" and the
"equivalence class" can sneak in. But in principle they should be more
or less the same.

An equivalence class consists roughly of all templates with the same
name, in a project and its associated Ubuntu package. Look at
\`POTemplateSharingSubset\` for the details.

Processes
---------

Import queue
~~~~~~~~~~~~

**TODO:** Describe.

Gardener
^^^^^^^^

**TODO:** Describe.

Export queue
~~~~~~~~~~~~

**TODO:** Describe.

Language packs
~~~~~~~~~~~~~~

**TODO:** Describe.

Bazaar imports
~~~~~~~~~~~~~~

**TODO:** Describe.

Bazaar exports
~~~~~~~~~~~~~~

**TODO:** Describe.

Template generation
~~~~~~~~~~~~~~~~~~~

**TODO:** Describe.

Statistics update
~~~~~~~~~~~~~~~~~

**TODO:** Describe.

Packaging translations
~~~~~~~~~~~~~~~~~~~~~~

**TODO:** Describe.

Translations pruner
~~~~~~~~~~~~~~~~~~~

**TODO:** Describe.

Caches
------

POFileTranslator
~~~~~~~~~~~~~~~~

Here is Launchpad Translations' equivalent of Cobol: old, ugly, in
desperate need of an overhaul — and as yet, irreplaceable.

\`POFileTranslator\` caches who contributed to which \`POFile`s, and
when. It's always been the basis for listing contributors, but we have
started using it for more. It's how we list a user's translation
activity on their personal Translations page. We're not sure the table
is really a very good fit for that; its purpose has become diluted and
we haven't fully reviewed how it matches our needs.

The \`POFileTranslator\` table is kept very roughly consistent by a
database trigger on \`TranslationMessage`. But we decided to move that
work into python. That would be particularly useful for translation
imports, where we do mass updates to (mostly) a single set of PO files
for a single users.

Status as of 2012-05-14: the trigger is about to be simplified so that
it takes care of creating new \`POFileTranslator\` records as needed,
but it will no longer try to clean up ones that become obsolete, or keep
track of the most recent \`TranslationMessage\` a user contributed. A
daily “scrubbing” job is about to land as part of Garbo, which will take
care of eventual consistency.

SuggestivePOTemplate
~~~~~~~~~~~~~~~~~~~~

The database query that looks for global suggestions is relatively
costly, and we need to do it for every translatable message on a
translation page. Its complexity also makes the SQL logs hard to follow.

A large part of this query (in terms of SQL text) was involved in
finding out what templates were eligible for taking suggestions from.
This part was also completely repetitive, and it doesn't even need to be
immediately consistent, so we materialised it as a simple cache table
called \`SuggestivePOTemplate`.

We refresh this cache all the time by clearing out the table and
rewriting it. This keeps the code simple and it's certainly fast enough
— we used to gather the same data 10× per page. Some changes may also
update it incrementally.

So don't worry if anything happens to this data. It will be rewritten
very soon.

POTExport
~~~~~~~~~

This isn't really a cache, but it was sort of meant as one. It's a
database view on a join that was apparently once meant to speed up
translation exports. To express that a view is involved, the model class
is called \`VPOTExport`.

In all probability though, this does not help performance in any way
whatsoever. There used to be a similar view for translations, called
\`POExport`, and removing it from our code has done a lot to speed up
exports. It also simplified the code.

But removing \`POTExport\` has never become a priority. It's simpler
than \`POExport\` was, so probably less costly; and as a rule there's
much less template data to export than there is translation data. So
getting rid of this would be a nice cleanup, but not vital.

UI shortcuts
------------
* Import queue: https://translations.launchpad.net/+imports
* Languages: https://translations.launchpad.net/+languages
* Translation groups: https://translations.launchpad.net/+groups

