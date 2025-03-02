# nbz


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Check out the [video
demo](https://www.loom.com/share/5bbc2abcc73d45498be4259cb108dc64?sid=4b367d88-a20d-45d2-bea7-e569959e9e35)!

[nbdev](https://nbdev.fast.ai/) (*pronounced ‘en-bee-zed’*) is an
incredible software development environment. You write code in notebooks
and it exports the result to Python flatfiles. It also handles
documentation, version releases, and so much more.

The goal of this project is to do the following, with items 2 and 3
being potential targets for upstream changes to nbdev:

1.  Wrap the nbdev command-line interface with
    [typer](https://typer.tiangolo.com/) to take advantage of some of
    the features of that framework (formatting, auto-completion, etc)
2.  Enhance the existing CLI documentation
3.  Add new features that may or may not fit in nbdev
4.  Provide an interface for other systems

## Developer Guide

If you are new to using `nbdev` here are some useful pointers to get you
started.

### Install nbz in Development mode

``` sh
# make sure nbz package is installed in development mode
$ pip install -e .

# make changes to nbs/core.ipynb
# ...

# compile to have changes apply to nbz

$ nbz export
$ nbz clean
$ nbz trust
```

## Usage

### Installation

Install latest from the GitHub
[repository](https://github.com/pydanny/nbz):

``` sh
$ pip install git+https://github.com/pydanny/nbz.git
```

COMING SOON: or from [conda](https://anaconda.org/pydanny/nbz)

``` sh
$ conda install -c pydanny nbz
```

COMING SOON: or from [pypi](https://pypi.org/project/nbz/)

``` sh
$ pip install nbz
```

### Documentation

Documentation can be found hosted on this GitHub
[repository](https://github.com/pydanny/nbz)’s
[pages](https://pydanny.github.io/nbz/). Additionally you can find
package manager specific guidelines on
[conda](https://anaconda.org/pydanny/nbz) and
[pypi](https://pypi.org/project/nbz/) respectively.

## Using nbz

Once you’ve installed `nbz`, check that all dependencies have been
installed and secrets have been configured with the
[`check`](https://pydanny.github.io/nbz/commands.html#check) command:

``` bash
nbz check
```

Now let’s create a new project, which we’ll call silo. From the
directory where you create your projects, run the following command:

``` sh
nbz new silo
```

This will attempt to infer your prefences from git, but for things it
can’t figure out, it will prompt you for answers:

``` bash
Creating and changing to silo directory
repo = nbz # Automatically inferred from git
branch = main # Automatically inferred from git
user = pydanny # Automatically inferred from git
author = Daniel Roy Greenfeld # Automatically inferred from git
author_email = daniel@feldroy.com # Automatically inferred from git
description = nbz is a typer-based wrapper around the incredible nbdev project. # Automatically inferred from git
settings.ini created.
pandoc -o README.md
  to: >-
    commonmark+autolink_bare_uris+emoji+footnotes+gfm_auto_identifiers+pipe_tables+strikeout+task_lists+tex_math_dollars
  output-file: index.html
  standalone: true
  default-image-extension: png

metadata
  description: nbz is a typer-based wrapper around the incredible nbdev project.
  title: nbz

Output created: _docs/README.md
```
