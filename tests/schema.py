from graphene import Field, Node, ObjectType, Schema
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from phenotype_ontologies import choices, models, schema as phenotype_ontologies_schema


# NOTE: We need to subclass Filter in combination with register above
from django.db.models import CharField

import django_filters
from genomix.filters import DisplayChoiceFilter


class OntologyFilter(django_filters.rest_framework.FilterSet):

    type = DisplayChoiceFilter(choices=choices.ONTOLOGY)

    class Meta:
        model = models.Ontology
        fields = '__all__'


class Query(ObjectType):

    phenotype_ontology = Node.Field(phenotype_ontologies_schema.OntologyNode)
    all_phenotype_ontologies = DjangoFilterConnectionField(
        phenotype_ontologies_schema.OntologyNode,
        filterset_class=OntologyFilter,
    )

    debug = Field(DjangoDebug, name='__debug')


schema = Schema(query=Query)
