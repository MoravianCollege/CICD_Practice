# CICD_Practice

In regards to the project structure, see this quote from Dr. Coleman:

> Tests should be in tests/ and source should be in src. This allows us to separate production code from test code, but it also causes problems with import statements. We place our code in a package and install it as editable to address the import problem.



**Developer Setup**

1. Create a virtual environment: 
  * Run `python3 -m venv .venv` to set up the virtual environment
  * Then run `source .venv/bin/activate` to start up the virtual environment
* Install the required libraries with 
`pip3 install -r requirements`
* Install the project's source code as an editable package with 
`pip3 install -e .`

You should now be able to run `pytest` from the root of the project or `/tests/`

**Continuous Integration Setup**

The file `.travis.yml` tells Travis-CI to install the requirements and then execute pytest.

The following file allows us to use Travis-CI for a Python 3.7 project.
The `xenial` line is just to get Travis-CI to work with Python 3.7.
We use `install` to tell Travis-CI what to install and then `script` get Travis-CI to run `pytest`.

```
dist: xenial
language: python
python: 3.7
install:
- pip install -r requirements.txt
- python setup.py install
script: pytest
```

