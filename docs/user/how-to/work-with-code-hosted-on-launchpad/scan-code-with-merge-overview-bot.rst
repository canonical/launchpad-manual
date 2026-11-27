.. meta::
   :description: Use Launchpad's Mobot to get an AI-powered scan of your
      code changes before merging.

.. _merge-proposal-overview-with-mobot:

Get overview of merge proposal using Mobot
==========================================

Mobot (merge overview bot) is an AI-powered bot that scans merge proposals to a
Launchpad repository and returns an overview of what the changes are about. The
bot also leaves inline comments to help you asses design and coding decisions
in your changes.

There are four main steps to using Mobot; sign in to Launchpad, connect Mobot
to OpenRouter, add a repository, and request a scan of a merge proposal.

Prerequisites
-------------
Before using Mobot, you'll need:

- An active Launchpad account
- An `OpenRouter account <https://openrouter.ai/>`_
- A repository for which you hold edit rights

Initial setup
-------------
Visit `Mobot's homepage <https://ai-bot.edge.launchpad.net>`_.

If you were previously signed in to Launchpad, there will be a green checkmark
next to the :guilabel:`Sign in with Launchpad` step.
If not, sign in to Launchpad first the navigate back to Mobot's homepage.

Next, go to :guilabel:`Settings` and select :guilabel:`Connect OpenRouter`.
Sign in to your OpenRouter account, fill in the required API key details, and
authorize Mobot to create an API key.

You should see the new key on the settings page.
Select your preferred model and save it.
On the home page, there will be a green checkmark next to :guilabel:`Connect your AI provider`.

Scan a merge proposal
---------------------
To get an overview of a merge proposal, add the target repository in the
repositories section.
This will create a webhook in the target repository.
You can add as many repositories as you need.

Create a merge proposal against the target repository, then post ``@mobot scan``
as a comment on the merge proposal page.

You should see a comment from Mobot informing you that the scan has started
with a link to a page tracking its progress.
The link expires after 30 days.

Once the scan is done, Mobot will post a second comment with an overview of the
merge proposal and inline comments where necessary.

Troubleshooting
---------------
A scan can fail for various reasons. Here are some messages you may see and how
to troubleshoot them:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Message
     - What to do
   * - Connect an OpenRouter account to enable ``@mobot scan``.
     - Connect OpenRouter on the
       `Settings page <https://ai-bot.edge.launchpad.net/settings>`_, then
       post a new ``@mobot scan`` comment.
   * - Select an eligible default model to enable ``@mobot scan``.
     - Choose a model on the Settings page and save it.
   * - OpenRouter rejected this scan's key.
     - Select :guilabel:`Reconnect OpenRouter` on the Settings page.
   * - OpenRouter credits or the key's spend cap are exhausted.
     - Add credits or raise the key's limit on
       `OpenRouter <https://openrouter.ai/settings/keys>`_. The credit details
       on the Settings page are not live balances.
   * - OpenRouter declined this scan under its policy or guardrails.
     - Check your policy and guardrail settings on OpenRouter.
   * - This scan's model is no longer available to the key.
     - Choose another model on the Settings page.
   * - OpenRouter remained rate limited.
     - Wait a while before you request a new scan.
   * - Mobot did not run this command because it first saw it more than 15
       minutes after it was posted.
     - Post a new ``@mobot scan`` comment.
