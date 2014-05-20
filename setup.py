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
This setup script packages the core package of pyQode: pyqode-core
"""
from setuptools import setup, find_packages
import sys


def readme():
    return str(open('README.rst').read())


data_files = []
if sys.platform == "linux":
    data_files.append(('/usr/share/applications',
                       ['share/pyqode_designer.desktop']))


setup(
    name='pyqode.designer',
    namespace_packages=['pyqode'],
    version="1.2",
    packages=find_packages(),
    data_files=data_files,
    keywords=["QCodeEditor", "PySide", "PyQt", "designer", "Qt"],
    url='https://github.com/pyQode/pyqode.designer',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='Starts Qt Designer with pyqode plugins',
    long_description=readme(),
    install_requires=["pyqode.core"],
    entry_points={'gui_scripts': [
                  'pyqode-designer = pyqode.designer:main']},
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications :: Qt',
          'Environment :: Win32 (MS Windows)',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3'
    ]
)
