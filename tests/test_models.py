#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-phenotype-ontologies
------------

Tests for `django-phenotype-ontologies` models module.
"""
import pytest

from .fixtures import *  # NOQA


@pytest.mark.django_db
def test_Term(Term, Ontology):
    hpo_term = Term(ontology=Ontology(type=1), identifier='001')
    assert str(hpo_term) == 'HP:001'
    assert hpo_term.source == 'HP'
    assert hpo_term.term == 'HP:001'
    assert hpo_term.url == 'http://compbio.charite.de/hpoweb/showterm?id=HP:001'

    mondo_term = Term(ontology=Ontology(type=2), identifier='002')
    assert str(mondo_term) == 'MONDO:002'
    assert mondo_term.source == 'MONDO'
    assert mondo_term.term == 'MONDO:002'
    assert mondo_term.url == 'https://monarchinitiative.org/disease/MONDO:002'

    ncit_term = Term(ontology=Ontology(type=3), identifier='003')
    assert str(ncit_term) == 'NCIT:003'
    assert ncit_term.source == 'ONCOTREE'
    assert ncit_term.term == 'NCIT:003'
    assert ncit_term.url == 'http://purl.obolibrary.org/obo/NCIT_003'


@pytest.mark.django_db
def test_Synonym(Synonym):
    instance = Synonym()
    assert str(instance) == 'HP:Term'


@pytest.mark.django_db
def test_CrossReference(CrossReference):
    instance = CrossReference()
    assert str(instance) == 'HP:Term'


@pytest.mark.django_db
def test_RelationshipType(RelationshipType):
    instance = RelationshipType(label='RelationshipType')
    assert str(instance) == 'RelationshipType'


@pytest.mark.django_db
def test_Relationship(Relationship):
    instance = Relationship()
    assert str(instance) == 'HP:Term'
