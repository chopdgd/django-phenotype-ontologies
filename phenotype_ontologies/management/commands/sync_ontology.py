# -*- coding: utf-8 -*-
import logging

from pronto import Ontology

from django.core.management import BaseCommand

from phenotype_ontologies import app_settings, choices, models


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Sync ontology from online resource'

    def add_arguments(self, parser):
        parser.add_argument(
            '--ontology',
            dest='ontology',
            choices=['HP', 'MONDO', 'ONCOTREE'],
            help='Ontology Source',
        )

    def handle(self, *args, **options):
        if options['ontology'] == 'HP':
            purl = app_settings.HPO_PURL

        elif options['ontology'] == 'MONDO':
            purl = app_settings.MONDO_PURL

        elif options['ontology'] == 'ONCOTREE':
            purl = app_settings.NCIT_PURL

        logger.info('Downloading {0}...'.format(purl))
        data = Ontology(purl, timeout=10)

        version = data.meta['data-version'][0]
        version_obj, version_created = models.Ontology.objects.get_or_create(
            type=getattr(choices.ONTOLOGY, options['ontology']),
            label=version,
        )

        if not version_created:
            logger.info('Version: {0} already available'.format(version))

        else:
            logger.info('Adding Version: {0}'.format(version))
            logger.info('Adding Terms...')

            relations = []
            for term in data:
                created_by = term.other.get('created_by', None)
                created = term.other.get('creation_date', None)
                alternate_ids = [
                    str(self.extract_id(alt_term))
                    for alt_term in term.other.get('alt_id', [])
                ]

                try:
                    term_obj = models.Term.objects.create(
                        ontology=version_obj,
                        identifier=self.extract_id(term.id),
                        label=term.name if term.name else "",
                        description=term.desc if term.desc else "",
                        created_by=created_by[0] if created_by else "",
                        created=created[0] if created else "",
                        alternate_ids=",".join(alternate_ids),
                    )
                except Exception as error:
                    msg = '{0} could not be added! Error: {1}'.format(term.id, error)
                    logger.error(msg)
                    raise Exception(msg)

                # Create Synonym objects
                for synonym in term.synonyms:
                    if synonym:
                        models.Synonym.objects.get_or_create(
                            term=term_obj,
                            description=synonym.desc if synonym.desc else "",
                            # NOTE: pronto always returns array
                            scope=getattr(choices.SYNONYM_SCOPES, synonym.scope),
                        )

                # Create Relationships objects
                for key, value in term.relations.items():
                    key = str(key).replace("Relationship('", "").replace("')", "")
                    type_obj, type_created = models.RelationshipType.objects.get_or_create(label=key)
                    for related_term in value:
                        # NOTE: We want source and id to store. There are a few records that don't conform
                        if related_term.id.startswith('https://rarediseases.info.nih.gov/diseases/'):
                            logger.warning('Relationship {0} format does not conform!'.format(related_term.id))
                        else:
                            relations.append({
                                "type": type_obj,
                                "term": term_obj,
                                # NOTE: This is to handle MONDO terms w/ source
                                "related_term": self.extract_id(related_term.id.strip().split()[0])
                            })

                # Create CrossReference objects
                for xref in term.other.get('xref', []):
                    if xref:
                        xref_data = xref.split(':', 1)

                        # NOTE: We want source and id to store. There are 3 records that don't conform
                        if len(xref_data) != 2 or xref_data[0].upper() == 'HTTP':
                            logger.warning('CrossReference: {0} format not supported!'.format(xref))

                        else:
                            models.CrossReference.objects.get_or_create(
                                term=term_obj,
                                source=xref_data[0].split()[0].upper(),
                                source_value=xref_data[1].split()[0],
                            )

            # Create is_a/can_be relationships
            logger.info('Building Relationships...')
            for relation in relations:
                try:
                    models.Relationship.objects.create(
                        type=relation['type'],
                        term=relation['term'],
                        related_term=models.Term.objects.get(
                            identifier=relation['related_term'],
                            ontology=version_obj,
                        ),
                    )
                except Exception as error:
                    logger.warning('Relationship: {0} was not added. Error: {1}'.format(relation, error))

    def extract_id(self, value):
        return value.strip().split(':')[1]
