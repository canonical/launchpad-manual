.. meta::
   :description: Understand how Mobot, Launchpad's merge overview bot, scans
      merge proposals, where your code and API key go, and who pays for scans.

.. _merge-proposal-overview-bot:

How Launchpad's merge overview bot works
========================================

`Mobot (merge overview bot) <https://ai-bot.edge.launchpad.net/>`_ is an
AI-powered bot that scans merge proposals on Launchpad and leaves comments
giving an overview of what the proposal is about and what it changes. When
asked to, it reads the diff, sends it to an AI model of your choice, and posts
the result back as both general and inline comments.

Mobot gives an overview to help human reviewers - it does not replace them.
It never votes on a merge proposal, and approving the changes remains a
decision for the human reviewers.

This page explains how a scan works, where your code and credentials go, and
what limits apply. See this how-to guide to
:ref:`set up Mobot and request a scan <merge-proposal-overview-with-mobot>`.

How a scan works
----------------

Mobot is made up of a web app, where you sign in and manage your settings, and
a worker that runs scans in the background. The two are connected through
`Temporal <https://temporal.io/>`_, a service that queues and tracks
long-running jobs.

When you post ``@mobot scan`` as a comment on a merge proposal:

1. Launchpad sends a webhook event to the Mobot web app. Mobot created this
   webhook when you `added the repository <https://ai-bot.edge.launchpad.net/repositories>`_.
2. The web app reads the comments on the merge proposal to find the new
   command and who posted it. It then queues a scan in Temporal. The scan
   contains only references, such as the comment, the merge proposal, and your
   OpenRouter connection and model; it does not contain the diff or your API
   key.
3. The Mobot worker picks up the scan and posts a comment on the merge
   proposal with a link to a status page where you can follow its progress.
4. The worker fetches the diff and details of the merge proposal from
   Launchpad.
5. The worker reads your OpenRouter API key from Vault, a secure credential
   store.
6. The worker sends the diff and instructions to your chosen model through
   OpenRouter, and receives the overview.
7. The worker posts the overview to the merge proposal as a new comment, with
   inline comments where relevant.

Mobot only acts on a command that sits on its own line in a comment. It
ignores commands inside quotes or code blocks, and comments that contain more
than one command.

Bring your own key
------------------

Mobot does not have its own AI budget. Each scan runs on the
`OpenRouter <https://openrouter.ai/>`_ account and model of the person who
posted the ``@mobot scan`` command. This means:

- You pay for the scans you request, regardless of who owns the repository or
  who proposed the changes.
- If two people request a scan on the same merge proposal, each scan uses the
  requester's own account and model.
- If you have not connected OpenRouter or chosen a model, Mobot replies with a
  link to its settings page instead of running the scan. It never falls back
  to another account or model.

You connect OpenRouter by signing in to OpenRouter and authorizing Mobot to
create an API key. You never paste a key into Mobot. The key Mobot receives
can only be used to run models; it cannot manage your OpenRouter account,
other keys, or guardrails.

Choosing a model
----------------

Mobot only lists models that your key can use and that support structured
output, which Mobot needs to place comments on the right lines. Restrictions
set on your OpenRouter account or organization also apply, so the list may be
shorter than OpenRouter's full catalog.

Your chosen model is recorded with each scan when it is queued, so changing your
model only affects future scans. If your model becomes unavailable, Mobot
stops the scan and asks you to choose another one rather than switching models
for you.

Where your data goes
--------------------

To scan a merge proposal, Mobot sends the following to OpenRouter, which
passes it to the provider of the model you chose:

- The diff of the merge proposal
- The merge proposal's URL and its commit message (or its description if there
  is no commit message
- The names of the source and target branches
- The display name of the merge proposal's author

The model provider's data handling policies apply to this content. You can
review and restrict which providers OpenRouter uses in your OpenRouter
settings. Consider this before scanning merge proposals that contain private
or sensitive code.

Your API key is kept in Vault. It is never stored in Mobot's database, passed
through Temporal, written to logs, or shown in comments. The diff is fetched
from Launchpad when a scan runs and is not stored in Mobot's database or in
Temporal.

Limits
------

Keep the following limits in mind when you request a scan:

- **Large diffs**: Mobot sends at most the first 50,000 characters of a diff to
  the model. On a larger diff, the model does not see later changes.
- **Command age**: Mobot only runs a command if it sees it within 15 minutes
  of it being posted. Older commands get a reply asking you to post a new one.
- **Changed diffs**: If the merge proposal's diff changes while a scan runs,
  Mobot still posts the summary but drops the inline comments, as they may no
  longer point to the correct lines.
- **Model responses**: If the model returns a response in the wrong format,
  Mobot retries once, then stops the scan.
- **Status pages**: The link to a scan's status page expires after 30 days.
  The scan remains listed under :guilabel:`My runs` on Mobot's site. Anyone who
  can see the comment on the merge proposal can open the status page while the
  link is valid.

Controlling costs
-----------------

Because scans run on your account, it's worth limiting what they can spend:

- Use a dedicated OpenRouter key for Mobot with a finite spend limit. Mobot
  shows a warning on its settings page if your key has no limit.
- The credit details on Mobot's settings page are recorded when the key was
  last checked; they are not a live balance. Check your current usage on
  OpenRouter.
- Disconnecting OpenRouter in Mobot deletes the key from Mobot, but does not
  revoke it on OpenRouter. To revoke it, delete the key in your
  `OpenRouter key settings <https://openrouter.ai/settings/keys>`_.

Controlling which repositories Mobot scans
------------------------------------------

Mobot only scans merge proposals in repositories that have its webhook. To add
a repository, you need edit rights on it. To stop Mobot scanning a repository,
delete its webhook from the repository's Webhooks page on Launchpad. A Mobot
administrator can also turn off scanning for a repository.
