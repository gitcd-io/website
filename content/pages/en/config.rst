Configfile
##########

:order: 3
:date: 2018-01-25 08:46
:icon: icon-settings
:summary: The .gitcd configfile in detail.
:lang: en
:slug: config


The gitcd configfile
~~~~~~~~~~~~~~~~~~~~


The configfile is one of the core features of gitcd. Since it is stored in the repository, your workflow is under version control as well, you can have different configurations for each repository and all of your users will automatically have the same config and therefore will adapt to your workflow boundaries.

The configfile is written by executing ``git cd init`` but can also be edited by hand if it is more comfortable for you.


Explanation of values
---------------------

First, let me show you a complete configfile, for demonstration, I'll use the one of gitcd itself.

.. code-block:: yaml

    master: master
    feature: null
    test: test
    tag: v
    versionType: file
    versionScheme: version.txt
    extraReleaseCommand: ./publish.sh

Now lets step through the values.

- master
    This represents your master branch. New feature branches will be derived from this branch as well as tagging will happen on this branch.
- feature
    This value is used as a prefix for your feature branches. Many projects use "feature/my-awesome-feature" for feature branch names. If this is the case, you can setup the prefix "feature/" here. Then, if you start a new feature by executing ``git cd start my-awesome-feature`` your new branch will end up with the desired name. Of course you can just let it empty as I do it in gitcd. Gitcd will then not use any prefix for feature branches.
- test
    This is the branch name you want to use for testing purposes. For example, in a lot of projects I work on we use this kind of branch for integration tests. This can be understood as a prefix as well. This is for the reason you might never merge the test branch back into your master but just merging features into your test branch. If this is the case and a feature is maybe to bad to make it into the master, this test branch will diverge from your master over time. At my workplace we solve this by drop a test branch on sunday night automatically and create a new one derived from master. To prevent users pushing the old history, our test branch gets a suffix. For example the sprint number or the current date. For example we have in two projects currently the test branches "test-159" and "develop-2018-03-04" respectively. Developers can execute a ``git cd clean`` on monday morning to get their local repositories up to date with the remote one.
- tag
    This is a prefix used for tags, usually this will be v or just null. If you have setup v as a prefix and releasing version 1.0.0, gitcd will tag this version as v1.0.0 on your remote.
- versionType [manual|file|date]
    You have different options to get to your version number

    \

    **manual**
    As you might consider, if you setup manual version numbers, gitcd will ask you for a number when you execute the release command.

    \

    **file**
    If you have a file storing your current version, this is the ideal option for you. Gitcd itself stores it version in a text file called version.txt. This is also used in setup.py for pushing the package to python package index. If you setup this option, you need to setup the file which is storing your version number in "versionScheme". \

    \

    **date**
    If you want to use a date format as version, this is the option for you. Even if i think it does not make much sense, I don't judge on you since, you might have already thought it, I implemented this option because we actually use it on a project at my workplace.
- versionScheme
    This option is tightly bound to the versionType setting. If you have choosen a manual versionType, you need to let this with null. If you have choosen version number by file, this is the option where your file path is stored. And finally, if you have choosen the type date, you can store the desired date format here. Read through python date formats for the right value: http://strftime.org/
- extraReleaseCommand
    You are able to execute any given command while executing ``git cd release`` for example, gitcd executes ./publish.sh which pushes the new package to the python package index.