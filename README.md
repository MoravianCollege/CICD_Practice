# CICD_Practice

In regards to the project structure, see this quote from Dr. Coleman:

> Tests should be in tests/ and source should be in src. This allows us to separate production code from test code, but it also causes problems with import statements. We place our code in a package and install it as editable to address the import problem.



**Developer Setup**

* Create a virtual environment: 
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

**Continuous Deployment Setup**

* First we must clone the production repo, not a fork, so that Travis-CI will be deploying the correct repo.
* Create an SSH key: `ssh-keygen -b 4096 -C 'build@travis-ci.com' -f ./deploy_rsa`
* Place the public key on the server's authorized users directory.
* Encrypt the private key: `travis encrypt-file deploy_rsa --org --add`
This will use the travis-ci.com endpoint and add the appropriate line to the `.travis.yml` file. Replacing the `--pro` flag with `--org` will use the travis-ci.org endpoint.
* Edit the `.travis.yml` and change `before_install` to `before_deploy`. The generated version makes the file available during testing, which isn't necessary - and is a security risk.
* Add `deploy_rsa.enc` and the edited version of `.travis.yml` to the repo. NOT `deploy_rsa`, which is the unencrypted version!!!
* Change the IP in `ssh_known_hosts` and `script`, and edit the path in `script`; both should match the server setup.
* Finally, add `deploy.sh` to the repo so that Travis-CI can deploy the project

```
addons:
  ssh_known_hosts:
  - 18.219.192.252
before_deploy:
- openssl aes-256-cbc -K $encrypted_49099c38b3b5_key -iv $encrypted_49099c38b3b5_iv -in deploy_rsa.enc -out deploy_rsa -d
- chmod 600 deploy_rsa
deploy:
  provider: script
  skip_cleanup: true
  script: ssh -i deploy_rsa ubuntu@18.219.192.252 'source /home/ubuntu/CICD_Practice/deploy.sh'
```
