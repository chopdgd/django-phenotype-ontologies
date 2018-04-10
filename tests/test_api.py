#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-hpo-terms
------------
Tests for `django-hpo-terms` API.
"""

from django.contrib.auth import get_user_model

try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from . import fixtures


class TestTermAPI(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # Create instance for GET, PUT, PATCH, DELETE Methods
        fixtures.Term()

    def test_post(self):
        """Test POST."""

        response = self.client.post(
            reverse('phenotype_ontologies:term-list'),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


    def test_get(self):
        """Test GET."""

        response = self.client.get(
            reverse('phenotype_ontologies:term-list'),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

    def test_put(self):
        """Test PUT."""

        response = self.client.put(
            reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_patch(self):
        """Test PATCH."""

        response = self.client.patch(
            reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete(self):
        """Test DELETE."""
        response = self.client.delete(
            reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


class TestCrossReferenceAPI(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # Create instance for GET, PUT, PATCH, DELETE Methods
        fixtures.Term()

    def test_post(self):
        """Test POST."""

        response = self.client.post(
            reverse('phenotype_ontologies:crossreference-list'),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


    def test_get(self):
        """Test GET."""

        response = self.client.get(
            reverse('phenotype_ontologies:crossreference-list'),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

    def test_put(self):
        """Test PUT."""

        response = self.client.put(
            reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_patch(self):
        """Test PATCH."""

        response = self.client.patch(
            reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}),
            {},
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete(self):
        """Test DELETE."""
        response = self.client.delete(
            reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
