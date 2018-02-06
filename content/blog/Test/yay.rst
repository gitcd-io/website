yay
##########

:date: 2018-12-22 18:32
:image: images/sublime.png
:tags: biber, tiger, super, duper
:summary: well, its bad if you just forget about it

Hui Buh

.. code-block:: bash

    #!/bin/bash
    cd $(dirname $0)/..;
    rm -f /opt/*;
    function start {
        docker-compose up -d;
    }

    function stop {
        docker-compose stop;
    }
