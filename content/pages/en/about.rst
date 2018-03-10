About
#####

:order: 1
:date: 2018-01-25 08:46
:icon: icon-link2
:summary: Learn about gitcd.
:lang: en
:slug: about
:show_on_home: false


About gitcd
~~~~~~~~~~~


Why the heck another tool for continuous delivery you might ask? Eligible question i might say. The main reason is that existing tools like gitflow, hubflow or reflow just didn't quite matched the desired `workflow`_. in the company i currently work. Branching models like nvie are very complicated and might be confusing to people which are new to git or cd in general.

I strongly believe your workflow should not support a tool but a tool should support your workflow.

If you feel that gitcd is not supporting your desired workflow, drop me an `issue`_. about it and I'll see if I can implement it properly.


Advantages of gitcd
-------------------

\

- Configuration in the git repository
    Gitcd stores the configuration of your current workflow in a  .gitcd config file within the repository you working on.
    Therefore the configuration gets committed and is inside your project. Which means only one person needs to setup all the things using git cd init and everybody else gets the same config by cloning your repository.
- Simple workflow
    The minimum branches you need is currently a master branch for simple projects. You deviate feature branches from master branches and merge it back into if they are finished.
- Flexibility
    Still you have the flexibility to setup a test branch, lets say for integration tests or anything else, you name it.
    You can have different configs for each repository you want to use gitcd for. For releases you can execute additional scripts or commands, as I do it in the gitcd repository itself to push the sources to the python package index.
- Multiple remotes
    Gitcd can handle multiple remotes, if you use more than one remote in your repository, gitcd will kindly ask you which one to use for the given action. Right now, gitcd works with github and bitbucket as remotes. There are plans to integrate gitlab and self hosted gitlabs as well.


.. _issue: https://github.com/gitcd-io/gitcd/issues
.. _workflow: https://www.gitcd.io/pages/workflow.html
