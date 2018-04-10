# -*- coding: utf-8 -*-
from rest_framework import routers

from . import viewsets


app_name = 'phenotype_ontologies'
router = routers.SimpleRouter()
router.register(r'phenotype-terms', viewsets.TermViewSet)
router.register(r'phenotype-xrefs', viewsets.CrossReferenceViewSet)

default_router = routers.DefaultRouter()
default_router.register(r'phenotype-terms', viewsets.TermViewSet)
default_router.register(r'phenotype-xrefs', viewsets.CrossReferenceViewSet)


urlpatterns = default_router.urls
