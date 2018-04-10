#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-phenotype-ontologies
------------
Tests for `django-phenotype-ontologies` urls module.
"""

from django.urls import reverse, resolve

from test_plus.test import TestCase

from . import fixtures


class TestTermURLs(TestCase):
    """Test URL patterns for HPO Terms."""

    def setUp(self):
        self.instance = fixtures.Term()

    def test_list_reverse(self):
        """phenotype_ontologies:term-list should reverse to /phenotype-terms/."""
        self.assertEqual(reverse('phenotype_ontologies:term-list'), '/phenotype-terms/')

    def test_list_resolve(self):
        """/phenotype-terms/ should resolve to phenotype_ontologies:term-list."""
        self.assertEqual(resolve('/phenotype-terms/').view_name, 'phenotype_ontologies:term-list')

    def test_detail_reverse(self):
        """phenotype_ontologies:term-detail should reverse to /phenotype-terms/1/."""
        self.assertEqual(
            reverse('phenotype_ontologies:term-detail', kwargs={'pk': 1}),
            '/phenotype-terms/1/'
        )

    def test_detail_resolve(self):
        """/phenotype-terms/1/ should resolve to phenotype_ontologies:term-detail."""
        self.assertEqual(resolve('/phenotype-terms/1/').view_name, 'phenotype_ontologies:term-detail')


class TestCrossReferenceURLs(TestCase):
    """Test URL patterns for HPO Term Cross References."""

    def setUp(self):
        self.instance = fixtures.CrossReference()

    def test_list_reverse(self):
        """phenotype_ontologies:crossreference-list should reverse to /phenotype-xrefs/."""
        self.assertEqual(reverse('phenotype_ontologies:crossreference-list'), '/phenotype-xrefs/')

    def test_list_resolve(self):
        """/phenotype-xrefs/ should resolve to phenotype_ontologies:crossreference-list."""
        self.assertEqual(resolve('/phenotype-xrefs/').view_name, 'phenotype_ontologies:crossreference-list')

    def test_detail_reverse(self):
        """phenotype_ontologies:crossreference-detail should reverse to /phenotype-xrefs/1/."""
        self.assertEqual(
            reverse('phenotype_ontologies:crossreference-detail', kwargs={'pk': 1}),
            '/phenotype-xrefs/1/'
        )

    def test_detail_resolve(self):
        """/phenotype-xrefs/1/ should resolve to phenotype_ontologies:crossreference-detail."""
        self.assertEqual(resolve('/phenotype-xrefs/1/').view_name, 'phenotype_ontologies:crossreference-detail')
