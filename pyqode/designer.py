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
import multiprocessing
import os
os.environ.setdefault("QT_API", "PyQt")
import pkg_resources
import subprocess
import sys


def get_pth_sep():
    """
    Gets platform dependand path separator
    """
    if sys.platform == "win32":
        sep = ';'
    else:
        sep = ':'
    return sep


def set_plugins_path(env, sep):
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
            print('failed to import plugin: %r' % entrypoint)
        else:
            pth = os.path.dirname(plugin.__file__)
            print('plugin loaded: %s' % pth)
            if not pth in dict:
                paths += pth + sep
                dict[pth] = None
    if 'PYQTDESIGNERPATH' in env:
        pyqt_designer_path = env['PYQTDESIGNERPATH']
        env['PYQTDESIGNERPATH'] = pyqt_designer_path + sep + paths
    else:
        env['PYQTDESIGNERPATH'] = paths
    print("pyQode plugins paths: %s" % env["PYQTDESIGNERPATH"])


def run(env):
    """
    Runs qt designer with our customised environment.
    """
    p = None
    env["PYQODE_NO_COMPLETION_SERVER"] = "1"
    try:
        p = subprocess.Popen(["designer-qt4"], env=env)
        if p.wait():
            raise OSError()
    except OSError:
        try:
            p = subprocess.Popen(["designer"], env=env)
            if p.wait():
                raise OSError()
        except OSError:
            print("Failed to start Qt Designer")
    if p:
        return p.wait()
    return -1


def check_env(env):
    """
    Ensures all key and values are strings on windows.
    """
    if sys.platform == "win32":
        win_env = {}
        for key, value in env.items():
            win_env[str(key)] = str(value)
        env = win_env
    return env


def main():
    """
    Runs the Qt Designer with an adapted plugin path.
    """
    sep = get_pth_sep()
    env = os.environ.copy()
    set_plugins_path(env, sep)
    env = check_env(env)
    return run(env)


if __name__ == "__main__":
    sys.exit(main())
