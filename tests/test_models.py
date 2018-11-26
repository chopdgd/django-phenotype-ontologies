#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-phenotype-ontologies
------------

Tests for `django-phenotype-ontologies` models module.
"""
from django.test import TestCase

from model_mommy import mommy

from . import fixtures


class TestOntology(TestCase):

    def setUp(self):
        self.instance = fixtures.Ontology()

    def test_str(self):
        assert str(self.instance) == 'HP Ontology'


class TestTerm(TestCase):

    def setUp(self):
        self.hpo_term = mommy.make(
            'phenotype_ontologies.Term',
            ontology=mommy.make('phenotype_ontologies.Ontology', type=1),
            identifier='0001',
        )
        self.mondo_term = mommy.make(
            'phenotype_ontologies.Term',
            ontology=mommy.make('phenotype_ontologies.Ontology', type=2),
            identifier='0002'
        )

        self.ncit_term = mommy.make(
            'phenotype_ontologies.Term',
            ontology=mommy.make('phenotype_ontologies.Ontology', type=3),
            identifier='0003',
        )

    def test_str(self):
        assert str(self.hpo_term) == 'HP:0001'
        assert str(self.mondo_term) == 'MONDO:0002'
        assert str(self.ncit_term) == 'NCIT:0003'

    def test_source(self):
        assert self.hpo_term.source == 'HP'
        assert self.mondo_term.source == 'MONDO'
        assert self.ncit_term.source == 'ONCOTREE'

    def test_term(self):
        assert self.hpo_term.term == 'HP:0001'
        assert self.mondo_term.term == 'MONDO:0002'
        assert self.ncit_term.term == 'NCIT:0003'

    def test_url(self):
        assert self.hpo_term.url == 'http://compbio.charite.de/hpoweb/showterm?id=HP:0001'
        assert self.mondo_term.url == 'https://monarchinitiative.org/disease/MONDO:0002'
        assert self.ncit_term.url == 'http://purl.obolibrary.org/obo/NCIT_0003'

    def tearDown(self):
        pass


class TestSynonym(TestCase):

    def setUp(self):
        self.instance = fixtures.Synonym()

    def test_str(self):
        assert str(self.instance) == 'HP:identifier'


class TestCrossReference(TestCase):

    def setUp(self):
        self.instance = fixtures.CrossReference()

    def test_str(self):
        assert str(self.instance) == 'HP:identifier'


class TestRelationship(TestCase):

    def setUp(self):
        self.instance = fixtures.Relationship()

    def test_str(self):
        assert str(self.instance) == 'HP:identifier'


class TestRelationshipType(TestCase):

    def setUp(self):
        self.instance = fixtures.RelationshipType()

    def test_str(self):
        assert str(self.instance) == 'RelationshipType'
