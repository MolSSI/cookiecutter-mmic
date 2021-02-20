# Cookiecutter for Computational Molecular Sciences (CMS) Python Packages
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/Andrew-AbiMansour/cookiecutter-mmic/workflows/Pseudo%20Validate%20GHA%20Output/badge.svg)](https://github.com/Andrew-AbiMansour/cookiecutter-mmic/actions?query=workflow%3A%22Pseudo+Validate+GHA+Output%22)


A [cookiecutter](https://github.com/audreyr/cookiecutter) template for MMSChema translators
written in Python. Based on the CMS cookiecutter. 

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features
included here. Just to name a few things you can alter to suit your needs: change continuous integration options,
remove deployment platforms, or test with a different suite.

## Features
* Python-centric skeletal structure with initial module files
* Pre-configured `setup.py` for installation and packaging
* Pre-configured Windows, Linux, and OSX continuous integration on GitHub Actions.
* Choice of dependency locations through `conda-forge`, default `conda`, or `pip`
* Basic testing structure with [PyTest](https://docs.pytest.org/en/latest/)
* Automatic `git` initialization + tag
* GitHub Hooks
* Automatic package version control with [Versioneer](https://github.com/warner/python-versioneer)
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by [Sphinx](http://www.sphinx-doc.org/en/master/)
* Automatic license file inclusion from several common Open Source licenses (optional)

## Requirements

* Python 3.7, 3.8, or 3.9
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)
* [Git](https://git-scm.com/)

## Usage

With [`cookiecutter` installed](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter),
execute the following command inside the folder you want to create the skeletal repository.

```bash
cookiecutter gh:andrew-abimansour/cookiecutter-mmschema
```

Which fetches this repository from github automatically and prompts the user for some simple information such as
package name, author(s), and licences.


## Acknowledgments

The MMSchema cookitercutter is based on the CMS cookiecutter developed by Levi N. Naden and Jessica A. Nash
from the [Molecular Sciences Software Institute (MolSSI)](http://molssi.org/); and
Daniel G. A. Smith of [ENTOS](https://www.entos.ai/). Copyright (c) 2021.

Elements of this repository drawn from the
[cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) by Driven Data
and the [MolSSI Python Template](https://github.com/MolSSI/python_template)
