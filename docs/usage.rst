=====
Usage
=====

To use Django Phenotype Ontologies in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'phenotype_ontologies.apps.PhenotypeOntologiesConfig',
        ...
    )

Add Django Phenotype Ontologies's URL patterns:

.. code-block:: python

    from phenotype_ontologies import urls as phenotype_ontologies_urls


    urlpatterns = [
        ...
        url(r'^', include(phenotype_ontologies_urls)),
        ...
    ]
