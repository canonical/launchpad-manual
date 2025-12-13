.. _plural-forms-information-for-languages:

Plural forms information for languages
======================================

.. include:: /includes/important_not_revised_help.rst

When you ask that a new language be added to Launchpad or you see that
the information Launchpad has about a language is incomplete, you will
need to provide plural form information. As many are not familiar with
the term, here are some explanations.

The gettext manual also provides some `information about plural
forms <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`__.

Which information is needed?
----------------------------

Plural forms information for translation purposes consists of two
values:

1. A number that denotes how many plural forms the language uses, e.g.
   "2" for English.
2. A logical expression (C style) that calculates which plural form is
   used for which number of items (n) being named, e.g. "n != 1" for
   English.

Information about how plurals are constructed *grammatically* (e.g. "in
English you need to append an 's' to form the plural except when ...")
is **completely irrelevant** for the translation system and *please
don't try to explain them*. Of course, you will need to know and use
these rules when you are doing the translations but Launchpad does not
need to know them.

If you are still unsure what this plural form information is about, read
on.

Many languages, predominantly western languages like English, only know
two plural forms of a noun: singular and plural. The singular is used
for one item while the plural is used for more than one item. If you now
find yourself thinking "Yes sure, that's what 'plural' means, what else
should there be?" then your native language is most likely of that basic
type. Don't be confused when we talk about "two" plural forms because
the system considers the singular as "form 0" and the plural as "form
1", thus adding up to two forms.

Languages with two plural forms
-------------------------------

If your language works like explained above, similar to English, then
you already found the first piece of information. The number of plural
forms is "2". Now all you need to find out is the correct plural
expression for your language. We are only aware of two different
expressions for these languages and they depend on how you treat "Zero".

In English as it is used in computer software, plural is used for
"Zero". A program might output messages like:

-  "0 files have been copied."
-  "1 file has been copied."
-  "2 files have been copied."
-  etc.

The plural expression for English is "n != 1", meaning "Use the plural
when the number of items is not equal to 1". If your language works the
same way, you have found your plural expression. You are done.

The other treatment of "Zero" is to use the singular form for it, i.e.
in French "0 fichier, 1 fichier, 2 fichiers, etc." If your language
works like this, then your plural expression is "n > 1", meaning "Use
the plural form if the number of items is larger than 1". You are done.

Treatment of Zero
-----------------

Please be aware that normal grammatical plural rules may not include a
rule for zero items because the language uses the equivalent of
"nothing" in this case. Some have argued that this case may actually be
a third plural form. Considering English as an example, though, you'll
find that speaking a language is different to reading it on the computer
screen. Nobody will actually say "I bought zero apples." but rather "I
bought no apples." or even "I didn't buy any apples." Still, when
reading a message like "0 messages in your mailbox" on your computer
screen, nobody thinks it sounds funny. Please find out how "Zero" is
treated in computer software in your language before you start treating
it as a separate case which will only add complications later.

Languages with one plural form
------------------------------

Some languages, e.g. Japanese, use the same plural form for any number
of items. In this case the number of plural forms is "1" and the
expression is "0", meaning "Always use form 0". If your language works
like that, you are done.

Languages with more than two plural forms
-----------------------------------------

These languages use different plural forms depending on the number of
items. The `gettext
manual <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`__
shows an example for Polish which uses three plural forms. The greatest
number of plural forms we are aware of is six, which is used by Arabic.

The plural form expression is expected to return a number in the range 0
to nplurals-1 (nplurals being the number of plural forms) that picks the
right plural form with "0" usually being the singular form. It is
important that this expression and the numbering of plural forms remain
consistent throughout Launchpad so you should research which expression
may already be in use for your language outside of Launchpad. It is
likely that this expression has already been defined elsewhere.