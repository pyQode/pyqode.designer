#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Colin Duquesnoy
#
# This file is part of pyQode.
#
# pyQode is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# pyQode is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with pyQode. If not, see http://www.gnu.org/licenses/.
#
"""
This setup script packages the core package of pyQode: pyqode-core
"""
from setuptools import setup, find_packages


def readme():
    return str(open('README.rst').read())


setup(
    name='pyqode.designer',
    namespace_packages=['pyqode'],
    version="1.0b1",
    packages=find_packages(),
    keywords=["QCodeEditor", "PySide", "PyQt", "designer", "Qt"],
    url='https://github.com/ColinDuquesnoy/pyqode.designer',
    license='GNU LGPL v3',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='Starts Qt Designer with pyqode plugins',
    long_description=readme(),
    entry_points={'gui_scripts': [
                  'pyqode-designer = pyqode.designer:main']},)
