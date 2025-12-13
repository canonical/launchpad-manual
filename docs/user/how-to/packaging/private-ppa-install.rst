Install software from private PPAs
==================================

.. include:: /includes/important_not_revised_help.rst

.. WARNING::
    THIS IS A DRAFT RELATING TO FUNCTIONALITY NOT YET AVAILABLE IN
    LAUNCHPAD

There are two types of Personal Package Archive: public PPAs and private
PPAs. Private PPAs are great for people who want to control who can
install their software.

To access a Private PPA, you'll need to contact its owner and ask for a
subscription. It's up to the Private PPA's owner how they decide to
grant access; for example, they may choose to charge a subscription fee.

:ref:`Contact us <get-help>` to find out how to get your own Private PPA.

Activate your subscription
--------------------------

Subscribing to a private PPA is a two-step process:

1. The Private PPA's owner offers you a subscription in Launchpad.
2. You either accept or reject the subscription.

You can see whether you have any outstanding subscription offers on your
`archive
subscriptions <https://launchpad.net/people/+me/+archivesubscriptions>`__
page.

Once you've accepted the offer, Launchpad will generate a unique
password that gives you access to the archive.

Get ready to install software from the Private PPA
--------------------------------------------------

Adding a Private PPA to your Ubuntu system is simple. Again, there are
two steps:

1. Add the Private PPA to the list of archives your Ubuntu computer can
   access.
2. Add the archive's security key to your computer so that Ubuntu can
   verify the authenticity of any software you download.

Add the Private PPA to Ubuntu
------------------------------

Ubuntu uses the Debian system of software archives, also called
repositories. Private PPAs are just like any other Debian-style software
archive, except that each subscriber has their own unique password.

Once you've accepted a subscription to a Private PPA Launchpad will show
exactly what information you need to give Ubuntu in order to install
software from that archive.

First up, let's take a look at your `archive
subscriptions <https://launchpad.net/people/+me/+archivesubscriptions>`__
page. Click *View* on the archive you want to access.

If you're familiar with adding repositories to your Ubuntu's
sources.list file, you'll see all the information you need there. Don't
worry if you're not: it's easy and takes just a couple of minutes.

**Step 1:** On the overview page for your Private PPA subcription is a
box with three lines of text. Highlight the second line (beginning
``deb``) and copy it to your clipboard.

**Step 2:** In Ubuntu's ``System->Administration`` menu click ``Software
Sources``. Enter your Ubuntu password when prompted.

**Step 3:** Click the ``Third Party Sources`` tab and then the ``Add``
button.

**Step 4:** Paste the line you copied from your subscription overview
page and click ``Add Source``

**Step 5:** Return to your subscription overview page, copy the third
line in the box (beginning ``deb-src``) and add it in the ``Third Party
Sources`` tab just as you did in step 4.

Leave the ``Software Sources`` application open because shortly we'll use
it to add the Private PPA's security key to your Ubuntu system.

Add the Private PPA's security key to Ubuntu
--------------------------------------------

Launchpad Personal Package Archives -- whether private or public -- each
have a unique security key, which Launchpad uses to sign the software
packages in the archive. Your Ubuntu system can use that signature to
check the authenticity of the packages.

Back on the overview page for your subscription to the Private PPA is a
link to the key, which reads something like:

::

   This repository is signed with 1024D/2AEF6A7D OpenPGP key.

Click the key ID -- ``1024D/2AEF6A7D``. You'll see a listing showing you
the details of that key: again, click the key ID.

Copy the public key, i.e. the portion starting:

::

   -----BEGIN PGP PUBLIC KEY BLOCK-----
   Version: SKS 1.0.10

   mI0ESXS1/wEEALis4to4JdgrkdRunmSTfB2tYRq99Cdcgdh9up4HzAf1yTZU1EtmETPP1Uy2
   vnAFf/cCunL5VRywNJB3QOxiHdvNlijbdsa0H/fT/ulq+A4iDljUEfsaJug+dAB5uEJE0BzZ
   agRjgLbFvRYtsKf3BwZizbo4XtWSAm3JSjZCGZKTABEBAAG0IkxhdW5jaHBhZCBQUEEgZm9y
   IEF3biBUZXN0aW5nIFRlYW2IRgQQEQIABgUCSXqnWgAKCRBBf7ZCSCH+JPZMAJ4xW7gbpuA+
   yedehvDQWdJHHUgseQCgy6NOmAyXqRKrIXWERkXw6h9TsRuItgQTAQIAIAUCSXS1/wIbAwYL
   CQgHAwIEFQIIAwQWAgMBAh4BAheAAAoJEH0seiO/gQzVpSID/0FXxTSLtxPHrT7IE9eif5qJ
   vjOjzcmOCXe9/3G0ctV8IfYHx0VynddjxgTqJ9WuEjMLVHRgXvK1Rw1XMlik+MeyyHrr9EWQ
   DUFbUs+Yc2usRyZY8pVe2Uwy2x7lFsi6VBfo0k9jVsu1l1qBU9BhANJDUTHjR15aPYiUJiZa
   13CZ
   =a6Gh
   -----END PGP PUBLIC KEY BLOCK-----

Now paste the public key into a text editor and save it.

Open ``System->Administration->Software Sources`` and click the
``Authentication`` tab.

Click ``Import Key File``, select the key you saved earlier and you're
done!