Testango
========

Example of test of reusable Django app

.. image:: https://travis-ci.org/openwebinars-django/testango.svg?branch=master
    :target: https://travis-ci.org/openwebinars-django/testango

.. image:: https://coveralls.io/repos/openwebinars-django/testango/badge.png
    :target: https://coveralls.io/r/openwebinars-django/testango

Install project
===============

::

    virtualenv vtestango
    source vtestango/bin/activate
    python setup.py develop

    pip install Django==1.6.3
    pip install pillow==1.7.8 # python 2
    pip install pillow==2.4.0 # python 3


Run the project
===============

You need install project before

::

    cd example
    python manage.py runserver

    And access to http://localhost:8000/testango/hello/


Executing the test
==================

You need install project before

::

    cd example
    python manage.py test testango


Executing the test with tox
===========================

You DON'T need install project before. And you executing the tests with python 2.7/3.3 and Django 1.5/1.6

::

    pip install tox
    tox


Executing the test with tox and coverage
========================================

::

    sudo pip install coveralls==0.3
    coverage erase
    tox
    coverage combine
    coverage report -m
    coverage html
    chromium-browser htmlcov/index.html  # or another browser
