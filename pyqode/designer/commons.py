#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#The MIT License (MIT)
#
#Copyright (c) <2013> <Colin Duquesnoy and others, see AUTHORS.txt>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
"""
Run this script to run qt designer with the pyqode plugins.

Requires
---------

On linux you need to install python-qt and python-qt-dev.

On windows you just have to install PyQt with its designer.

Usage
-----

You can try the pyqode qt designer plugin without installing pyqode, just run
designer.pyw from the source package.

If pyqode is installed, this script is installed into the Scripts folder on
windows or in a standard bin folder on linux. Open a terminal and run
**pyqode_designer**.
"""
import logging
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)
import os
import pkg_resources
import sys

from pyqode.qt import QtCore


def get_pth_sep():
    """
    Gets platform dependand path separator
    """
    if sys.platform == "win32":
        sep = ';'
    else:
        sep = ':'
    return sep


def get_plugins_path(sep):
    """
    Sets PYQTDESIGNERPATH
    """
    paths = ""
    dict = {}
    if sys.platform != "win32":
        # if the packages were installed through apt-get, then there is no
        # entry point.
        # We can check for all directories in pyqode root dir to find plugins
        import pyqode
        root = os.path.dirname(pyqode.__file__)
        for dir_name in os.listdir(root):
            dir_name = os.path.join(root, dir_name)
            if os.path.isdir(dir_name) and not "_" in dir_name:
                for sub_dir in os.listdir(dir_name):
                    if sub_dir == "plugins":
                        pth = os.path.join(dir_name, sub_dir)
                        paths += pth + sep
    for entrypoint in pkg_resources.iter_entry_points("pyqode_plugins"):
        try:
            plugin = entrypoint.load()
        except pkg_resources.DistributionNotFound:
            pass
        except ImportError:
            _logger.exception('failed to import plugin: %r', entrypoint)
        else:
            pth = os.path.dirname(plugin.__file__)
            _logger.info('plugin loaded: %s', pth)
            if not pth in dict:
                paths += pth + sep
                dict[pth] = None
    if 'PYQTDESIGNERPATH' in os.environ:
        pyqt_designer_path = os.environ['PYQTDESIGNERPATH'] + sep + paths
    else:
        pyqt_designer_path = paths
    _logger.info("pyQode plugins paths: %s", pyqt_designer_path)
    return pyqt_designer_path


def run(pyqt_designer_path):
    """
    Runs qt designer with PYQTDESIGNERPATH set to all loaded plugins.
    """
    base = os.path.dirname(__file__)
    env = QtCore.QProcessEnvironment.systemEnvironment()
    env.insert('PYQTDESIGNERPATH', pyqt_designer_path)

    # Start Designer.
    designer = QtCore.QProcess()
    designer.setProcessEnvironment(env)

    designer_bin = QtCore.QLibraryInfo.location(
        QtCore.QLibraryInfo.BinariesPath)

    if sys.platform == 'darwin':
        designer_bin += '/Designer.app/Contents/MacOS/Designer'
    else:
        designer_bin += '/designer'

    _logger.info('Qt Designer bin: %s' % designer_bin)

    designer.start(designer_bin)
    designer.waitForFinished(-1)
    logger = logging.getLogger('designer')
    logger.info(designer.readAllStandardOutput().data().decode('utf-8'))
    logger.error(designer.readAllStandardError().data().decode('utf-8'))
    sys.exit(designer.exitCode())


def main():
    """
    Runs the Qt Designer with an adapted plugin path.
    """
    pyqt_designer_path = get_plugins_path(get_pth_sep())
    return run(pyqt_designer_path)
