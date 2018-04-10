# -*- coding: utf-8 -*-
from django.db.models import CharField, TextField

import django_filters
from genomix.filters import DisplayChoiceFilter

from . import choices, models


class TermFilter(django_filters.rest_framework.FilterSet):

    ontology__type = DisplayChoiceFilter(choices=choices.ONTOLOGY)

    ontology = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Ontology.objects.all(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    synonyms = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Synonym.objects.fast(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    xrefs = django_filters.ModelMultipleChoiceFilter(
        queryset=models.CrossReference.objects.fast(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    relationships = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Relationship.objects.fast(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    relationships__related_term = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Term.objects.fast(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.Term
        fields = [
            'ontology',
            'ontology__type',
            'ontology__label',
            'identifier',
            'label',
            'description',
            'synonyms',
            'synonyms__description',
            'xrefs',
            'xrefs__source',
            'xrefs__source_value',
            'relationships',
            'relationships__type__label',
            'relationships__related_term',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
            TextField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }


class CrossReferenceFilter(django_filters.rest_framework.FilterSet):

    term = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Term.objects.fast(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.CrossReference
        fields = [
            'term',
            'source',
            'source_value',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            }
        }
