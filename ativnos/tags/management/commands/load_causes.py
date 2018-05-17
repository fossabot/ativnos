import json
import argparse

from django.core.management.base import BaseCommand

from ativnos.tags.models import Cause


class Command(BaseCommand):
    help = 'dump causes to json'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        data = json.load(options['file'])
        names_in_file = {i['name'] for i in data}
        names_in_db = set(Cause.objects.all().values_list('name', flat=True))
        names_in_file_but_not_in_db = names_in_file - names_in_db
        for name in names_in_file_but_not_in_db:
            Cause.objects.create(name=name)
