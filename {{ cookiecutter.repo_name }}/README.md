{{  cookiecutter.project_name }}
========

{{ cookiecutter.project_short_description }}

# Installation

## Pre-Requisites

Following pre-requisites are needed before installation:

- python 2.7

## Run Code

After the pre-requisites are installed, clone this repository using git and move into the repository by running: 

```bash
cd {{ cookiecutter.repo_name }}
```

Then to run the code run following commands:

```bash
sudo docker build  -t {{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}:{{ cookiecutter.version }} .
sudo docker run --rm {{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}:{{ cookiecutter.version }}
```