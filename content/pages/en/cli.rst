CLI Usage
#########

:order: 3
:date: 2018-01-25 08:46
:icon: icon-code-outline
:summary: How to use gitcd on the Command Line.
:lang: en
:slug: cli
:use_disqus: true

CLI Usage of gitcd
~~~~~~~~~~~~~~~~~~~~~

For coninience, you can call gitcd as a git subcommand as well. Therefore you can replace "git-cd" in any of the following commands with "git cd" if you like it more.


.. container:: alert alert-warning

    Note: Python argument completion wont work if you use it as a git subcommand!


Check version and upgrade
-------------------------
Gitcd is able to check your local version with the one published on pypi and upgrade itself if you wish so.

.. code-block:: bash

    git-cd upgrade

.. image:: /images/cli/git-cd_upgrade.png
    :alt: git-cd upgrade
    :width: 100%

Clean up local branches
-----------------------