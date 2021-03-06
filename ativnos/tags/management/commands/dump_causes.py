from django.core.management.base import BaseCommand

from ativnos.tags.models import Cause
from ._common import DumpMixin


class Command(DumpMixin, BaseCommand):
    model = Cause
