.. meta::
   :description: Learn how to interact with Launchpad using launchpadlib, the
      library for accessing Launchpad's web services.

.. _launchpadlib-tutorial:

Get started with launchpadlib
==================================

``launchpadlib`` is a Python SDK that lets you interact with Launchpad directly 
from the command line, treating its HTTP resources like native Python objects.
In this tutorial, you'll learn how to install the library, explore and inspect 
Launchpad objects, and manage subscriptions—so you can easily turn 
notifications on or off as needed.

Prerequisites
-------------
- You have a Launchpad account. If you don't have one, you can create one at
  https://launchpad.net/+login.
- You have Python 3 installed on your system. You can check this by running
  ``python3 --version`` in your terminal.

Install launchpadlib
--------------------

#. Create and activate a new virtual environment, and install launchpadlib:

   .. code-block:: bash

        python3 -m venv launchpadlib-tutorial-env
        source launchpadlib-tutorial-env/bin/activate
        pip install 'launchpadlib[keyring]'

#. Open a new Python shell and set up your connection to Launchpad:

   .. code-block:: python

        from launchpadlib.launchpad import Launchpad
        lp = Launchpad.login_with('tutorial', 'production', version="devel")


Know your user
--------------

#. Access your user information:

   .. code-block:: python

        lp.me

   This is your user object. It contains all the information about you that 
   Launchpad has. Running this, you should see:

   .. code-block:: python
     
        <person at https://api.launchpad.net/devel/~your-username>

#. Access your user attributes. You can see your username and display name
   with:

   .. code-block:: python

        lp.me.name
        lp.me.display_name

   Explore other attributes:

   .. code-block:: python

        lp.me.lp_attributes

   This lists all the attributes of your user object. Example output:

   .. code-block::

        ['self_link', 'web_link', 'resource_type_link', 'http_etag', 'account_status', 'account_status_history', 'date_created', 'description', 'display_name', 'hide_email_addresses', 'homepage_content', 'id', 'is_probationary', 'is_team', 'is_ubuntu_coc_signer', 'is_valid', 'karma', 'mailing_list_auto_subscribe_policy', 'name', 'private', 'time_zone', 'visibility']

#. Update an attribute of your user object, for example, your user description:

   .. code-block:: python

        me = lp.me
        print(me.description)
        me.description = "On a mission to explore Launchpad API!"
        me.lp_save()
        print(me.description)

   The ``lp_save()`` method will update your object on Launchpad.


Explore the tutorial project
----------------------------

#. Load the tutorial project:

   .. code-block:: python

        project = lp.load("launchpadlib-tutorial")

#. List all questions within a project by using the
   ``searchQuestions()`` method on the project object:

   .. code-block:: python

        questions = project.searchQuestions(sort="oldest first")

   The result is a collection of question objects.

   You can iterate over the collection to access individual question attributes,
   such as the question ID and title:

   .. code-block:: python

        for question in questions:
           print(f"Question {question.id}: {question.title}")

#. Retrieve a specific question object using its ID:

   .. code-block:: python

        question = lp.questions.getByID(question_id=824116)
        question.title

   .. note::

        You can also directly access a specific question.

        .. code-block:: python

            question = questions[0]


Interact with project questions
-------------------------------

#. Subscribing to updates for a question means you'll receive notifications
   via email:

   .. code-block:: python

        question.subscribe(person=lp.me)

   ``subscribe`` is an operation. You can list all operations of an object by 
   using the ``lp_operations`` attribute, for example:

   .. code-block:: python

        question.lp_operations

   For questions, the following operations are available:

   .. code-block:: python

        ['reject', 'subscribe', 'unsubscribe', 'setCommentVisibility']

#. To view the question in the browser, you can get the link via the API:

   .. code-block:: python

        question.web_link

#. While in the browser, you can post a comment to the question. This will
   trigger an email notification.

#. List all the comments in a question, and access the latest comment:

   .. code-block:: python

        comments = question.messages
        print(f"There are {comments.total_size} comments in this question.")
        print(list(comments))
        latest_comment = comments[comments.total_size-1]
        print(f"Comment by {latest_comment.owner.name}: {latest_comment.content}")

   The ``question.messages`` is a collection that contains all comments
   referring to that question. You can list all collections of an object by
   using the ``lp_collections`` attribute, for example:

   .. code-block:: python

        question.lp_collections

   For questions specifically, there is only one collection accessible:

   .. code-block:: python

        ['messages']

#. Check who asked the question and where the question was asked:
   
   .. code-block:: python
   
        print(f"Asked by {question.owner.name} ({question.owner.web_link})")
        print(f"Asked in {question.target.name} ({question.target.web_link})")

   ``question.owner`` and ``question.target`` are both entries of
   a question - they refer to other objects related to the question.
   
   You can list all entries of an object by using the ``lp_entries``
   attribute:

   .. code-block:: python

        question.lp_entries
        
   For questions, you should see the following entries:
   
   .. code-block:: python
   
        ['answer', 'answerer', 'assignee', 'language', 'owner', 'target']

#. Unsubscribe from the question so that you don't receive any more email
   notifications.

   .. code-block:: python

        question.unsubscribe(person=lp.me)


API reference
-------------

This tutorial only shows a small subset of Launchpad's API endpoints.

You can find the full API reference at https://api.launchpad.net/devel.html.

Further information
-------------------

You can get more information about this topic in :ref:`work-with-launchpadlib`.

This tutorial uses Python.
SDKs for the Launchpad API are also available in Golang and Rust.

- `Golang SDK <https://github.com/canonical/lpad>`_
- `Rust SDK <https://docs.rs/launchpadlib/latest/launchpadlib/>`_ (not maintained by Canonical)
