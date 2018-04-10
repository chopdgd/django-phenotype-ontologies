# -*- coding: utf-8 -*-
from django.db.models import QuerySet


class TermQuerySet(QuerySet):

    def fast(self):
        return self.select_related('ontology') \
            .prefetch_related('xrefs') \
            .prefetch_related('synonyms') \
            .prefetch_related('relationships__type') \
            .all()


class SynonymQuerySet(QuerySet):

    def fast(self):
        return self.select_related('term').all()


class CrossReferenceQuerySet(QuerySet):

    def fast(self):
        return self.select_related('term').all()


class RelationshipQuerySet(QuerySet):

    def fast(self):
        return self.select_related('type').select_related('term').all()
