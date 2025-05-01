#######################
Application integration
#######################

Third-party developers have written applications like Ground Control
that let you use Launchpad from the desktop, rather than through a web
browser. You can also use the \`launchpadlib\` library to write your own
scripts that automate common tasks.

To use these scripts and desktop applications, you'll need to grant them
access to your Launchpad account. This page explains exactly what
happens when a third-party application (or your own script) tries to
access Launchpad on your behalf. It tells you what your options are, and
how you can revoke access if something goes wrong.

Desktop integration (Natty Narwhal and later)
=============================================

The very first time you use an application that needs access to your
Launchpad account, your browser will open to a Launchpad page called
"Confirm Computer Access". If the application is running in a terminal
window, you'll also see some text like this printed to the terminal
window:

::

    The authorization page:
     (https://launchpad.net/...)
    should be opening in your browser. Use your browser to authorize
    this program to access Launchpad on your behalf. 

    Waiting to hear from Launchpad about your decision...

If you're not already logged in to Launchpad, you'll need to log in
through the Launchpad Login Service before you see the "Confirm Computer
Access" screen. If you've never used Launchpad before, you'll have to
*create* a Launchpad account--obviously the application can't use your
Launchpad account if you don't have one.

The authorization screen
------------------------

The screen called "Confirm Computer Access" will explain that you're not
just integrating a single application with your Launchpad
account--you're integrating your entire desktop. You have three options:

-  Permanently integrate this desktop with your Launchpad account.
-  Temporarily integrate this desktop with your Launchpad account (for
   an hour, a day, or a week)
-  Refuse to integrate this desktop with your Launchpad account.

A temporary integration is useful if you're using someone else's
computer or if you just want to try out desktop integration.

After you grant access
----------------------

Once you grant access, the application or script you were using should
automatically detect that it now has access to your Launchpad account,
and you should be able to continue using the application.

Since you've integrated your entire desktop into your Launchpad, you
should never see the "Confirm Computer Access" screen again on this
computer. The exception is if you chose a temporary integration: you'll
see this screen again once your temporary integration expires, and have
to get a new token. You'll also see this screen again if you use the
Launchpad website to manually revoke your desktop integration token.

Getting the GNOME keyring to work over X forwarding
---------------------------------------------------

If you SSH into another computer and try to run an application that uses
the launchpad web service, you may get an IOError because the
application can't communicate with the GNOME keyring.

::

   Traceback (most recent call last):
     ...
     File "/usr/lib/python2.7/dist-packages/keyring/backend.py", line 139, in get_password
       items = gnomekeyring.find_network_password_sync(username, service)
   gnomekeyring.IOError
      

This is because your SSH session doesn't have access to the dbus used
for inter-process communication. You can work around it by adding this
to your .bashrc:

::

   if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
       export `dbus-launch`
   fi
      

Put that in your .bashrc, and you should be able to use applications
that feature Launchpad integration over an X forwarded session.

Website integration
===================

The process is slightly different if you're integrating your Launchpad
account with *some other website*.

Let's say you go to some other website and click a button that will
integrate your Launchpad account with the offerings of that other site.
Since your browser is already open, the website will simply redirect you
to Launchpad. You'll log in to Launchpad and see a screen called
"Integrating [website name] into your Launchpad account."

With desktop-wide integration, you choose how long your integration
should last. With website integration, you choose how much access you
want to grant. For instance, you may trust a third-party website to
access public data but not private data, or you may trust it to read
your data but not to change it. Every website is different. You may have
up to five choices:

-  No access
-  Read Non-Private Data
-  Change Non-Private Data
-  Read Anything
-  Change Anything

A website may restrict which access levels you can choose, since it may
need a minimum level of access to do its job, but you'll always have the
option to deny access altogether.

After you grant access
----------------------

Once you integrate a website into your Launchpad account, you shouldn't
see this screen again *for that website*. Of course, you may see it
while using a *different* website that wants access to your Launchpad
account.

Desktop integration before Natty Narwhal (pre-launchpadlib 1.8.0)
=================================================================

If you're using an older release of Ubuntu, you'll have to authorize
your desktop applications one at a time. The system used is the same one
currently used for website integration: your browser will open to a
screen called "Integrating [application name] into your Launchpad
account." You'll be asked what level of access you want to grant the
application. You won't have the option to grant access for a limited
time.

You'll see this screen once for *every* desktop application and script
you integrate into Launchpad. To avoid this inconvenience, you'll need
to upgrade your Ubuntu installation to Natty, or upgrade your copy of
launchpadlib to 1.8.0 or above. Then you can integrate your entire
desktop at once.

If you're using an old version of launchpadlib, after you see the
message in your terminal window beginning "The authorization page:",
you'll see an extra line asking you to authorize the integration, then
tab back to that terminal window and hit Enter. In newer versions of
launchpadlib, you don't have to do this--launchpadlib automatically
detects when you've authorized the integration.

If your credential is compromised
=================================

If you give some computer access to your Launchpad account, and the
computer is stolen, then you should (among other things) revoke that
computer's Launchpad authorization. You can do that from the Launchpad
website: visit `your list of authorized
applications <https://launchpad.net/people/+me/+oauth-tokens>`__, find
the "System-wide" authorization for the computer that was stolen, and
click the "Revoke authorization" button underneath it.

Of course, "your computer gets stolen" is just one extreme way a
Launchpad integration credential might be compromised. Instead of
stealing your computer, someone may come up to your computer while
you're away, and dump the contents of your GNOME Keyring or KDE Wallet.
You might integrate a third-party website into your Launchpad account,
only to find that website acquired by a company you don't trust. Or you
might accidentally choose to permanently integrate your Launchpad
account into someone else's computer while using it.

However it happens: if you ever need to stop a computer, application, or
website from using your Launchpad account, you can revoke its
authorization from `your list of authorized
applications <https://launchpad.net/people/+me/+oauth-tokens>`__.
