# -*- coding: utf-8 -*-
from model_mommy import mommy
import pytest


@pytest.fixture
def Ontology():

    return mommy.make(
        'phenotype_ontologies.Ontology',
        type=1,
        label='Ontology',
        active=True,
    )


@pytest.fixture
def Term():

    return mommy.make(
        'phenotype_ontologies.Term',
        ontology=Ontology(),
        identifier='identifier',
        label='Term',
        description='Term',
        alternate_ids='1,2',
        created_by='created_by',
        created='created',
    )


@pytest.fixture
def Synonym():

    return mommy.make(
        'phenotype_ontologies.Synonym',
        term=Term(),
        description='Synonym',
        scope=1,
    )


@pytest.fixture
def CrossReference():

    return mommy.make(
        'phenotype_ontologies.CrossReference',
        term=Term(),
        source=1,
        source_value='source_value',
    )


@pytest.fixture
def Relationship():

    return mommy.make(
        'phenotype_ontologies.Relationship',
        type=RelationshipType(),
        term=Term(),
    )


@pytest.fixture
def RelationshipType():

    return mommy.make(
        'phenotype_ontologies.RelationshipType',
        label='RelationshipType'
    )
