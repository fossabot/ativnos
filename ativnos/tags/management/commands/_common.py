import json
import argparse


class DumpMixin():
    """
    Mixin for BaseCommand

    Attributes:
        model - Model from ativnos.tags.models
    """
    @property
    def help(self):
        return f'dump {self.model._meta.verbose_name} entires from database to file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('w'))

    def handle(self, *args, **options):
        data = list(self.model.objects.all().order_by('name').values('name'))
        json.dump(data, options['file'], indent=2, sort_keys=True)


class LoadMixin():
    """
    Mixin for BaseCommand

    Attributes:
        model - Model from ativnos.tags.models
    """
    @property
    def help(self):
        return f'merge {self.model._meta.verbose_name} entires from file to database.'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        data = json.load(options['file'])
        names_in_file = {i['name'] for i in data}
        names_in_db = set(self.model.objects.all().values_list('name', flat=True))
        names_in_file_but_not_in_db = names_in_file - names_in_db
        for name in names_in_file_but_not_in_db:
            self.model.objects.create(name=name)
