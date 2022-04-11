************************
 Continuous integration
************************

Continuous integration is practice of automating integration code from multiple contributors
but also could be use to simplify maintain own code.

Main benefits of CI usage:

* test on every push to repository
* test if a contribution does not break existing functionality
* simple testing against multiple version of environment (for example different package versions, python interpreter, etc)

Most often continuous integration providers uses yaml files for define steps to be done:

* Gitlab https://docs.gitlab.com/ee/ci/, https://docs.gitlab.com/ee/ci/yaml/, https://docs.github.com/en/actions/guides/building-and-testing-python
* Github https://docs.github.com/en/actions/guides/about-continuous-integration, https://docs.github.com/en/actions/guides/building-and-testing-python

Gitlab provides repository with templates for most of languages:
https://gitlab.com/gitlab-org/gitlab-foss/tree/master/lib/gitlab/ci/templates

Github has templates build in interface.


pre-commit
##########

pre-commit (https://pre-commit.com/) is tool for manage hooks executed before commit action.
Its store configuration inside ``.pre-commit-config.yaml`` file. It could be used to keep codebase quality better.
List of hooks is available here: https://pre-commit.com/hooks.html.

To use pre-commit for current project execute the following commands:

.. code-block:: bash

    $ pip install pre-commit
    $ pre-commit install
    $ pre-commit run --all

Short description of most interesting hooks from this project:

* ``black`` – code formatter
* ``flake8`` – statistical code analyser
* ``pyupgrade`` – use modern syntax of python
* ``isort`` – sort import order to satisfy pep8 requirements

pre-commit could be also used in CI as check of code quality. For example using


.. code-block:: bash

    $ pre-commit run --all --show-diff-on-failure

Its also provide own CI service which will create autofix commits https://pre-commit.ci/

tox
###

``tox`` is a tool for simplify testing using separated environment. https://tox.readthedocs.io/en/latest/
Testing environments are created inside ``.tox`` directory. For speedup test execution tox create environment only if
it is missed. So if you change dependencies of package then you may need to delete ``.tox`` directory. Simple ``tox.ini``
file is attached in this repository. It defines test environment for python 3.8 and 3.9.
To select specific environment to be executed flag ``-e`` may be used. For example:

.. code-block:: bash

    $ tox -e py38


Exercise 1
**********

Modify CI configuration to execute test also for python 3.9.

Exercise 2
**********
Base on documentation disable bundle step for non master branch:
https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idif
https://docs.gitlab.com/ee/ci/yaml/#onlyexcept-basic
