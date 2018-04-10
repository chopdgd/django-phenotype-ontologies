# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


from . import filters, models, serializers


class TermViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing HPO Terms."""

    queryset = models.Term.objects.fast()
    serializer_class = serializers.TermSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = filters.TermFilter
    search_fields = (
        'label',
        'description',
        'synonyms__description',
    )


class CrossReferenceViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing HPO Term Cross References."""

    queryset = models.CrossReference.objects.fast()
    serializer_class = serializers.CrossReferenceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = filters.CrossReferenceFilter
    search_fields = ('source', 'source_value', )
