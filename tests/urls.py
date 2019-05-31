# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django.contrib import admin


app_name = 'phenotype_ontologies'
urlpatterns = [
    url(r'^', include('phenotype_ontologies.urls')),
    url(r'^admin/', admin.site.urls),
]
