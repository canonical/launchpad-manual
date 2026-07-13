.. meta::
   :description: Reference of Launchpad comment parsing syntax for
      linking bugs and branches using special markup in comments.

.. _launchpad-comment-parsing:

Launchpad comment parsing
=========================

Launchpad automatically parses and formats comment text, creating links
to bugs, branches, and other resources when you use specific syntax
patterns.

Whitespaces
-----------

Launchpad reduces any whitespace between non-whitespace characters to a
single space, keeps whitespace to the left, and removes whitespace to
the right.

.. note::
    Technically Launchpad passes whitespace through and the browser just
    ignores the whitespace.

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``This sentence has varying amounts of whitespace between
       its words.``
     - ``This sentence has varying amounts of whitespace between
       its words.``
   * - ::

          | Column 1   | Column 2 | Column 3    |
          |------------+----------+-------------|
          | Lorem      | ipsum    | dolor       |
          | sit        | amet     | consectetur |
          | adipiscing | elit     | sed         |

     - ::

          | Column 1 | Column 2 | Column 3 |
          |------------+----------+-------------|
          | Lorem | ipsum | dolor |
          | sit | amet | consectetur |
          | adipiscing | elit | sed |


Paragraphs
----------

Multiple newline characters will be reduced to one.

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ::

          Here are two paragraphs with lots of whitespace between them.




          But they're still just two paragraphs

     - ::

          Here are two paragraphs with lots of whitespace between them.

          But they're still just two paragraphs

Mention a single Launchpad bug
------------------------------

Use any of these patterns to link to a bug. These patterns are
case-insensitive.

Patterns::

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

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``bug 123``
     - `bug 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug    123``
     - `bug 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug #123``
     - `bug #123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug number 123``
     - `bug number 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug number. 123``
     - bug number. 123
   * - ``bug num 123``
     - `bug num 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug num. 123``
     - `bug num. 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug no 123``
     - `bug no 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug report 123``
     - `bug report 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug no. 123``
     - `bug no. 123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug#123``
     - bug#123
   * - ``bug-123``
     - `bug-123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug-report-123``
     - `bug-report-123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``bug=123``
     - `bug=123 <https://bugs.launchpad.net/bugs/123>`_
   * - ``debug #52``
     - debug #52

Mention multiple Launchpad bugs
-------------------------------

Use this pattern to link to multiple bugs. These patterns are
case-insensitive. The amount of whitespace can be variable, but
whitespace in other positions may prevent parsing.

Pattern::

   LP: #<LP-Bug-Number>[, #<LP-Bug-Number>]...

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``LP: #1``
     - LP: `#1 <http://example.net>`_
   * - ``(LP: #1)``
     - (LP: `#1 <http://example.net>`_
   * - ``LP: #1, #2.``
     - LP: `#1 <http://example.net>`_, `#2 <http://example.net>`_.
   * - ::

          LP:
          #1,
          #2,
          #3,
          #4

     - | LP:
       | `#1 <http://example.net>`_
       | `#2 <http://example.net>`_
       | `#3 <http://example.net>`_
       | `#4 <http://example.net>`_
   * - ``lp: #1``
     - lp: `#1 <http://example.net>`_
   * - ``(lp: #1)``
     - (lp: `#1 <http://example.net>`_
   * - ``lp: #1, #2.``
     - lp: `#1 <http://example.net>`_, `#2 <http://example.net>`_.
   * - ``LP #1``
     - LP #1
   * - ``LP: #1 , #2``
     - LP: `#1 <http://example.net>`__ , #2
   * - ::

          LP: #1, #2,

          #3

     - | LP: `#1 <http://example.net>`_, `#2 <http://example.net>`_,
       |
       | 1. 3

Mention a branch
----------------

Link to a Launchpad branch using the ``lp`` URI syntax. The ``lp:``
prefix will expand to ``https://bugs.launchpad.net/+code/``. These
patterns are case-insensitive.

Patterns::

   lp:<Relative-URL>
   lp:/<Relative-URL>
   lp:///<Relative-URL>

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``lp:~foo/bar/baz``
     - `lp:~foo/bar/baz <https://bugs.launchpad.net/+code/~foo/bar/baz>`_
   * - ``lp:~foo/bar/bug-123``
     - `lp:~foo/bar/bug-123
       <https://bugs.launchpad.net/+code/~foo/bar/bug-123>`_
   * - ``lp:~foo/+junk/baz``
     - `lp:~foo/+junk/baz
       <https://bugs.qastaging.launchpad.net/+code/~foo/+junk/baz>`_
   * - ``lp:~foo/ubuntu/jaunty/evolution/baz``
     - `lp:~foo/ubuntu/jaunty/evolution/baz
       <https://bugs.qastaging.launchpad.net/+code/~foo/ubuntu/jaunty/evolution/baz>`_
   * - ``lp:foo/bar``
     - `lp:foo/bar <https://bugs.qastaging.launchpad.net/+code/foo/bar>`_
   * - ``lp:foo``
     - `lp:foo <https://bugs.launchpad.net/+code/foo>`__
   * - ``lp:foo,``
     - `lp:foo <https://bugs.launchpad.net/+code/foo>`__,
   * - ``lp:foo/bar.``
     - `lp:foo/bar <https://bugs.launchpad.net/+code/foo/bar>`__.
   * - ``lp:foo/bar/baz``
     - `lp:foo/bar/baz <https://bugs.launchpad.net/+code/bar/baz>`_
   * - ``lp:///foo``
     - `lp:///foo <https://bugs.launchpad.net/+code/foo>`_
   * - ``lp:/foo``
     - `lp:///foo <https://bugs.launchpad.net/+code/foo>`_

Mention an FAQ thread
---------------------

Link to a Launchpad FAQ thread by mentioning its number. These patterns
are case-insensitive.

Patterns::

   faq <faq-number>
   faq #<faq-number>
   faq-<faq-number>
   faq=<faq-number>
   faq item <faq-number>
   faq number <faq-number>

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``faq 3041``
     - `faq 3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_
   * - ``faq #3041``
     - `faq #3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_
   * - ``faq-3041``
     - `faq-3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_
   * - ``faq=3041``
     - `faq=3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_
   * - ``faq item 3041``
     - `faq item 3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_
   * - ``faq  number  3041``
     - `faq number 3041 <https://answers.launchpad.net/ubuntu/+faq/3041>`_

URIs
----

Launchpad automatically recognizes and links ``http``, ``https``,
``ftp``, ``sftp``, ``mailto``, ``news``, ``irc``, and ``jabber`` URIs.

Not recognized: ``tel``, ``urn``, ``telnet``, ``ldap`` URIs, relative
URLs (e.g., ``example.com``), and plain email addresses (e.g.,
``test@example.com``).

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``http://localhost:8086/bar/baz/foo.html``
     - http://localhost:8086/bar/baz/foo.html
   * - ``ftp://localhost:8086/bar/baz/foo.bar.html``
     - ftp://localhost:8086/bar/baz/foo.bar.html
   * - ``sftp://localhost:8086/bar/baz/foo.bar.html.``
     - sftp://localhost:8086/bar/baz/foo.bar.html.
   * - ``http://localhost:8086/bar/baz/foo.bar.html;``
     - http://localhost:8086/bar/baz/foo.bar.html;
   * - ``news://localhost:8086/bar/baz/foo.bar.html:``
     - news://localhost:8086/bar/baz/foo.bar.html:
   * - ``http://localhost:8086/bar/baz/foo.bar.html?``
     - http://localhost:8086/bar/baz/foo.bar.html?
   * - ``http://localhost:8086/bar/baz/foo.bar.html,``
     - http://localhost:8086/bar/baz/foo.bar.html,
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>``
     - <http://localhost:8086/bar/baz/foo.bar.html>
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>,``
     - <http://localhost:8086/bar/baz/foo.bar.html>,
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>.``
     - <http://localhost:8086/bar/baz/foo.bar.html>.
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>;``
     - <http://localhost:8086/bar/baz/foo.bar.html>;
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>:``
     - <http://localhost:8086/bar/baz/foo.bar.html>:
   * - ``<http://localhost:8086/bar/baz/foo.bar.html>?``
     - <http://localhost:8086/bar/baz/foo.bar.html>?
   * - ``(http://localhost:8086/bar/baz/foo.bar.html)``
     - (http://localhost:8086/bar/baz/foo.bar.html)
   * - ``(http://localhost:8086/bar/baz/foo.bar.html),``
     - (http://localhost:8086/bar/baz/foo.bar.html),
   * - ``(http://localhost:8086/bar/baz/foo.bar.html).``
     - (http://localhost:8086/bar/baz/foo.bar.html).
   * - ``(http://localhost:8086/bar/baz/foo.bar.html);``
     - (http://localhost:8086/bar/baz/foo.bar.html);
   * - ``(http://localhost:8086/bar/baz/foo.bar.html):``
     - (http://localhost:8086/bar/baz/foo.bar.html):
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a``
     - http://localhost/bar/baz/foo.bar.html?a=b&b=a
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a.``
     - http://localhost/bar/baz/foo.bar.html?a=b&b=a.
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a,``
     - http://localhost/bar/baz/foo.bar.html?a=b&b=a,
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a;``
     - http://localhost/bar/baz/foo.bar.html?a=b&b=a;
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a:``
     - http://localhost/bar/baz/foo.bar.html?a=b&b=a:
   * - ``http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%f~g#h,j!k-l+m$n*o'p``
     - `http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%f~g#h,j!k-l+m$n*o'p
       <http://localhost/bar/baz/foo.bar.html?a=b&b=a:b;c@d_e%25f~g#h,j!k-l+m$n*o'p>`_
   * - ``http://www.searchtools.com/test/urls/(parens).html``
     - `<http://www.searchtools.com/test/urls/(parens).html>`_
   * - ``http://www.searchtools.com/test/urls/-dash.html``
     - http://www.searchtools.com/test/urls/-dash.html
   * - ``http://www.searchtools.com/test/urls/_underscore.html``
     - http://www.searchtools.com/test/urls/_underscore.html
   * - ``http://www.searchtools.com/test/urls/period.x.html``
     - http://www.searchtools.com/test/urls/period.x.html
   * - ``http://www.searchtools.com/test/urls/!exclamation.html``
     - `<http://www.searchtools.com/test/urls/!exclamation.html>`_
   * - ``http://www.searchtools.com/test/urls/~tilde.html``
     - `<http://www.searchtools.com/test/urls/~tilde.html>`_
   * - ``http://www.searchtools.com/test/urls/*asterisk.html``
     - `<http://www.searchtools.com/test/urls/*asterisk.html>`_
   * - ``irc://chat.freenode.net/launchpad``
     - irc://chat.freenode.net/launchpad
   * - ``irc://chat.freenode.net/%23launchpad,isserver``
     - irc://chat.freenode.net/%23launchpad,isserver
   * - ``mailto:noreply@launchpad.net``
     - `mailto:noreply@launchpad.net <mailto:noreply@launchpad.net>`_
   * - ``jabber:noreply@launchpad.net``
     - jabber:noreply@launchpad.net
   * - ``http://localhost/foo?xxx&``
     - `<http://localhost/foo?xxx&>`_
   * - ``http://localhost?testing=[square-brackets-in-query]``
     - `<http://localhost?testing=%5Bsquare-brackets-in-query]>`_

Quote removal
-------------

If a comment is entirely enclosed in double quotes (``"Content"``),
Launchpad will drop the quotes.

Examples
~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Input
     - Output
   * - ``"Content"``
     - Content
