# -*- coding: utf-8 -*-
from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.utils.translation import ugettext_lazy as _

from genomix.models import TimeStampedLabelModel
from model_utils.models import TimeStampedModel

from . import choices, managers


class Ontology(TimeStampedModel):
    """Model to keep track of Ontology and version."""

    type = models.PositiveSmallIntegerField(choices=choices.ONTOLOGY)
    label = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Ontology')
        verbose_name_plural = _('Ontology')

    def __str__(self):
        return '{0} {1}'.format(
            self.get_type_display(),
            self.label
        )


class Term(models.Model):
    """HPO Terms.
    Source: http://purl.obolibrary.org/obo/hp.obo
    """

    ontology = models.ForeignKey('phenotype_ontologies.Ontology', on_delete=models.CASCADE)
    identifier = models.CharField(max_length=25, db_index=True)
    label = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    alternate_ids = models.CharField(
        max_length=2500,
        blank=True,
        validators=[validate_comma_separated_integer_list]
    )
    created_by = models.CharField(max_length=50, blank=True)
    created = models.CharField(max_length=25, blank=True)
    modified = models.DateTimeField(auto_now=True)

    objects = managers.TermQuerySet.as_manager()

    class Meta:
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')
        index_together = [
            ['ontology', 'identifier']
        ]

    def __str__(self):
        return self.term

    @property
    def source(self):
        return self.ontology.get_type_display()

    @property
    def term(self):
        if self.source == 'MONDO':
            return '{0}:{1}'.format(
                'MONDO',
                self.identifier,
            )
        elif self.source == 'HP':
            return '{0}:{1}'.format(
                'HP',
                self.identifier,
            )
        elif self.source == 'ONCOTREE':
            return '{0}:{1}'.format(
                'NCIT',
                self.identifier,
            )

    @property
    def url(self):
        if self.source == 'MONDO':
            return 'https://monarchinitiative.org/disease/{0}'.format(self.term)
        elif self.source == 'HP':
            return 'http://compbio.charite.de/hpoweb/showterm?id={0}'.format(self.term)
        elif self.source == 'ONCOTREE':
            return 'http://purl.obolibrary.org/obo/{0}_{1}'.format(
                'NCIT',
                self.identifier,
            )


class Synonym(TimeStampedModel):
    """Synonms for HPO terms."""

    term = models.ForeignKey(
        'phenotype_ontologies.Term',
        related_name='synonyms',
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True)
    scope = models.PositiveSmallIntegerField(choices=choices.SYNONYM_SCOPES, blank=True, null=True)

    objects = managers.SynonymQuerySet.as_manager()

    class Meta:
        verbose_name = _('Synonym')
        verbose_name_plural = _('Synonyms')

    def __str__(self):
        return str(self.term)


class CrossReference(TimeStampedModel):
    """XRefs for HPO terms."""

    term = models.ForeignKey(
        'phenotype_ontologies.Term',
        related_name='xrefs',
        on_delete=models.CASCADE,
    )
    source = models.CharField(max_length=25, db_index=True)
    source_value = models.CharField(max_length=255)

    objects = managers.CrossReferenceQuerySet.as_manager()

    class Meta:
        verbose_name = _('Cross Reference')
        verbose_name_plural = _('Cross References')

    def __str__(self):
        return str(self.term)


class Relationship(TimeStampedModel):
    """Relationship for HPO terms."""

    type = models.ForeignKey(
        'phenotype_ontologies.RelationshipType',
        related_name='relationships',
        on_delete=models.CASCADE,
    )
    term = models.ForeignKey(
        'phenotype_ontologies.Term',
        related_name='relationships',
        on_delete=models.CASCADE,
    )
    related_term = models.ForeignKey(
        'phenotype_ontologies.Term',
        related_name='relationships_related',
        on_delete=models.CASCADE,
    )

    objects = managers.RelationshipQuerySet.as_manager()

    class Meta:
        verbose_name = _('Relationship')
        verbose_name_plural = _('Relationships')

    def __str__(self):
        return str(self.term)


class RelationshipType(TimeStampedLabelModel):

    class Meta:
        verbose_name = _('Relationship Types')
        verbose_name_plural = _('Relationship Types')
