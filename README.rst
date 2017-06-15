======
Hermes
======


.. image:: https://img.shields.io/pypi/v/Hermes.svg
        :target: https://pypi.python.org/pypi/Hermes

.. image:: https://img.shields.io/travis/somosprte/Hermes.svg
        :target: https://travis-ci.org/somosprte/Hermes

.. image:: https://readthedocs.org/projects/Hermes/badge/?version=latest
        :target: https://Hermes.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


The Hermes project uses a zigbee network, hence it works with zigbee protocol, and this requires interacting with low-level hardware.


* Free software: MIT license
* Documentation: https://hermes.readthedocs.io.


Hermes
======

.. image:: https://github.com/somosprte/Hermes/blob/master/img/logo-hermes-final.png

The Hermes project uses a zigbee network, hence it works with zigbee protocol, and this requires interacting with low-level hardware.

The idea of using python is because of performance, simplicity and ease of dealing with hardware.

In the initial design, we will have a Raspberry Pi, which would function as a server, connected to an xbee card in the USB port, the interaction via serial, and the idea is that Raspberry Pi, through its Wi-Fi network, provides a restfull service to that when requested the status of an X port dialogically type server/port1, there is the hexadecimal communication with xbee, so that it searches for this information.

Development
===========

Before start, on GitHub, fork Hermes project (https://github.com/somosprte/Hermes)

So, on the root folder when the project should be cloned, type:

.. code-block:: bash

    git clone https://github.com/<your-user-id>/Hermes.git


Environment
-----------

If you are using conda, before the code bellow, enter into the Hermes folder. Next, type the following commands:

.. code-block:: bash

    conda create --name hermes python=3.4

    source activate hermes

    conda install --file requirements.txt


The Python interpret installed should be version 3.4, because this is the version used by Raspberry Pi 2 (armv6l), at this moment.

If you are using virtualenv (remember to use Python 3.4), on the Hermes folder, type:

.. code-block:: bash

    virtualenv .

    source bin/activate

    pip install -r requirements.txt


To run the project, type:

.. code-block:: bash

    python hermes.py


Start API
---------

To start the api do:

.. code-block:: bash

    python hermes.py


And to test it:

.. code-block:: bash

    $ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
    {"todo1": "Remember the milk"}
    
    $ curl http://localhost:5000/todo1
    {"todo1": "Remember the milk"}
    
    $ curl http://localhost:5000/todo2 -d "data=Change my brakepads" -X PUT
    {"todo2": "Change my brakepads"}
    
    $ curl http://localhost:5000/todo2
    {"todo2": "Change my brakepads"}


(resource: `[3]`)


References
==========

[1] https://www.continuum.io/downloads

[2] https://conda.io/miniconda.html

[3] http://flask-restful-cn.readthedocs.io/en/0.3.5/quickstart.html

