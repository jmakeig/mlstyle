# mlstyle

A command-line code formatter that enforces MarkLogic corporate branding guidelines. 

Given a snippet of code as a file or on your clipboard, `mlstyle` will turn that into pretty, syntax-highlighted text suitable for pasting into PowerPoint, or just about anywhere.

_“Why would I want to use this?”_

Code snippets in PowerPoint or Word (or anywhere outside of your editor) are very difficult to read without proper formatting. Moreover, one-off implementations tend to vary greatly in aesthetics and usability. `mlstyle` makes it so you don’t have to think about anything when it comes to formatting your code for presentation outside of your editor. It will format your code according to the official MarkLogic branding guidelines and usability standards.

_“How does it work?”_

`mlstyle` is a very thin wrapper around the popular Python-based [Pygments](http://pygments.org) library. Pygments supports hundreds of different languages and other data types and dozens of output formats. `mlstyle` implements the same [command-line interface as `pygmentize`](http://pygments.org/docs/cmdline/), the Pygments command-line utility. `mlstyle` seeds the appropriate defaults for the official MarkLogic branding guidelines. 

## Example

```shell
mlstyle -f html -P 'noclasses=true' setup.py
```

<div class="highlight"><pre style="line-height: 125%"><span></span><span style="color: #3f7f5f"># coding=utf-8</span>

<span style="color: #3f7f5f"># Copyright 2016 MarkLogic Corporation</span>
<span style="color: #3f7f5f">#</span>
<span style="color: #3f7f5f"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span>
<span style="color: #3f7f5f"># you may not use this file except in compliance with the License.</span>
<span style="color: #3f7f5f"># You may obtain a copy of the License at</span>
<span style="color: #3f7f5f">#</span>
<span style="color: #3f7f5f">#    http://www.apache.org/licenses/LICENSE-2.0</span>
<span style="color: #3f7f5f">#</span>
<span style="color: #3f7f5f"># Unless required by applicable law or agreed to in writing, software</span>
<span style="color: #3f7f5f"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span>
<span style="color: #3f7f5f"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>
<span style="color: #3f7f5f"># See the License for the specific language governing permissions and</span>
<span style="color: #3f7f5f"># limitations under the License.</span>

<span style="color: #2a3483; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">setuptools</span> <span style="color: #2a3483; font-weight: bold">import</span> setup, find_packages

setup(
    name<span style="color: #666666">=</span><span style="color: #BA2121">&#39;marklogicstyle&#39;</span>,
    version<span style="color: #666666">=</span><span style="color: #BA2121">&#39;0.3.0&#39;</span>,
    description<span style="color: #666666">=</span><span style="color: #BA2121">&#39;MarkLogic code syntax highlighting and beautification for PowerPoint&#39;</span>,
    long_description<span style="color: #666666">=</span><span style="color: #BA2121">&quot;&quot;&quot;</span>
<span style="color: #BA2121">A command-line code formatter that enforces MarkLogic corporate branding guidelines.</span>

<span style="color: #BA2121">Given a snippet of code as a file or on your clipboard, mlstyle will turn that into pretty, syntax-highlighted text suitable for pasting into PowerPoint, or just about anywhere.</span>
<span style="color: #BA2121">    &quot;&quot;&quot;</span>,
    packages<span style="color: #666666">=</span>find_packages(),
    platforms<span style="color: #666666">=</span>[<span style="color: #BA2121">&#39;POSIX&#39;</span>, <span style="color: #BA2121">&#39;Windows&#39;</span>],
    entry_points<span style="color: #666666">=</span>{
        <span style="color: #BA2121">&#39;pygments.styles&#39;</span>: [<span style="color: #BA2121">&#39;marklogic = marklogicstyle.style:MarkLogicStyle&#39;</span>],
        <span style="color: #BA2121">&#39;console_scripts&#39;</span>: [<span style="color: #BA2121">&#39;mlstyle = marklogicstyle.cli:main&#39;</span>],
    },
    install_requires<span style="color: #666666">=</span>[
        <span style="color: #BA2121">&#39;docopt&#39;</span>, <span style="color: #BA2121">&#39;Pygments&#39;</span>
    ],
    author<span style="color: #666666">=</span><span style="color: #BA2121">&#39;Justin Makeig&#39;</span>,
    author_email<span style="color: #666666">=</span><span style="color: #BA2121">&#39;jmpublic+github@makeig.com&#39;</span>,
    url<span style="color: #666666">=</span><span style="color: #BA2121">&#39;https://github.com/jmakeig/mlstyle&#39;</span>,
    license<span style="color: #666666">=</span><span style="color: #BA2121">&#39;Apache-2.0&#39;</span>,
)
</pre></div>

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
mlstyle -f rtf myfile.xqy
```

or send the highlighted text to Microsoft Word

```shell
mlstyle -f rtf myfile.xqy | open -f -b com.microsoft.Word
```

or to the clipboard to paste anywhere

```shell
mlstyle -f rtf myfile.xqy | pbcopy
```

### Windows 

```shell
mlstyle -f rtf myfile.xqy > 
```


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
