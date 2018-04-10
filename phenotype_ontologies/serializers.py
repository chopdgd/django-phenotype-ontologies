# -*- coding: utf-8 -*-
from genomix.fields import DisplayChoiceField
from rest_framework import serializers

from . import choices, models


class SynonymSerializer(serializers.ModelSerializer):
    """Serializer for HPO Term Synonms."""

    term = serializers.StringRelatedField()
    scope = DisplayChoiceField(choices=choices.SYNONYM_SCOPES)

    class Meta:
        model = models.Term
        fields = (
            'id', 'term', 'description', 'scope',
            'created', 'modified',
        )


class CrossReferenceSerializer(serializers.ModelSerializer):
    """Serializer for HPO Term Cross References."""

    term = serializers.StringRelatedField()

    class Meta:
        model = models.CrossReference
        fields = (
            'id', 'term', 'source', 'source_value',
            'created', 'modified',
        )


class RelationshipSerializer(serializers.ModelSerializer):
    """Serializer for HPO Term Cross References."""

    type = serializers.StringRelatedField()
    term = serializers.StringRelatedField()
    related_term = serializers.StringRelatedField()

    class Meta:
        model = models.Relationship
        fields = (
            'id', 'type', 'term', 'related_term',
            'created', 'modified',
        )


class TermSerializer(serializers.ModelSerializer):
    """Serializer for HPO Terms."""

    ontology = serializers.StringRelatedField()
    synonyms = SynonymSerializer(many=True, read_only=True)
    xrefs = CrossReferenceSerializer(many=True, read_only=True)
    relationships = RelationshipSerializer(many=True, read_only=True)

    class Meta:
        model = models.Term
        fields = (
            'id', 'ontology', 'term', 'label', 'description',
            'url', 'synonyms', 'xrefs', 'relationships',
            'created_by', 'created', 'modified',
        )
