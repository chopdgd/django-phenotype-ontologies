from graphene import Node, String
from graphene_django import DjangoObjectType

from . import choices, models


class OntologyNode(DjangoObjectType):

    type = String()

    class Meta:
        model = models.Ontology
        interfaces = (Node, )

    def resolve_type(self, info):
        return choices.ONTOLOGY[self.type]


class TermNode(DjangoObjectType):

    source = String()
    term = String()
    url = String()

    class Meta:
        model = models.Term
        interfaces = (Node, )

    def resolve_source(self, info):
        return self.source

    def resolve_term(self, info):
        return self.term

    def resolve_url(self, info):
        return self.url


class SynonymNode(DjangoObjectType):

    scope = String()

    class Meta:
        model = models.Synonym
        interfaces = (Node, )

    def resolve_url(self, info):
        if self.scope:
            return choices.SYNONYM_SCOPES[self.scope]


class CrossReferenceNode(DjangoObjectType):

    class Meta:
        model = models.CrossReference
        interfaces = (Node, )


class RelationshipNode(DjangoObjectType):

    class Meta:
        model = models.Relationship
        interfaces = (Node, )


class RelationshipTypeNode(DjangoObjectType):

    class Meta:
        model = models.RelationshipType
        interfaces = (Node, )
