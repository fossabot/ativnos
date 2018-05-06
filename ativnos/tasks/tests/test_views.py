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


class TaskDetailViewTestCase(TestCase):
    url_name = 'tasks:detail'
    view_class = views.TaskDetailView

    def setUp(self):                
        self.view = self.view_class.as_view()        

    @parameterized.expand([        
        (
            "other user views public user's task",
            UserFactory,
            lambda : UserFactory(is_public=True),
            True,
        ),
        (
            "non user views public user's task",
            AnonymousUser,
            lambda : UserFactory(is_public=True),
            True,
        ),
        (
            "other user views non-public user's task",
            UserFactory,
            lambda : UserFactory(is_public=False),
            True,
        ),
        (
            "non user views non-public user's task",
            AnonymousUser,
            lambda : UserFactory(is_public=False),
            False,
        )        
    ])    
    def test_get(self, name, get_user, get_profile_user, authorized):
        profile = get_profile_user()
        task = TaskFactory(user=profile)
        resource = reverse(self.url_name, kwargs={'pk': task.pk})
        req = get(resource, user=get_user())
        res = self.view(req, pk=task.pk)
        if authorized:
            self.assertEqual(res.status_code, 200)
        else:
            self.assertEqual(res.status_code, 302)


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
