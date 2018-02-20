Installation
############

:order: 2
:date: 2018-01-25 08:46
:icon: icon-download
:summary: How to install gitcd.
:lang: en
:slug: installation
:use_disqus: true

Installation of gitcd
~~~~~~~~~~~~~~~~~~~~~


Pre requisites
--------------
Gitcd is written in Python3. Most systems still deliver with Python2 as default.
You need to install Python3 in order to run gitcd properly.

MacOSX
______

.. code-block:: bash

    brew install python3

Ubuntu / Debian
_______________

.. code-block:: bash

    sudo apt-get install python3 python3-pip


Installation of gitcd itself
----------------------------
Now you are ready to install gitcd itself, which is quite easy using pip.

.. code-block:: bash

    pip3 install --user --upgrade gitcd


Trouble using git-cd?
---------------------
If the command "git-cd" or "git cd" is not available now, you probably need to add the pip binary path to your $PATH variable.

MacOSX
______

Open ~/.bash_profile in your favorite editor and add the following lines at the end of the file.

.. container:: alert alert-warning

    Replace <python-version> with your currently installed python version

.. code-block:: bash

    if [ -d "$HOME/Library/Python/<python-version>/bin" ] ; then
        PATH="$HOME/Library/Python/<python-version>/bin:$PATH"
    fi

Ubuntu / Debian
_______________

Open ~/.profile in your favorite editor and add the following lines at the end of the file.

.. code-block:: bash

    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi


Argument Completion
-------------------
Gitcd supports argument completion, to activate it execute the following steps.

MacOSX
______

Under OSX it isn't that simple unfortunately. Global completion requires bash support for complete -D, which was introduced in bash 4.2. On OS X or older Linux systems, you will need to update bash to use this feature. Check the version of the running copy of bash with echo $BASH_VERSION. On OS X, install bash via Homebrew (brew install bash), add /usr/local/bin/bash to /etc/shells, and run chsh to change your shell.

You might consider reading the docs for argcomplete https://argcomplete.readthedocs.io/en/latest/#global-completion

Activate Global argcomplete
_____________________________

You are now ready to activate global argcompletion for python with the following command.

.. code-block:: bash

    activate-global-python-argcomplete
