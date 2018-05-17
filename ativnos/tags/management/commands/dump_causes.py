import json
import argparse

from django.core.management.base import BaseCommand

from ativnos.tags.models import Cause


class Command(BaseCommand):
    help = 'dump causes to json'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('w'))

    def handle(self, *args, **options):
        data = list(Cause.objects.all().values('name'))
        json.dump(data, options['file'])
