Installation
############

:order: 2
:date: 2018-01-25 08:46
:icon: icon-code-outline
:summary: Wie man gitcd installiert.
:lang: de
:slug: installation
:use_disqus: true

Installation von gitcd
~~~~~~~~~~~~~~~~~~~~~~


Voraussetzungen
---------------
Gitcd setzt gewisse Software und Python Module voraus. Zu allererst, gitcd ist in Python3 geschrieben.
Für das gui (welches aktuell nicht weit forgeschritten ist) musst du kivy und kivyMD installieren. Die Installation von kivy über die Python setuptools ist leider nicht gerade einfach und vor allem sehr Zeitintensiv.

Führe die folgenden Schritte aus um gitcd sauber auf Mac MacOSX und auf Ubuntu (klappt vermutlich auf allen Debian Derivaten).

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
Du bist jetzt bereit gitcd selbst zu installieren, mit pip ist das sehr einfach.

.. code-block:: bash

    pip3 install --user --upgrade gitcd

Probleme git-cd auf der cli zu verwenden?
-----------------------------------------
Wenn du jetzt keinen cli Befehl "git-cd" oder "git cd" verfügbar hast musst du vermutlich den Pfad installierter Python Programme in deine lokale $PATH Variable aufnehmen.

MacOSX
______

Öffne ~/.bash_profile in deinem bevorzugten Editor und füge die folgenden Zeilen am Ende der Datei hinzu.

.. container:: alert alert-warning

    Ersetze <python-version> mit deiner installierten Python Version

.. code-block:: bash

    if [ -d "$HOME/Library/Python/<python-version>/bin" ] ; then
        PATH="$HOME/Library/Python/<python-version>/bin:$PATH"
    fi

Ubuntu / Debian
_______________

Öffne ~/.profile in deinem bevorzugten Editor und füge die folgenden Zeilen am Ende der Datei hinzu

.. code-block:: bash

    if [ -d "$HOME/.local/bin" ] ; then
        PATH="$HOME/.local/bin:$PATH"
    fi

Argument Completion
-------------------
Gitcd unterstützt argument completion, um das Feature zu aktivieren führe die folgenden Schritte aus.

MacOSX
______

Unter OSX ist das leider gar nicht so einfach. Globale argument completion setzt Bash Unterstützung für complete -D voraus. Dieses Feature hat erst mit Bash Version 4.2 Einzug erhalten. Unter OSX und älteren Linux Systemen musst du deine Bash aktualisieren um dieses Feature nutzen zu können.
Prüfe deine aktuelle Bash Version mit echo $BASH_VERSION. Unter OSX kannst du deine Bash mit Homebrew aktualisieren (brew install bash), dann den Pfad /usr/local/bin/bash zu /etc/shells hinzufügen und schliesslich chsh ausführen um die Änderung zu aktivieren.

Du möchtest dir vielleicht die offizielle Dokumentation hierzu durchlesen https://argcomplete.readthedocs.io/en/latest/#global-completion

Aktiviere argcompletion Systemweit
__________________________________

Jetzt bist du bereit argcompletion für Python Systemweit zu aktivieren, führe dazu das folgende Kommando aus.

.. code-block:: bash

    activate-global-python-argcomplete
