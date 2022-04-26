######
Codemy
######

Codemy is a discord bot for an idle-RPG style game relating to the profession
of coding.

***************
Running Locally
***************

Running Codemy locally lets you debug and test the bot's functionality before
integrating code changes into the repository.

=============
Prerequisites
=============

To run Codemy locally, you will need to have the following prerequisites
installed:

* `Git`_
* `Python`_ (>3.10)
* `Poetry`_

  * ``Poetry`` is a dependency management and packaging tool for Python,
    similar in functionality to ``npm`` or ``yarn`` for JavaScript.

All other dependencies will be installed in a virtual environment when
running Poetry.

.. note::
  If this is your first time using ``Poetry``, consider changing the config
  to create virtual environments in the project's root directory by running::

    $ poetry config virtualenvs.in-project true


============
Installation
============

Installing Codemy is relatively straight-forward.

----------------
Cloning the Repo
----------------

First, you must clone this repository to your local machine.

If you have an SSH key setup for GitHub, clone the repo using SSH::

  $ git clone git@github.com:Septem151/Codemy.git

Alternatively, clone the repo using HTTPS::

  $ git clone https://github.com/Septem151/Codemy.git

-----------------------
Installing Dependencies
-----------------------

``Poetry`` will manage all project dependencies and the virtual environment.

To install dependencies and create the virtual environment, run::

  $ poetry install

=================
Environment Setup
=================

It's recommended to use Visual Studio Code for this project. To maintain
consistent styling, formatting, and linting, the ``.vscode/settings.json``
file will utilize some `extensions`_:

* **Python** by Microsoft
* **Pylance** by Microsoft
* **Prettier - Code formatter** by Prettier

These extensions will provide opinionated auto-formatting on save,
and linting for finding errors quickly.

================
Helpful Commands
================

Here are some helpful commands to run before submitting Pull Requests:

* format all python files: ``poetry run black .``
* sort all import statements: ``poetry run isort .``
* check for any type errors: ``poetry run mypy .``
* checks for any code errors: ``poetry run pylint codemy/ tests/``
* run tests: ``poetry run pytest``

=========
Licensing
=========

All code in this repository is licensed under `GPLv2`_.


.. _Git: https://git-scm.com/downloads
.. _Python: https://www.python.org/downloads/
.. _Poetry: https://python-poetry.org/docs/
.. _extensions: https://code.visualstudio.com/docs/editor/extension-marketplace
.. _GPLv2: ./LICENSE
