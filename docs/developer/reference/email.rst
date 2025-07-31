Launchpad and email
===================

Quicker interactive testing
---------------------------

There is a script ``process-one-mail.py`` which reads a single mail
message from a file (or stdin), processes it as if it had been received by
Launchpad, and then prints out any mail generated in response.  For
quasi-interactive testing of email processing this may be your best bet.

Quickstart
----------

Otherwise, you can configure Launchpad with an incoming mailbox and an
outgoing mailer, in a way somewhat similar to what is used in production.
This lets you catch mail sent other than in response to an incoming
message.

Create the file override-includes/+mail-configure.zcml with contents
similar to the following::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:mail="http://namespaces.zope.org/mail"
        i18n_domain="zope">

        <!-- delete the username and password attributes if you don't use
            SMTP auth -->
        <mail:smtpMailer
            name="smtp"
            hostname="localhost"
            port="25"
            username="user"
            password="pass"
            />

        <mail:stubMailer
            name="stub"
            from_addr="stuart@stuartbishop.net"
            to_addr="stuart@stuartbishop.net"
            mailer="smtp"
            rewrite="false"
            />

        <mail:testMailer name="test-mailer" />

        <mail:mboxMailer
            name="mbox"
            filename="/tmp/launchpad.mbox"
            overwrite="true"
            mailer="test-mailer"
            />

    <!--

        Uncomment me if you want to get copies of emails in your normal inbox,
        via the stubMailer above.  However, tests will fail because they
        depend on using a directDelivery mailer.  See below.

        <mail:queuedDelivery
            mailer="stub"
            permission="zope.SendMail"
            queuePath="/var/tmp/launchpad_mailqueue" />

    -->
    <!--

        Uncomment me if you want to get test emails in a Unix mbox file, via
        the mboxMailer above.

        <mail:directDelivery
            mailer="mbox"
            permission="zope.SendMail"
            />
    -->

    </configure>


Options
-------

Zope3 provides two defined mailers out of the box (`smtp` and `sendmail`) so
most people won't actually need the `mail:smtpMailer` tag because the defaults
will usually just work.  However, several additional mailers are available for
you to use, depending on what you're trying to do.

The `mail:stubMailer` can be used to forward all emails to your normal inbox
via some other mailer.  Think of it as a proxy mailer that can be used to
specify explicit MAIL FROM and RCTP TO envelope addresses.  The `rewrite`
attribute of the `mail:stubMailer` specifies whether the RFC 2822 headers
should also be rewritten.  You and your spam filters might prefer this set to
`true`.

The `mail:mboxMailer` stores messages in a Unix mbox file and then forwards
the message on to another mailer.  You can use this if you want a record on
disk of all the messages sent, or if you'd rather not clutter up your inbox
with all your Launchpad test email.  The `overwrite` attribute says whether to
truncate the mbox file when Launchpad starts up (i.e. opens the file once in
'w' mode before appending all new messages to the file).

The `mail:testMailer` is necessary for the Launchpad tests to work.  You must
use a `mail:directDelivery` mailer for the tests, otherwise you'll get lots of
failures.  Basically, the testMailer stores the messages in a list in memory.

For both `mail:mboxMailer` and `mail:stubMailer` the `mailer` attribute
specifies the next mailer in the chain that the message will get sent to.
Thus if `mailer` is set to `smtp`, you'll get the messages in your inbox, but
if it's `test-mailer`, the unit tests will work.

Finally, these are all hooked up at the top with either a
`mail:queuedDelivery` section or a `mail:directDelivery` tag.  You must
use a `mail:directDelivery` tag if you want the unit tests to work because
otherwise, the in-memory list of the `mail:testMailer` won't be updated by the
time the unit test checks it.

If you just want the unit tests to work normally, don't include a
`mail:queuedDelivery` or a `mail:directDelivery` section at all.  Launchpad
will DTRT internally.  However, if you want copies in an mbox file or in your
inbox, set the `mailer` attribute to the appropriate mailer, chaining that to
a `mail:testMailer` for the unit tests or a `mail:smtpMailer` for
development.


API
---

Launchpad code should use the methods defined in lp.services.mail.sendmail
to send emails (`simple_sendmail`, `sendmail` or possibly `raw_sendmail`)


Functional Tests
----------------

The functional test harness is configured to allow easy testing of emails.
See `lp/services/mail/tests/test_stub.py` for example code.


Details
-------

To send email from Zope3, you use an `IMailDelivery` Utility, which
defines a single `send` method. There are two standard `IMailDelivery`
implementations:

    1. `QueuedDelivery` -- email is delivered in a separate thread. We use
       this for production.

    2. `DirectDelivery` -- email is send synchronously during transaction
       commit.  We use this for tests.

Both implementations will send no email if the transaction is aborted.  Both
implementations use events to notify anything that cares to subscribe if
delivery succeeded or failed.  Both implementations look up an `IMailer`
utility by name to do the actual delivery, as specified in the `mailer`
attribute of the `queuedDelivery` and `directDelivery` ZCML tags.

Zope3 provides two `IMailer` implementations out of the box:

    1. `SMTPMailer` -- sends email using SMTP

    2. `SendmailMailer1 -- Uses the `sendmail` program to send email.

In addition to these two, there are three more `IMailer` implementations
for use with Launchpad development (production instances will just use
`SMTPMailer` or `SendmailMailer`):

    3. `StubMailer` -- rewrites the envelope headers and optionally the RFC
       2822 To and From headers before handing on to a different `IMailer`.

    4. `TestMailer` -- stores the email in memory in a Python list object
       called `lp.services.mail.stub.test_email` for easy access by unit
       tests.

    5. `MboxMailer` -- stores the email in a Unix mbox file before optionally
       handing the message off to another `IMailer`.

Developers (and production server, until we are confident
messaging is working fine) should use the StubMailer, like in the quickstart
example.  This causes all emails to be redirected to the specified destination
address to you can test to your hearts content without spamming other
developers or innocent civilians.  Or you can use the MboxMailer.

The functional test suite is already configured to use the TestMailer.
However, if you use a StubMailer or MboxMailer and want the test suite to
work, you must hook it up to a TestMailer explicitly.  See
`lp/services/mail/tests/test_stub.py` for an example showing how functional
tests can check that notifications are being sent correctly.
