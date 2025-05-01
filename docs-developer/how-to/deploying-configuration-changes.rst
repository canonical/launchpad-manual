=============================================
Deploying configuration changes to production
=============================================

While technically there is a procedure for doing a rollout that just
`updates the configuration <https://wiki.canonical.com/InformationInfrastructure/OSA/LaunchpadRollout#Config-only_Rollouts>`_,
it hasn't been used for some years, and it also requires manual intervention by
IS.

The recommended way to deploy configuration changes is to deploy a new code
revision, e.g. deploying Launchpad, which will always pull in the latest
configuration.
