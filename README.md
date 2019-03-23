## spike to validate the way of using resources in python

[![Build Status](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python.svg?branch=master)](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python)

the goal of this spike is to be able to copy
a file packaged in the application inside the
working directory of the user.

## references

* [Alice in Python projectland](http://veekaybee.github.io/2017/09/26/python-packaging/)

    the python packaging introduction I would have dreamed to write.

* [Python Packaging User Guide](https://packaging.python.org/)

    the source of truth for python packaging written by the Python Packaging Authority.

## step 1 : setup the environment

```bash
git clone https://github.com/FabienArcellier/spike-python-deploy-files-with-command.git
cd spike-python-deploy-files-with-command
make venv
make install_requirements_dev


venv/bin/python -m mycommand.cli command1 --name fabien
```

## step 2 : package a resource file with MANIFEST in source distribution

in MANIFEST.in, reference the directory `mycommand/resources/*`.

```
make dist
```

2.1 - check `configuration.json` is present in the source distribution artefact `dist/mycommand-1.0.0.tar.gz`

## step 3 : package the application in wheel

The packaging through `bdist_wheel` does not contain `configuration.json`.

```bash
venv/bin/python setup.py bdist_wheel
```

`MANIFEST.in` is not supported in python3. The way to package
data resource is to use the attribute `package_data` from `setup.py`.

We will use `setup.py` to reference our configuration.json file.

```python
setup(
    # ...
    include_package_data=True,
    package_data={
        'configuration': ['mycommand/resources/configuration.json'],
    }
)
```

* [Python Packaging User Guide - Packaging and distributing projects - package_data](https://packaging.python.org/guides/distributing-packages-using-setuptools/?highlight=package_data#package-data)
* [Building and Distributing Packages with Setuptools - including data files](https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files)

## step 4 : copy configuration.json in the working directory

## Usage

You can run the application with the following command

```bash
python -m mycommand.cli command1 --name fabien

# inside a virtualenv or after installation with pip
mycommand command1 --name fabien
```

## Developper guideline

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

