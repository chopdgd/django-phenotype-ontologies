# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('phenotype_ontologies.urls', namespace='phenotype_ontologies')),
    url(r'^admin/', admin.site.urls),
]
