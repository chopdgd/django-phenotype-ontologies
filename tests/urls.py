# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from phenotype_ontologies.urls import urlpatterns as phenotype_ontologies_urls

urlpatterns = [
    url(r'^', include(phenotype_ontologies_urls, namespace='phenotype_ontologies')),
    url(r'^admin/', admin.site.urls),
]
