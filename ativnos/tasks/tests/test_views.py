from django.test import TestCase, RequestFactory
from django.urls import reverse

from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory

from ativnos.tasks import views

