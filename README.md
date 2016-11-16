A command-line code formatter that enforces MarkLogic corporate branding guidelines. 

Based on [“Custom syntax in pygments”](http://www.catchmecode.com/2013/03/custom-syntax-in-pygments.html).

## Usage

* OS X/macOS

    ```shell
    pygmentize -f rtf -O "style=marklogic,fontface=Consolas" setup.py | pbcopy
    ```
* Windows _(TODO)_

## Installation

```shell
pip install marklogicstyle
```

## Development Set-up

Use a Python 3 virtual environment.

First time,

1. `mkdir env`
1. `echo 'env' >> .gitignore`
1. `pyvenv env/python3`

In a virgin shell,

1. `source env/python3/bin/activate` to activate the environment (and `deactivate` to deactivate it)
1. `pip install -r requirements.txt`
1. `python setup.py develop`

## Distribution

First time, [manually register on the PyPi web site](https://pypi.python.org/pypi?%3Aaction=submit_form).

1. `python setup.py sdist upload`

See also [“Packaging and Distributing Projects”](https://packaging.python.org/distributing/#uploading-your-project-to-pypi).
