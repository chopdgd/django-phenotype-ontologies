#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-phenotype-ontologies
------------
Tests for `django-phenotype-ontologies` API.
"""

try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .fixtures import *


@pytest.mark.django_db
def setup_client(user=None):
    client = APIClient()

    if user:
        client.force_authenticate(user=user)

    return client


def test_api_permissions():
    client = setup_client()

    response = client.post(reverse('phenotype_ontologies:term-list'), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.post(reverse('phenotype_ontologies:crossreference-list'), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.put(reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.put(reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.patch(reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.patch(reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.delete(reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    response = client.delete(reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_get_terms_list(Term):
    Term(pk=999)
    client = setup_client()
    response = client.get(reverse('phenotype_ontologies:term-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json().get('results', [])) == 1

    observed_keys = list(response.json()['results'][0].keys())
    expected_keys = [
        'id',
        'ontology',
        'term',
        'label',
        'description',
        'url',
        'synonyms',
        'xrefs',
        'relationships',
        'created_by',
        'created',
        'modified',
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_terms_detail(Term):
    Term(pk=999)
    client = setup_client()
    response = client.get(reverse('phenotype_ontologies:term-detail', kwargs={'pk': 999}), format='json')
    assert response.status_code == status.HTTP_200_OK

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'ontology',
        'term',
        'label',
        'description',
        'url',
        'synonyms',
        'xrefs',
        'relationships',
        'created_by',
        'created',
        'modified',
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_xrefs_list(CrossReference):
    CrossReference(pk=999)
    client = setup_client()
    response = client.get(reverse('phenotype_ontologies:crossreference-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json().get('results', [])) == 1

    observed_keys = list(response.json()['results'][0].keys())
    expected_keys = [
        'id',
        'term',
        'source',
        'source_value',
        'created',
        'modified',
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_xrefs_detail(CrossReference):
    CrossReference(pk=999)
    client = setup_client()
    response = client.get(reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 999}), format='json')
    assert response.status_code == status.HTTP_200_OK

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'term',
        'source',
        'source_value',
        'created',
        'modified',
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0
