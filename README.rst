=============================
Django Phenotype Ontologies
=============================

.. image:: https://badge.fury.io/py/django-phenotype-ontologies.svg
    :target: https://badge.fury.io/py/django-phenotype-ontologies

.. image:: https://travis-ci.org/genomics-geek/django-phenotype-ontologies.svg?branch=develop
    :target: https://travis-ci.org/genomics-geek/django-phenotype-ontologies

.. image:: https://codecov.io/gh/genomics-geek/django-phenotype-ontologies/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/genomics-geek/django-phenotype-ontologies

.. image:: https://pyup.io/repos/github/genomics-geek/django-phenotype-ontologies/shield.svg
     :target: https://pyup.io/repos/github/genomics-geek/django-phenotype-ontologies/
     :alt: Updates

.. image:: https://pyup.io/repos/github/genomics-geek/django-phenotype-ontologies/python-3-shield.svg
      :target: https://pyup.io/repos/github/genomics-geek/django-phenotype-ontologies/
      :alt: Python 3

Django app to parse/load phenotype ontologies (OncoTree, HPO, MONDO, etc)

Documentation
-------------

The full documentation is at https://django-phenotype-ontologies.readthedocs.io.

Quickstart
----------

Install Django Phenotype Ontologies::

    pip install django-phenotype-ontologies

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'phenotype_ontologies',
        ...
    )

Add Django Phenotype Ontologies's URL patterns:

.. code-block:: python

    from phenotype_ontologies import urls as phenotype_ontologies_urls


    urlpatterns = [
        ...
        url(r'^', include(phenotype_ontologies_urls, namespace='phenotype_ontologies')),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
