from django.conf import settings


HPO_PURL = getattr(
    settings,
    'HPO_PURL',
    'http://purl.obolibrary.org/obo/hp.obo'
)


MONDO_PURL = getattr(
    settings,
    'MONDO_PURL',
    'http://purl.obolibrary.org/obo/mondo.obo'
)


NCIT_PURL = getattr(
    settings,
    'NCIT_PURL',
    'http://purl.obolibrary.org/obo/ncit/ncit-oncotree.obo'
)
