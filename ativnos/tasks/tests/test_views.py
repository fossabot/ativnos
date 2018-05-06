from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from ativnos.helpers.testing import DetailViewMixin, ListViewMixin, get, post
from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.tasks import views
from ativnos.tasks.models import Task
from ativnos.tasks.tests.factories import TaskFactory
from ativnos.users.tests.factories import UserFactory


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
    view_class = views.TaskDeleteView
    url_name = 'tasks:delete'

    def setUp(self):
        self.task = TaskFactory()
        self.view = self.view_class.as_view()
        self.resource = reverse(self.url_name, kwargs={'pk': self.task.pk})

    @parameterized.expand([
        (
            "task owner",
            lambda x: x.user,
            True,
        ),
        (
            "other user",
            lambda x: UserFactory(),
            False,
        ),
        (
            "non user",
            lambda x: AnonymousUser(),
            False,
        ),
    ])
    def test_post(self, name, get_user, authorized):
        """
        Only creating user can delete task.
        other users are unauthorized
        non users are unauthorized
        """
        req = post(self.resource)
        req.user = get_user(self.task)
        if authorized:
            res = self.view(req, pk=self.task.pk)
            self.assertEqual(res.status_code, 302)
        else:
            self.assertRaises(
                PermissionDenied, self.view, req, pk=self.task.pk)

        self.assertNotEqual(
            Task.objects.filter(pk=self.task.pk).exists(), authorized)
