from django.test import TestCase

from ativnos.helpers.testing import ListViewMixin
from ativnos.tags.tests.factories import SkillFactory, CauseFactory

from ativnos.tags import views


class CauseListViewTestCase(ListViewMixin, TestCase):
    object_factory = CauseFactory
    view_class = views.CauseListView
    url_name = 'tags:causes'


class SkillListViewTestCase(ListViewMixin, TestCase):
    object_factory = SkillFactory
    view_class = views.CauseListView
    url_name = 'tags:skills'