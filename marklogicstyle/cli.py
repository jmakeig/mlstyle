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

import sys
import docopt

from pygments.cmdline import main as pyg

def main(args=sys.argv):
    """
    Main command line entry point.
    Pass-through for pygmentize CLI.
    """

    pass_thru = ['-L', '-S', '-H', '-v', '-h']

    if not list(filter(set(args).__contains__, pass_thru)): # List intersection
        ml_opts = [
            '-P', 'style=marklogic',
            '-P', 'fontface=Consolas',
            '-P', 'fontsize=32', # Doesn’t seem to have any effect pasting into PowerPoint
        ]
        args[1:1] = ml_opts

    # print(args, file=sys.stderr)
    return pyg(args)
