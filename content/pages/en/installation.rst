Installation
############

:order: 2
:date: 2018-01-25 08:46
:icon: icon-code-outline
:summary: How to install gitcd.
:lang: en
:slug: installation
:use_disqus: true

Installation of gitcd
~~~~~~~~~~~~~~~~~~~~~


Pre requisites
--------------
Gitcd needs some pre requisites in order to work properly. First of all it is written in Python3.
Then for the gui (which is not far in progress right now) you need to install kivy and kivyMD which is not that easy and very time intense to do by python setuptools.

Following are the steps to install all the pre requisites on MacOSX and on Ubuntu (might apply to any Debian derivate).

MacOSX
______

.. code-block:: bash

    brew install python3
    brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
    pip3 install -I Cython==0.25.2
    pip3 install kivy
    pip3 install kivymd


Ubuntu / Debian
_______________

.. code-block:: bash

    sudo apt-get install python3 python3-pip
    sudo apt-get install python3-kivy
    pip3 install kivymd


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
You want to read the creators instruction. 