# mlstyle

A command-line code formatter that enforces MarkLogic corporate branding guidelines. 

Given a snippet of code as a file or on your clipboard, `mlstyle` will turn that into pretty, syntax-highlighted text suitable for pasting into PowerPoint, or just about anywhere.

_“Why would I want to use this?”_

Code snippets in PowerPoint or Word (or anywhere outside of your editor) are very difficult to read without proper formatting. Moreover, one-off implementations tend to vary greatly in aesthetics and usability. `mlstyle` makes it so you don’t have to think about anything when it comes to formatting your code for presentation outside of your editor. It will format your code according to the official MarkLogic branding guidelines and usability standards.

_“How does it work?”_

`mlstyle` is a very thin wrapper around the popular Python-based [Pygments](http://pygments.org) library. Pygments supports hundreds of different languages and other data types and dozens of output formats. `mlstyle` implements the same [command-line interface as `pygmentize`](http://pygments.org/docs/cmdline/), the Pygments command-line utility. `mlstyle` seeds the appropriate defaults for the official MarkLogic branding guidelines. 

## Installation

`mlstyle` is implemented in [Python](https://www.python.org). It was developed for Python3, but works with recent versions of Python 2 as well. 

```shell
pip install marklogicstyle
```

It is recommended, but not required that you install `mlstyle` into a virtual environemnt. If you’re installing globally, you may be required to use `sudo -H` _(not recommended)_.

## Usage

`mlstyle` is drop-in replacement for the [`pygmentize` command-line interface](http://pygments.org/docs/cmdline/) for Pygments.

### OS X/macOS

For example, to generate an RTF document with a syntax-highlighted version of `setup.py`,

```shell
mlstyle -f rtf setup.py
```

or send the highlighted text to Microsoft Word

```shell
mlstyle -f rtf setup.py | open -f -b com.microsoft.Word
```

or to the clipboard to paste anywhere

```shell
mlstyle -f rtf setup.py | pbcopy
```

### Windows _(TODO)_

--------------------------------------------------------

## Development Set-up

Use a Python 3 [virtual environment](https://docs.python.org/3/library/venv.html).

First time,

1. `mkdir env`
1. `pyvenv env/python3` or `virtualenv env/python2` for Python 2

In a virgin shell,

1. `source env/python3/bin/activate` to activate the environment (and `deactivate` to deactivate it)
1. `pip install -r requirements.txt`
1. `python setup.py develop`

## Distribution

First time, [manually register on the PyPi web site](https://pypi.python.org/pypi?%3Aaction=submit_form).

1. `python setup.py sdist upload`

See also [“Packaging and Distributing Projects”](https://packaging.python.org/distributing/#uploading-your-project-to-pypi).
