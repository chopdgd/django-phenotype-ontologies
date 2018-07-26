# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


ONTOLOGY = Choices(
    (1, 'HP', _('HP')),  # http://purl.obolibrary.org/obo/hp.obo
    (2, 'MONDO', _('MONDO')),  # http://purl.obolibrary.org/obo/mondo.obo
    (3, 'ONCOTREE', _('ONCOTREE')),  # http://purl.obolibrary.org/obo/ncit/ncit-oncotree.owl
)


SYNONYM_SCOPES = Choices(
    (1, 'EXACT', _('EXACT')),
    (2, 'BROAD', _('BROAD')),
    (3, 'NARROW', _('NARROW')),
    (4, 'RELATED', _('RELATED')),
    (5, 'ABBREVATION', _('ABBREVATION')),
)
