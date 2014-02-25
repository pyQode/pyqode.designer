Qt Designer startup script
===================================

.. image:: https://pypip.in/d/pyqode.designer/badge.png
    :target: https://crate.io/packages/pyqode.designer/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/v/pyqode.designer/badge.png
    :target: https://crate.io/packages/pyqode.designer/
    :alt: Latest PyPI version

What is pyqode.designer?
----------------------------

pyqode.designer is a single scripts that starts Qt Designer with the installed pyqode plugins.

It uses pkg config to collect pyqode_plugins entry points and adapt the PYQTDESIGNERPATH env var before starting Qt Designer.


.. image:: https://raw.github.com/ColinDuquesnoy/pyqode.designer/master/share/screenshot.png
    :alt: Qt Designer with QGenericCodeEdit plugin

License
----------------

pyQode is licensed under the MIT license.


Requires
-------------
 - pyqode.core

On Windows you just need to install PyQt4 (it contains the Qt Designer and the python plugins dll)

On GNU/Linux you have to install the following packages:

 - qt4-designer
 - pyqt4-dev-tools

*Note that PyQt4 is only required to develop the ui files with Qt Designer, you can use and compile the ui files with PySide!*

Installation
------------

::

    $ pip install pyqode.designer
    
or ::

    $ python setup.py install
    
This will install the *pyqode-designer* gui script to your bin/Scripts folder.

Usage
-----

Open a terminal and run the following command::

    $ pyqode-designer
    
If you don't want to install the package, you can just run the designer script manually (in the pyqode package)::
 
    $ python pyqode/designer.py


.. note:: On GNU/Linux, a desktop entry in the Development category will be
          created when you install the package

Resources
---------

-  `Downloads`_
-  `Source repository`_
-  `Wiki`_

.. _Downloads: https://github.com/pyQode/pyqode.designer/releases
.. _Source repository: https://github.com/pyQode/pyqode.designer/
.. _Wiki: https://github.com/pyQode/pyqode.core/wiki


.. _pyQode: https://github.com/pyQode/pyqode.core
.. _Jedi: https://github.com/davidhalter/jedi


