# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('phenotype_ontologies.urls', namespace='phenotype_ontologies')),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
