Translations licensing
======================

We have now updated the "Translations copyright" section of the
`Launchpad terms of use <Legal>`__ to require that translations
submitted in Launchpad licensed using the `BSD
licence <#license-text>`__, but also that groups of strings from one
project which are a derivative work of the project are licensed under
the licence of the project.

Why was this needed?
--------------------

Translations are freely shared between projects on Launchpad. Copyright
complicates that free exchange. That's why our terms of use require
that, when you translate in Launchpad, you grant us the right to share
those translations with other projects. To the extent translations are
aggregated together such that the result is a derivative work of a
particular project, that derivative is licensed under the license of the
rest of the project.

Why the BSD license?
--------------------

The BSD license is universally compatible. This lets you share and
combine with projects under GPL, LGPL, BSD, and many other licenses.

Why not public domain like the FSF's Translation Project?
---------------------------------------------------------

For all practical purposes, BSD license is very much like
`disclaiming <http://translationproject.org/html/whydisclaim.html>`__
any copyrights, similar to what Translation Project does by asking for
disclaimers in writing. However, you still get to keep your copyright,
which is slightly easier to manage.

Does that mean my translations may be used in proprietary software?
-------------------------------------------------------------------

Yes, this risk exists. However, we believe that the advantage of having
large translation memories for free software far outweighs the risk of
having free software translations end up in proprietary software.

Keeping track of how each string is allowed to be used would be much
more difficult, and gain us relatively little.

If and when we allow proprietary projects to use Launchpad for
translation, they will get the same translation suggestions as anyone
else. Those may include translations you entered (and conversely, those
projects' translations may be included in the suggestions you receive as
well).

If I don't want my translations licensed under BSD, what will you do?
---------------------------------------------------------------------

If you don't want your contributions licensed under BSD, do not use
Launchpad for translating, although we'll be very sad to see you go.

Can I select a packaged translation from some other template?
-------------------------------------------------------------

Yes, however, it is up to you to check licensing compatibility. For
example, you should not reuse nontrivial translations from a GPL module
in a BSD-licensed project without asking the author for permission. An
icon warns of potential licensing issues.

You can freely reuse a few translations, though, because that's what
copyright laws allow. Also, accidental matches between translations for
short phrases should not make you worry.

I have no problem with BSD myself, but I also uploaded translations from upstream. What do I do?
------------------------------------------------------------------------------------------------

As long as the uploads were marked as translations that were published
elsewhere, they fall under a separate copyright regime: those imports
will retain their original copyright license. The BSD licence only
applies to translations that are (as far as the system knows) original
to Launchpad.

<<Anchor(license-text)>>

What is the exact text of the BSD license?
------------------------------------------

There are a few variants of the text available, but the differences are
minor and the variants should be legally equivalent:

::

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are
        met:

          * Redistributions of source code must retain the above copyright
            notice, this list of conditions and the following disclaimer.

          * Redistributions in binary form must reproduce the above
            copyright notice, this list of conditions and the following
            disclaimer in the documentation and/or other materials provided
            with the distribution.

          * Neither the name of the <ORGANIZATION> nor the names of its
            contributors may be used to endorse or promote products derived
            from this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
        "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
        LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
        A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
        HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
        SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
        LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
        DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
        THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

(In the third clause, "**the **" would be replaced with your name.)

Note that this is the modern, simplified BSD license, that is, without
the advertising clause (see `the full history of the
license <http://en.wikipedia.org/wiki/BSD_license>`__ for more
information). In modern times, this simplified, three-clause version is
the most widely used.