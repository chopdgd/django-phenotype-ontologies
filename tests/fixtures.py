# -*- coding: utf-8 -*-
from model_mommy import mommy
import pytest


@pytest.fixture
def Ontology():
    def _func(**kwargs):
        return mommy.make('phenotype_ontologies.Ontology', **kwargs)
    return _func


@pytest.fixture
def Term():
    def _func(ontology=None, **kwargs):
        if ontology is None:
            ontology = mommy.make('phenotype_ontologies.Ontology', label='Ontology')
        return mommy.make('phenotype_ontologies.Term', ontology=ontology, **kwargs)
    return _func


@pytest.fixture
def Synonym():
    def _func(term=None, **kwargs):
        if term is None:
            ontology = mommy.make('phenotype_ontologies.Ontology', type=1)
            term = mommy.make('phenotype_ontologies.Term', ontology=ontology, identifier='Term')
        return mommy.make('phenotype_ontologies.Synonym', term=term, **kwargs)
    return _func


@pytest.fixture
def CrossReference():
    def _func(term=None, **kwargs):
        if term is None:
            ontology = mommy.make('phenotype_ontologies.Ontology', type=1)
            term = mommy.make('phenotype_ontologies.Term', ontology=ontology, identifier='Term')
        return mommy.make('phenotype_ontologies.CrossReference', term=term, **kwargs)
    return _func


@pytest.fixture
def RelationshipType():
    def _func(term=None, **kwargs):
        return mommy.make('phenotype_ontologies.RelationshipType', **kwargs)
    return _func


@pytest.fixture
def Relationship():
    def _func(term=None, type=None, **kwargs):
        if term is None:
            ontology = mommy.make('phenotype_ontologies.Ontology', type=1)
            term = mommy.make('phenotype_ontologies.Term', ontology=ontology, identifier='Term')
        if type is None:
            type = mommy.make('phenotype_ontologies.RelationshipType', label='RelationshipType')
        return mommy.make('phenotype_ontologies.Relationship', term=term, type=type, **kwargs)
    return _func
