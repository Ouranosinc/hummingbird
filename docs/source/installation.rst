.. _installation:

Installation
************

Check out code from the Hummingbird github repo and start the installation::

   $ git clone https://github.com/bird-house/hummingbird.git
   $ cd hummingbird
   $ make

For other install options run ``make help`` and read the documention of the `Makefile <https://github.com/bird-house/birdhousebuilder.bootstrap/blob/master/README.rst>`_.

After successful installation you need to start the services. Hummingbird is using `Anaconda <http://www.continuum.io/>`_ Python distribution system. All installed files (config etc ...) are below the Anaconda root folder which is by default in your home directory ``~/anaconda``. Now, start the services::

   $ make start    # starts supervisor services
   $ make status   # shows supervisor status

The depolyed WPS service is by default available on http://localhost:8092/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors::

   $ tail -f  ~/anaconda/var/log/pywps/hummingbird.log
   $ tail -f  ~/anaconda/var/log/pywps/hummingbird_trace.log





