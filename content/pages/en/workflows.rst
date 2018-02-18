Workflow
########

:order: 5
:date: 2018-01-25 08:46
:icon: icon-flow-children
:summary: Workflow and possible obstacles.
:lang: en
:slug: workflow
:use_disqus: true

Workflow
~~~~~~~~

Your productivity depends on your workflows alot. As an employe in a larger company and coding as a member of three teams on shared codebases is a challange some times. You need a tool supporting your workflows and not your workflows supporting a tool. Therefore gitcd might not be the right tool for you or doesent match your specific workflow perfectly. As a developer and sysadmin I personally work on many different repositories on a usual day. And each of it has different requirements. But at the same time, the workflow of all projects is quite similar. Thats the reason I even created gitcd, existing tools like gitflow/hubflow. Those just did not match our workflow quite properly or did not fullify our needs complete.


A very important thing in continuous delivery is continuous integration and reliable tests. Those should be executed automatically.

The following is a quite simple branching model which we use on all our projects and is well supported by gitcd.
The only disadvantage is that you might test features which never makes it into production. Therefore your Test branch might diverge quite a bit at some point. Our solution to this problem is to recreate the test branch from master frequently. In one project, we make this manually every two weeks at the sprint end on another one we create a new test branch from master every sunday evening in jenkins. There is still one problem remaining, if your test branch keeps the same name, everybody not deleting the branch locally might overwrite the history with the old, diverged content again.
We solve this by using a postfix, for example test-<sprint-number> or test-<date> respectively. This is also well supported by gitcd which is treatening the test branch setting as a prefix. If it finds more than one correspondig test branch, it will ask you which one you want to use. To keep your branches proper, git-cd clean was implemented, which will delete all your "test" branches not found on remote.


.. image:: /images/workflow/branching-model.svg
    :alt: branching model
    :width: 100%     