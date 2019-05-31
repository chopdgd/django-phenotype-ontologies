#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-phenotype-ontologies management command sync
------------
Tests for `django-phenotype-ontologies` sync command.
"""

from django.core.management import call_command

import mock
import pytest

from phenotype_ontologies import models
import pronto


@pytest.mark.django_db
@mock.patch.object(pronto, 'Ontology')
def test_sync(ontology_mock):
    # Mock pronto.Ontology
    # Mock term synonmys
    synonym_mock_attrs = {
        'desc': 'desc',
        'scope': 'EXACT',
    }
    synonym_term_mock = mock.Mock()
    synonym_term_mock.configure_mock(**synonym_mock_attrs)

    synonyms_mock_attrs = {
        '__iter__': mock.Mock(return_value=iter([synonym_term_mock]))
    }
    synonyms_mock = mock.Mock()
    synonyms_mock.configure_mock(**synonyms_mock_attrs)

    # Mock Term itself
    relation_mock_attrs = {
        'id': 'HP:0000002',
        'name': 'name2',
        'desc': 'desc2',
        'other': {
            'created_by': ['created_by'],
            'creation_date': ['1987-12-18'],
            'alt_id': ['HP:0000004'],
        },
        'synonyms': synonyms_mock,
        'relations': {},
    }
    relation_mock = mock.Mock()
    relation_mock.configure_mock(**relation_mock_attrs)

    term_mock_attrs = {
        'id': 'HP:0000001',
        'name': 'name',
        'desc': 'desc',
        'other': {
            'created_by': ['created_by'],
            'creation_date': ['1987-12-18'],
            'alt_id': ['HP:0000002'],
            'xref': [
                'shouldbeskipped',
                'UMLS:1',
            ],
        },
        'synonyms': synonyms_mock,
        'relations': {
            "Relationship('is_a')": [relation_mock],
            "Relationship('can_be')": [relation_mock],
        },
    }
    term_mock = mock.Mock()
    term_mock.configure_mock(**term_mock_attrs)

    # Mock Ontology
    ontology_attrs = {
        'meta': {'data-version': ['test']},
        '__iter__': mock.Mock(return_value=iter([term_mock, relation_mock])),
    }
    ontology_return_mock = mock.Mock()
    ontology_return_mock.configure_mock(**ontology_attrs)
    ontology_mock.return_value = ontology_return_mock

    call_command('sync_ontology', ontology='MONDO')

    # Check version is created correctly
    ontology_obj = models.Ontology.objects.get(label='test')
    assert ontology_obj.id == 1

    # Check that Term is created correctly
    term_objects = models.Term.objects.all()
    term_object = models.Term.objects.get(pk=1)
    assert len(term_objects) == 2
    assert str(term_object.ontology) == 'MONDO test'
    assert term_object.identifier == '0000001'
    assert term_object.label == 'name'
    assert term_object.description == 'desc'
    assert term_object.created_by == 'created_by'
    assert term_object.created == '1987-12-18'
    assert term_object.alternate_ids == '0000002'

    # Check that Synonym is created correctly
    term_synonym_objects = models.Synonym.objects.all()
    term_synonym_object = models.Synonym.objects.get(term=term_object)
    assert len(term_synonym_objects) == 1
    assert term_synonym_object.description == 'desc'
    assert term_synonym_object.get_scope_display() == 'EXACT'

    # Check that CrossReference is created correctly
    term_xref_objects = models.CrossReference.objects.all()
    term_xref_object = models.CrossReference.objects.get(term=term_object)
    assert len(term_xref_objects) == 1
    assert term_xref_object.source == 'UMLS'
    assert term_xref_object.source_value == '1'

    # Check that Relationship is created correctly
    relationship_objects = models.Relationship.objects.all()
    assert len(relationship_objects) == 2

    is_a_object = models.Relationship.objects.get(type__label='is_a')
    assert str(is_a_object.type) == 'is_a'
    assert str(is_a_object.term) == 'MONDO:0000001'
    assert str(is_a_object.related_term) == 'MONDO:0000002'

    can_be_object = models.Relationship.objects.get(type__label='can_be')
    assert str(can_be_object.type) == 'can_be'
    assert str(can_be_object.term) == 'MONDO:0000001'
    assert str(can_be_object.related_term) == 'MONDO:0000002'
