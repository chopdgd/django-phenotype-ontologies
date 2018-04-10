# -*- coding: utf-8
from django.contrib import admin

from . import models


class OntologyAdmin(admin.ModelAdmin):
    model = models.Ontology
    list_display = ('type', 'label', 'created', 'modified')
    search_fields = ('label', )
    save_as = True


class TermAdmin(admin.ModelAdmin):
    model = models.Term
    list_display = ('ontology', 'term', 'label', 'created_by', 'created', 'modified')
    raw_id_fields = ('ontology', )
    search_fields = ('ontology__label', 'identifier', 'label', 'description', 'synonyms__description')
    save_as = True


class SynonymAdmin(admin.ModelAdmin):
    model = models.Synonym
    list_display = ('term', 'scope', 'created', 'modified')
    raw_id_fields = ('term', )
    list_filter = ('scope', )
    search_fields = ('description', )
    save_as = True


class CrossReferenceAdmin(admin.ModelAdmin):
    model = models.CrossReference
    list_display = ('term', 'source', 'source_value', 'created', 'modified')
    raw_id_fields = ('term', )
    list_filter = ('source', )
    search_fields = ('source', 'source_value', )
    save_as = True


class RelationshipAdmin(admin.ModelAdmin):
    model = models.Relationship
    list_display = ('type', 'term', 'related_term', 'created', 'modified')
    raw_id_fields = ('type', 'term', 'related_term')
    list_filter = ('type', )
    search_fields = (
        'term__label',
        'term__description',
        'term__synonyms__description',
        'related_term__label',
        'related_term__description',
        'related_term__synonyms__description'
    )
    save_as = True


class RelationshipTypeAdmin(admin.ModelAdmin):
    model = models.RelationshipType
    list_display = ('label', 'created', 'modified')
    search_fields = ('label', )
    save_as = True


admin.site.register(models.Ontology, OntologyAdmin)
admin.site.register(models.Term, TermAdmin)
admin.site.register(models.Synonym, SynonymAdmin)
admin.site.register(models.CrossReference, CrossReferenceAdmin)
admin.site.register(models.Relationship, RelationshipAdmin)
admin.site.register(models.RelationshipType, RelationshipTypeAdmin)
