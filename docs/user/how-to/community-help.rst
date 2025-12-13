
.. _help-the-community:

Help the community
==================

.. include:: /includes/important_not_revised_help.rst


You can help other members of the free software community quickly and with
little effort by answering support questions in `Launchpad Answers <https://answers.launchpad.net>`_.

Anyone can answer any question in Launchpad. However, if you're keen to
help out on an on-going basis, you can make sure you stay up to date
with new questions by becoming an ``answer contact``.

Answer contacts
---------------

As an answer contact, you have two main jobs:

-  reviewing new questions
-  creating stock answers to frequently asked questions.

You or anyone else can volunteer to become an answer contact for a
project. All you have to do is click the ``Set answer contact`` link
on a project or distro's Answers overview page. If you're the admin of a
team, you can also set that team to be an answer contact.

.. note::

   When you become an answer contact, Launchpad will send you an email each 
   time someone asks a question about that project or distro. If you make one 
   of your teams an answer contact, you're subscribing each member to also 
   receive that email. You should gain each member's permission before you make
   the team an answer contact.

Volunteering to be an answer contact is the easy bit. While Launchpad
provides the mechanism to offer help to people, each project can choose
for themselves how they deal with user support queries.

To find out about any such conventions, you should get in touch with one
or two of the other answer contacts. Visit any of the project's Answers
pages and expand the answer contacts box, in the left-hand column, for a
full list.

Responding to new questions
---------------------------

Once you're an answer contact, Launchpad will email you each time
someone posts a new question to your chosen project or distribution.

You can also see a list of questions awaiting an answer by using the
``Open`` filter towards the top of the page.

Handling frequently asked questions
-----------------------------------

Every free software project has questions that crop up regularly.

If you're an answer contact for a project, you can create a library of
stock answers to the project's frequently asked questions.

Answering a question with an existing FAQ
-----------------------------------------

When you answer a question, you can choose to use an existing FAQ
answer. This saves you from typing an answer that has already been given
by one of the project's answer contacts.

-  Visit the open questions page for the project you're interested in. For 
   example: https://answers.launchpad.net/ubuntu
-  Click **Open** in the menu, then select a question from the list.
-  Click **This is a FAQ** in the menu.
-  Launchpad will search for any existing FAQ answers that appear to be relevant. 
   If you see a relevant answer, select the radio button beside. 
   Otherwise, you can enter your own search terms to look for other FAQ answers that 
   may be useful to the original questioner.

.. note::

   If you can't find a relevant answer, but think that the question should be
   considered an FAQ, skip to the next section *Creating a new FAQ*.

-  You can send a message to the questioner to explain why you're sending them 
   a link to an FAQ. Launchpad automatically enters a generic message in the 
   *Answer Message* text-box, which you can customise.
-  When you're ready to send the FAQ to the questioner, click the **Link FAQ** 
   button. A link to the FAQ and your message will then appear as an answer, 
   alongside any other answers, to the question.

Creating a new FAQ
------------------

*Continues from the fourth step in the section above.*

.. note::

   Although any user can answer a question with an existing
   FAQ answer, only answer contacts for the project can create a new FAQ answer.

-  If you can't find a suitable FAQ answer, 
   click **create a new FAQ** in the page's introductory text.
-  Specify relevant keywords to improve the chances of your FAQ being found in searches.
-  Enter the text of your FAQ answer. You should make sure that your answer is 
   accurate and complete, as it will be used as the canonical answer to this 
   problem. Alternatively, enter a simple explanation and a link to an external
   page where the reader can find more details (for example, if the complete 
   answer is contained in the project's wiki or documentation).
-  When you are happy with your answer text, optionally customise the *Answer Message*, 
   then click the **Create and Link** button to add your FAQ to Launchpad and 
   send it to the questioner.

Filtering email
---------------

As an answer contact, you'll receive quite a bit of email from
Launchpad. To help you deal with this email, Launchpad uses special
headers to help you filter incoming messages.

Rationale
---------

The ``X-Launchpad-Message-Rationale`` header appears in all email
that Launchpad sends you. This tells you why Launchpad sent you the
email, which is particularly useful if you want to find the quickest way
to stop that type of email.

::

   X-Launchpad-Message-Rationale: Answer Contact (Launchpad itself)

X-Launchpad-Question
--------------------

Emails from Launchpad Answers have the ``X-Launchpad-Question``
header, which is made up of:

-  ``Product``: the project that the question is about.
-  ``Status``: open, needs info, answered, solved, invalid or expired -
   more: :ref:`question-statuses`.
-  ``Assignee``: the person assigned to work on the question, if any.
-  ``Priority``: always set to normal.
-  ``Language``: the language the questioner chose when asking their
   question.

Here's an example:

::

   X-Launchpad-Question: product=launchpad; status=Open;
   assignee=None; priority=Normal; language=en

Next step
---------
Different projects favour different ways of planning future releases and
organising chunks of work. `Blueprint <https://launchpad.net/blueprint>`_ is Launchpad's
light-touch specification tracker that makes it easy to organise and
follow future work.

