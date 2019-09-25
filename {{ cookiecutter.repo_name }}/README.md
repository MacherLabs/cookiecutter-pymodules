{{  cookiecutter.project_name }}
========

{{ cookiecutter.project_short_description }}

# Installation

## Pre-Requisites

Following pre-requisites are needed before installation:

- python 2.7

## Install Pip package

After the pre-requisites are installed, clone this repository using git and move into the repository by running: 

```bash
cd {{ cookiecutter.repo_name }}
pip install .
```

# Usage

# Development

## Test:

To run all the tests, just run
```
$ tox
```
To build and verify that the built package is proper and other code QA checks::
```
  tox -e check
```

## Releasing the project
Before releasing your package on PyPI you should have all the tox environments passing.

### bump version:
```
$ bumpversion [major|minor|patch] --commit --tag
```

### Building and uploading

Before building dists make sure you got a clean build area:
```
$ rm -rf build
$ rm -rf src/*.egg-info
```
Then you should check that you got no packaging issues::
```
$ tox -e check
```
And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::
```
$ python setup.py clean --all sdist bdist_wheel
```
To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::
```
$ twine register dist/*
$ twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip
```
In ZSH you can use this to upload everything in ``dist/`` that ain't a linux-specific wheel (you may need ``setopt extended_glob``)::
```
$ twine upload --skip-existing dist/*.(whl|gz|zip)~dist/*linux*.whl
```
