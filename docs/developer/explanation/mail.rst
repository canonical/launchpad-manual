Launchpad Mail
==============

.. include:: ../../includes/important_not_revised.rst

There are various kinds of emails in Launchpad:

1. Emails sent from one user to another (that is, an email sent "by"
   Launchpad, but really sent by user Alice when Alice uses the
   ``https://launchpad.net/~barry/+contactuser`` form to contact
   user Barry.
2. Emails sent by Launchpad itself, such as emails sent to subscribers
   when a bug is changed.
3. Emails received by Launchpad itself, such as emails sent by users to
   manipulate the bug tracker.

We should document all these kinds of email here, but right now this
page is really in draft state, so it's just a grab bag of various
information. We'll continue to improve it; please :ref:`help <get-help>` us if
you can.

Configuring Mail
----------------

Outgoing mail is configured using configs, so you'll need a config that
puts outgoing mail somewhere you can see it. Like so:

**WARNING: this configuration info may be outdated; it's taken from
documentation that was last modified in Sep 2008:**

::

      <configure
          xmlns="http://namespaces.zope.org/zope"
          xmlns:mail="http://namespaces.zope.org/mail"
          i18n_domain="zope">
      
          <mail:smtpMailer
              name="smtp"
              hostname="mail.wooz.org"
              port="25"
              />
      
          <mail:stubMailer
              name="barry"
              from_addr="barry@wooz.org"
              to_addr="barry@wooz.org"
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
      
          <mail:queuedDelivery permission="zope.SendMail"
              queuePath="/var/tmp/launchpad_mailqueue" mailer="barry" />
      
      -->
      
          <mail:directDelivery
              mailer="mbox"
              permission="zope.SendMail"
              />
      
      </configure>

You can then specify the config to make:

::

      make LPCONFIG=+abentley run_all
