Qt Designer startup script
==========================

.. image:: https://pypip.in/d/pyqode.designer/badge.png
    :target: https://crate.io/packages/pyqode.designer/
    :alt: Number of PyPI downloads

.. image:: https://pypip.in/v/pyqode.designer/badge.png
    :target: https://crate.io/packages/pyqode.designer/
    :alt: Latest PyPI version

What is pyqode.designer?
------------------------

pyqode.designer is a single scripts that starts Qt Designer with the installed
`pyQode`_ plugins.

It uses pkg_config to collect pyqode_plugins entry points and adapt the
PYQTDESIGNERPATH env var before starting Qt Designer.


.. image:: https://raw.github.com/ColinDuquesnoy/pyqode.designer/master/share/screenshot.png
    :alt: Qt Designer with QGenericCodeEdit plugin

License
-------

pyQode is licensed under the MIT license.


Requires
--------

Here are the tools and packages required to run the designer:

 - Qt Designer for Qt4 or Qt5
 - PyQt4 or PyQt5 + dev tools
 - pyqode.core

**On Windows**, you just need to install PyQt4 or PyQt5 (it contains the
Qt Designer and the python plugins dll)

**On GNU/Linux**, you have to install the following packages:

    * For PyQt4:

      - qt4-designer
      - pyqt4-dev-tools

    * For PyQt5:

      - qt5-designer
      - pyqt5-dev-tools

*Note that PyQt4 is required to develop the ui files but you can use and
compile the ui files with PySide!*


Installation
------------

::

    $ pip3 install pyqode.designer
    
or ::

    $ python3 setup.py install
    
This will install the *pyqode-designer-qt4* and *pyqode-designer-qt5* gui
scripts into your bin/Scripts folder.

Usage
-----

Open a terminal and run the following command::

    $ pyqode-designer-qt4

or

    $ pyqode-designer-qt5


If you don't want to install the package, you can just run the scripts
manually::

    $ python pyqode/designer/qt4.py

or

    $ python pyqode/designer/qt5.py

.. note:: On GNU/Linux, a desktop entry in the Development category will be
          created for each designer script when you install the package (using
          pip or from the debian package).

Resources
---------

-  `Downloads`_
-  `Source repository`_
-  `Wiki`_

.. _Downloads: https://github.com/pyQode/pyqode.designer/releases
.. _Source repository: https://github.com/pyQode/pyqode.designer/
.. _Wiki: https://github.com/pyQode/pyqode.core/wiki
.. _pyQode: https://github.com/pyQode/pyqode.core
