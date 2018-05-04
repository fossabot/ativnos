from django.test import TestCase
from django.urls import reverse

from ativnos.helpers.testing import DetailViewMixin, ListViewMixin, get
from ativnos.tasks.tests.factories import TaskFactory
from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory

from ativnos.tasks import views


class TaskDetailViewTestCase(DetailViewMixin, TestCase):
    object_factory = TaskFactory
    view_class = views.TaskDetailView
    url_name = 'tasks:detail'
    

class TaskListViewTestCase(ListViewMixin, TestCase):
    object_factory = TaskFactory
    view_class = views.TaskListView
    url_name = 'tasks:list'


class TaskCreateViewTestCase(TestCase):
    view_class = views.TaskCreateView
    url_name = 'tasks:create'
    
    def setUp(self):
        self.view = self.view_class.as_view()
        self.resource = reverse(self.url_name)
        
        self.user = UserFactory()
        self.cause = CauseFactory()
        self.skill = SkillFactory()

    def test_get(self):
        req = get(self.resource)
        req.user = self.user
        res = self.view(req)
        self.assertEqual(res.status_code, 200)
        
    
class TaskDeleteViewTestCase(TestCase):
    pass