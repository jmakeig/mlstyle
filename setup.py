# coding=utf-8

# Copyright 2016 MarkLogic Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='marklogicstyle',
    version='0.3.0',
    description='MarkLogic code syntax highlighting and beautification for PowerPoint',
    long_description="""
A command-line code formatter that enforces MarkLogic corporate branding guidelines.

Given a snippet of code as a file or on your clipboard, mlstyle will turn that into pretty, syntax-highlighted text suitable for pasting into PowerPoint, or just about anywhere.
    """,
    packages=find_packages(),
    platforms=['POSIX', 'Windows'],
    entry_points={
        'pygments.styles': ['marklogic = marklogicstyle.style:MarkLogicStyle'],
        'console_scripts': ['mlstyle = marklogicstyle.cli:main'],
    },
    install_requires=[
        'docopt', 'Pygments'
    ],
    author='Justin Makeig',
    author_email='jmpublic+github@makeig.com',
    url='https://github.com/jmakeig/pulchritude',
    license='Apache-2.0',
)
