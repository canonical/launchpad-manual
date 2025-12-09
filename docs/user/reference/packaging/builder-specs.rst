.. _builder-specs:

Builder specs
=============

Launchpad's builders currently run with the following configuration for all architectures except for ppc64el:

- CPUs: 8

- RAM: 32 GB

- DISK: 100 GB

- SWAP: 8 GB

For ppc64el we have the folllowing spec in place:

- CPUs: 4

- RAM: 16 GB

- DISK: 80 GB

- SWAP: 4 GB

These specs are configured in the `Launchpad Mojo specs <https://launchpad.net/launchpad-mojo-specs>`__. 
Please note that hardware random number generation of the host is used.