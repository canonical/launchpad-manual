##############################
 Building charms in Launchpad
##############################

Launchpad supports building charms using `Charmcraft
<https://documentation.ubuntu.com/juju/3.6/howto/manage-charms/#build-a-charm>`_.
for all architectures supported by Ubuntu, and pushing the resulting builds to
Charmhub. As of October 2021, this feature is in beta testing, open to all
Canonical employees.

******************************
 Setting up builds of a charm
******************************

If you haven't done so already, `register your charm's name with Charmhub
<https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/manage-charms/#publish-a-charm-on-charmhub>`_
using ``charmcraft login`` and ``charmcraft register``.

Make sure that your charm has a suitable ``charmcraft.yaml``. A minimal example
looks something like this:

.. code:: python

   type: charm
   bases:
   - name: "ubuntu"
     channel: "20.04"

See the `Charmcraft documentation
<https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/manage-charmcraft/>`_
for more details. You can test your charm build locally using charmcraft pack.
The only part of charmcraft.yaml that Launchpad itself pays attention to (as
opposed to letting Charmcraft take care of things) is the bases section:
Launchpad dispatches a build for each build-on entry there that Launchpad
supports, where name should be "ubuntu", channel identifies an Ubuntu series by
version, and architectures is a list of Ubuntu architecture names. If you don't
specify any architectures, then Launchpad will build on all architectures that
the requested series supports.

Push your charm's code to a Git repository on Launchpad; we recommend putting
each charm in its own `project <https://launchpad.net/projects/+new>`_,
conventionally starting with "charm-". If your charm's code is already on
another site such as GitHub, then you can also ask Launchpad to maintain a
mirror.

In Launchpad's web UI, go to the branch (perhaps "master" or "main") in your
repository that you want to build the charm from, and select "Create charm
recipe". Then:

   1. Fill in the charm recipe name, which identifies this particular recipe in
   Launchpad. You can normally just use the charm's name, but you might want to
   pick something different if you're maintaining multiple branches of your
   charm.

   2. You should normally select "Automatically build when branch changes".

   3. In most cases you won't need to specify any source snap channels, but for
   example you can use this to test your charm with candidate builds of
   charmcraft.

   4. To configure Launchpad to push builds to Charmhub, select "Automatically
   upload to store", fill in the name that you registered using charmcraft
   register, and select a channel to release to ("edge" is appropriate if
   you're not sure).

If you configured Launchpad to push builds to Charmhub, it will then obtain
authorization to do so on your behalf; follow the prompts in your web browser.

Your charm recipe is now ready to build! Select "Request builds" to dispatch
the first set of builds and see how they work. If all goes well, when you push
new commits to your branch, Launchpad will shortly afterwards dispatch builds
for all relevant architectures and push the resulting charms to Charmhub for
you. You are responsible for promoting charms to other channels after suitable
testing, using ``charmcraft release``.

***********************
 Notes and limitations
***********************

We only support building charms using Charmcraft, not the older `charm build
<https://launchpad.net/projects/+new>`_. (However, you can use the `reactive
plugin
<https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/build-guides/pack-a-reactive-charm-with-charmcraft/>`_
to build reactive charms.) This is partly based on the direction of
charm-building technology in Canonical, and partly because there's more use in
having a multi-architecture build system for Operator Framework charms: unlike
reactive charms and older frameworks, built OF charms are in practice always
architecture-dependent due to embedding architecture-dependent Python wheels.
As a result, in the absence of a multi-architecture build farm, the bulk of
charms would end up only existing on ``amd64``. We hope that providing charm
building in Launchpad will encourage most charms to support multiple
architectures by default.

We currently only support building charms not bundles. :ref:`Contact us <get-help>` 
if you have a use case for building bundles on Launchpad and would like to 
discuss it with us.

We don't currently support building OCI images to attach as resources to
charms. This is partly because that would be significantly more complex, partly
because we expect charms and resources to typically have quite different build
frequencies (changes to a resource very often require no changes to the
corresponding charm), and partly because in the long run it seems likely that
we'll want to encourage charms to consume something like rocks which should be
built separately anyway (although also by Launchpad).

Be careful to quote channel correctly in ``charmcraft.yaml``: you must write
channel: "``20.04``", not channel: ``20.04``. This is because the unquoted form
is interpreted by YAML as a fixed-point number rather than as a version string.

Launchpad charm recipes do not have any independent configuration of which
architectures to build. Instead, use bases in `charmcraft.yaml
<https://canonical-charmcraft.readthedocs-hosted.com/stable/howto/manage-charmcraft/>`_.

As yet, there is no support for private charms. Contact us if you have a use
case for this and would like to discuss it with us.

There are likely to be various minor UI deficiencies. We always welcome `bug
reports <https://bugs.launchpad.net/launchpad/+filebug>`_.
