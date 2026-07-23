.. meta::
   :description: Install software from a private PPA.

Install software from private PPAs
==================================

There are two types of Personal Package Archives: public PPAs and private
PPAs. Anyone can install software from a public PPA, but you can only install
software from a Private PPA with the owner's permission.

To access a Private PPA, you'll need to contact its owner and ask for a
subscription. It's up to the Private PPA's owner to decide the criteria used
to grant access.

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

Add a private PPA to your sources list
--------------------------------------

Ubuntu uses the Debian system of software archives, also called
repositories. Private PPAs are like any other Debian-style software
archive, except that each subscriber has their own unique password.

.. tab-set::

    .. tab-item:: Ubuntu > 18.04

        #. Check your subscriptions in the `archive subscriptions
           <https://launchpad.net/people/+me/+archivesubscriptions>`__
           page and get the name of the archive you want to add. It should be
           something like ``ppa:user/ppa-name``.
        #. Run the ``add-apt-repository`` using the ``--login`` flag and update
           the package list.

        ::

           sudo add-apt-repository --login ppa:user/ppa-name
           sudo apt update

    .. tab-item:: Older Ubuntu versions

        Check your `archive subscriptions
        <https://launchpad.net/people/+me/+archivesubscriptions>`__ page. Click
        *View* on the archive you want to access.

        If you're familiar with adding repositories to your Ubuntu's
        sources.list file, you'll see all the information you need there. Don't
        worry if you're not: it's easy and takes just a couple of minutes.

        #. On the overview page for your Private PPA subscription is a
           box with three lines of text. Highlight the second line (beginning
           ``deb``) and copy it to your clipboard.

        #. In Ubuntu's ``System->Administration`` menu click ``Software
           Sources``. Enter your Ubuntu password when prompted.

        #. Click the ``Third Party Sources`` tab and then the ``Add``
           button.

        #. Paste the line you copied from your subscription overview
           page and click ``Add Source``

        #. Return to your subscription overview page, copy the third
           line in the box (beginning ``deb-src``) and add it in the ``Third Party
           Sources`` tab just as you did in step 4.

        **Add the private PPA's security key to Ubuntu**

        Launchpad Personal Package Archives -- whether private or public -- each
        have a unique security key, which Launchpad uses to sign the software
        packages in the archive. Your Ubuntu system can use that signature t4
        check the authenticity of the packages.

        ::

           This repository is signed with 1024D/2AEF6A7D OpenPGP key.

        1. Click the key ID -- ``1024D/2AEF6A7D``. You'll see a listing showing you
           the details of that key: again, click the key ID.
        2. Copy the public key and save it into a file, i.e. the portion starting:

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

        3. Open ``System->Administration->Software Sources`` and click the
           ``Authentication`` tab.
        4. Click ``Import Key File``, select the key you saved earlier and you're
           done!

