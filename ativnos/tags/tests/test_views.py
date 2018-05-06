from django.test import TestCase

from ativnos.helpers.testing import ListViewMixin
from ativnos.tags import views
from ativnos.tags.tests.factories import CauseFactory, SkillFactory


class CauseListViewTestCase(ListViewMixin, TestCase):
    object_factory = CauseFactory
    view_class = views.CauseListView
    url_name = 'tags:causes'


class SkillListViewTestCase(ListViewMixin, TestCase):
    object_factory = SkillFactory
    view_class = views.CauseListView
    url_name = 'tags:skills'
