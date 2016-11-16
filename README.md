A command-line code formatter that enforces MarkLogic corporate branding guidelines. 

## Usage

```shell
pygmentize -f rtf -O "style=marklogic,fontface=Consolas" setup.py | pbcopy
```


## Installation

1. Make sure you’re running Python 3 (`python --version`)
1. `pip install -r requirements.txt`

## Development Set-up

Create a new Python 3 virtual environment.

First time

1. `mkdir env`
1. `pyvenv env/python3`
1. `echo 'env' >> .gitignore`

In a new shell,

1. `source env/python3/bin/activate`

## Register Style

Based on [“Custom syntax in pygments”](http://www.catchmecode.com/2013/03/custom-syntax-in-pygments.html).

_(You set up and activated the virtual environment above, right?)_

1. `cd MarkLogicStyle`
1. `python setup.py develop`
