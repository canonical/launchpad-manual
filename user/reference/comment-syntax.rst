Launchpad Comment Parsing
=========================

This page aims to introduce the most important elements of comment's
syntax on Launchpad at a glance.

Whitespaces
-----------

Launchpad will

-  cut off any whitespace to the right and
-  keep any whitespace to the left and
-  reduce any whitespace between non-whitespace characters to just one.

.. note::
    Technically Launchpad passes whitespace through and the browser
just ignores the whitespace.

Examples
~~~~~~~~

`This sentence has varying amounts of whitespace between its words.`

will look like this:

`This sentence has varying amounts of whitespace between its words.`

--------------

Keep in mind that you have a bad time writing tables

::

   | Column 1   | Column 2 | Column 3    |
   |------------+----------+-------------|
   | Lorem      | ipsum    | dolor       |
   | sit        | amet     | consectetur |
   | adipiscing | elit     | sed         |

will loke like this

::

   | Column 1 | Column 2 | Column 3 |  
   |------------+----------+-------------|  
   | Lorem | ipsum | dolor |  
   | sit | amet | consectetur |  
   | adipiscing | elit | sed |

because any whitespace between non-whitespace characters gets reduced to
just one

Paragraphs
----------

Just like the whitespace between words. Multiple new-line characters
will be reduced to one.

Example
~~~~~~~

::

   Here are two paragraphs with lots of whitespace between them.




   But they're still just two paragraphs

will look like this:

::

   Here are two paragraphs with lots of whitespace between them.  
      
   But they're still just two paragraphs

Mention a single Launchpad Bug
------------------------------

Synopsis
~~~~~~~~

::

   bug <LP-Bug-Number>
   bug #<LP-Bug-Number>
   bug number <LP-Bug-Number>
   bug num <LP-Bug-Number>
   bug num. <LP-Bug-Number>
   bug no <LP-Bug-Number>
   bug no. <LP-Bug-Number>
   bug report <LP-Bug-Number>
   bug-report <LP-Bug-Number>
   bug-<LP-Bug-Number>
   bug=<LP-Bug-Number>

Note that these patterns are case invariant.

Examples
~~~~~~~~

::

   bug 123
   bug    123
   bug #123
   bug number 123
   bug number. 123
   bug num 123
   bug num. 123
   bug no 123
   bug report 123
   bug no. 123
   bug#123
   bug-123
   bug-report-123
   bug=123
   debug #52

will look like this:

| `bug 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug #123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug number 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > bug number. 123<
| > `bug num 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug num. 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug no 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug report 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug no. 123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > bug#123<
| > `bug-123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug-report-123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > `bug=123 <https://bugs.launchpad.net/bugs/123>`__\ <
| > debug #52

Mention multiple Launchpad Bugs
-------------------------------

Synopsis
~~~~~~~~

::

   LP: #<LP-Bug-Number>[, #<LP-Bug-Number>]...

Note that these patterns are case invariant. The amount of whitespace
can be variable, but if you place whitespace anywhere else; the regular
expression might not parse the input correctly.

Examples
~~~~~~~~

::

   LP: #1
   (LP: #1)
   LP: #1, #2.
   LP:
   #1,
   #2,
   #3,
   #4
   lp: #1
   (lp: #1)
   lp: #1, #2.
   LP #1
   LP: #1 , #2
   LP: #1, #2,

   #3

will look like this:

| LP: `#1 <http://example.net>`__\ <
| > (LP: `#1 <http://example.net>`__)<
| > LP: `#1 <http://example.net>`__, `#2 <http://example.net>`__.<
| > LP: <
| > `#1 <http://example.net>`__,<
| > `#2 <http://example.net>`__,<
| > `#3 <http://example.net>`__,<
| > `#4 <http://example.net>`__\ <
| > lp: `#1 <http://example.net>`__\ <
| > (lp: `#1 <http://example.net>`__)<
| > lp: `#1 <http://example.net>`__, `#2 <http://example.net>`__.<
| > LP #1<
| > LP: `#1 <http://example.net>`__ , #2<
| > LP: `#1 <http://example.net>`__, `#2 <http://example.net>`__,<
| > <
| >

1. 3

Mention a Branch
----------------

You can link a launchpad branch by mentioning it with the \`lp\` URI
syntax. \`lp\` will expand to https://bugs.launchpad.net/+code/

Synopsis
~~~~~~~~

::

   lp:<Relative-URL>
   lp:/<Relative-URL>
   lp:///<Relative-URL>

Note that these patterns are case invariant.

Examples
~~~~~~~~

::

   lp:~foo/bar/baz
   lp:~foo/bar/bug-123
   lp:~foo/+junk/baz
   lp:~foo/ubuntu/jaunty/evolution/baz
   lp:foo/bar
   lp:foo
   lp:foo,
   lp:foo/bar.
   lp:foo/bar/baz
   lp:///foo
   lp:/foo

will look like this:

| `lp:~foo/bar/baz <https://bugs.launchpad.net/+code/~foo/bar/baz>`__\ <
| >
  `lp:~foo/bar/bug-123 <https://bugs.launchpad.net/+code/~foo/bar/bug-123>`__\ <
| >
  `lp:~foo/+junk/baz <https://bugs.qastaging.launchpad.net/+code/~foo/+junk/baz>`__\ <
| >
  `lp:~foo/ubuntu/jaunty/evolution/baz <https://bugs.qastaging.launchpad.net/+code/~foo/ubuntu/jaunty/evolution/baz>`__\ <
| >
  `lp:foo/bar <https://bugs.qastaging.launchpad.net/+code/foo/bar>`__\ <
| > `lp:foo <https://bugs.launchpad.net/+code/foo>`__\ <
| > `lp:foo <https://bugs.launchpad.net/+code/foo>`__,<
| > `lp:foo/bar <https://bugs.launchpad.net/+code/foo/bar>`__.<
| > `lp:foo/bar/baz <https://bugs.launchpad.net/+code/bar/baz>`__\ <
| > `lp:///foo <https://bugs.launchpad.net/+code/foo>`__\ <
| > `lp:///foo <https://bugs.launchpad.net/+code/foo>`__\ <
| >

Mention an FAQ Thread
---------------------

You can link a launchpad FAQ thread by mentioning the number.

Synopsis
~~~~~~~~

::

   faq <faq-number>
   faq #<faq-number>
   faq-<faq-number>
   faq=<faq-number>
   faq item <faq-number>
   faq number <faq-number>

Note that these patterns are case invariant.

Examples
~~~~~~~~

::

   faq 1
   faq #2
   faq-2
   faq=2
   faq item 1
   faq  number  2

will look like this:

| `faq 1 <faq_1>`__\ <
| > `faq #2 <faq_#2>`__\ <
| > `faq-2 <faq-2>`__\ <
| > `faq=2 <faq=2>`__\ <
| > `faq item 1 <faq_item_1>`__\ <
| > `faq number 2 <faq_number_2>`__\ <
| >

URIs
----

Launchpad can recognize \`http`, \`https`, \`ftp`, \`sftp`, \`mailto`,
\`news`, \`irc\` and \`jabber\` URIs.

\`tel`, \`urn`, \`telnet`, \`ldap\` URIs, relative URLs like
"`example.com <https://example.com/>`__" and E-Mails like
"test@example.com" are **NOT** recognized.

Examples
~~~~~~~~

::

   http://localhost:8086/bar/baz/foo.html
   ftp://localhost:8086/bar/baz/foo.bar.html
   sftp://localhost:8086/bar/baz/foo.bar.html.
   http://localhost:8086/bar/baz/foo.bar.html;
   news://localhost:8086/bar/baz/foo.bar.html:
   http://localhost:8086/bar/baz/foo.bar.html?
   http://localhost:8086/bar/baz/foo.bar.html,
   <http://localhost:8086/bar/baz/foo.bar.html>
   <http://localhost:8086/bar/baz/foo.bar.html>,
   <http://localhost:8086/bar/baz/foo.bar.html>.
   <http://localhost:8086/bar/baz/foo.bar.html>;
   <http://localhost:8086/bar/baz/foo.bar.html>:
   <http://localhost:8086/bar/baz/foo.bar.html>?
   (http://localhost:8086/bar/baz/foo.bar.html)
   (http://localhost:8086/bar/baz/foo.bar.html),
   (http://localhost:8086/bar/baz/foo.bar.html).
   (http://localhost:8086/bar/baz/foo.bar.html);
   (http://localhost:8086/bar/baz/foo.bar.html):
   http://localhost/bar/baz/foo.bar.html?a=b&b=a
   http://localhost/bar/baz/foo.bar.html?a=b&b=a.
   http://localhost/bar/baz/foo.bar.html?a=b&b=a,
   http://localhost/bar/baz/foo.bar.html?a=b&b=a;
   http://localhost/bar/baz/foo.bar.html?a=b&b=a:
   http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%f~g#h,j!k-l+m$n*o'p
   http://www.searchtools.com/test/urls/(parens).html
   http://www.searchtools.com/test/urls/-dash.html
   http://www.searchtools.com/test/urls/_underscore.html
   http://www.searchtools.com/test/urls/period.x.html
   http://www.searchtools.com/test/urls/!exclamation.html
   http://www.searchtools.com/test/urls/~tilde.html
   http://www.searchtools.com/test/urls/*asterisk.html
   irc://chat.freenode.net/launchpad
   irc://chat.freenode.net/%23launchpad,isserver
   mailto:noreply@launchpad.net
   jabber:noreply@launchpad.net
   http://localhost/foo?xxx&
   http://localhost?testing=[square-brackets-in-query]

will look like this:

| http://localhost:8086/bar/baz/foo.html
  ftp://localhost:8086/bar/baz/foo.bar.html
  sftp://localhost:8086/bar/baz/foo.bar.html.<
| > http://localhost:8086/bar/baz/foo.bar.html;<
| > news://localhost:8086/bar/baz/foo.bar.html:<
| > http://localhost:8086/bar/baz/foo.bar.html?<
| > http://localhost:8086/bar/baz/foo.bar.html,<
| > <http://localhost:8086/bar/baz/foo.bar.html><
| > <http://localhost:8086/bar/baz/foo.bar.html>,<
| > <http://localhost:8086/bar/baz/foo.bar.html>.<
| > <http://localhost:8086/bar/baz/foo.bar.html>;<
| > <http://localhost:8086/bar/baz/foo.bar.html>:<
| > <http://localhost:8086/bar/baz/foo.bar.html>?<
| > (http://localhost:8086/bar/baz/foo.bar.html)<
| > (http://localhost:8086/bar/baz/foo.bar.html),<
| > (http://localhost:8086/bar/baz/foo.bar.html).<
| > (http://localhost:8086/bar/baz/foo.bar.html);<
| > (http://localhost:8086/bar/baz/foo.bar.html):<
| > http://localhost/bar/baz/foo.bar.html?a=b&b=a\ <
| > http://localhost/bar/baz/foo.bar.html?a=b&b=a.<
| > http://localhost/bar/baz/foo.bar.html?a=b&b=a,<
| > http://localhost/bar/baz/foo.bar.html?a=b&b=a;<
| > http://localhost/bar/baz/foo.bar.html?a=b&b=a:<
| >
  `http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%f~g#h,j!k-l+m$n*o'p <http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%25f~g#h,j!k-l+m$n*o'p>`__\ <
| > http://www.searchtools.com/test/urls/(parens).html\ <
| > http://www.searchtools.com/test/urls/-dash.html\ <
| > http://www.searchtools.com/test/urls/_underscore.html\ <
| > http://www.searchtools.com/test/urls/period.x.html\ <
| > http://www.searchtools.com/test/urls/!exclamation.html\ <
| > http://www.searchtools.com/test/urls/~tilde.html\ <
| > http://www.searchtools.com/test/urls/*asterisk.html\ <
| > irc://chat.freenode.net/launchpad\ <
| > irc://chat.freenode.net/%23launchpad,isserver\ <
| > `mailto:noreply@launchpad.net <mailto:noreply@launchpad.net>`__\ <
| > jabber:noreply@launchpad.net\ <
| > http://localhost/foo?xxx&\ <
| > http://localhost?testing=%5Bsquare-brackets-in-query]<
| >

Others
------

\`"\` Removal
-------------

If the entire comment is encapsulated in \`"\` like this:

::

   "Content"

Launchpad will remove the \`"\`

::

   Content