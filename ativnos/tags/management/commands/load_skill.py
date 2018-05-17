from django.core.management.base import BaseCommand

from ativnos.tags.models import Skill
from ._common import LoadMixin


class Command(LoadMixin, BaseCommand):
    model = Skill
