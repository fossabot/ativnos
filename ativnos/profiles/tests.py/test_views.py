from django.test import TestCase, RequestFactory
from django.urls import reverse

from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory

from ativnos.profiles import views


class UserProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.view = views.UserProfileView.as_view()
        self.resource = reverse('profile', kwargs={'pk': self.user.pk})
        self.factory = RequestFactory()

    def test_get(self):
        res = self.view(self.factory.get(self.resource), self.user.pk)
        self.assertEqual(res.status_code, 200)
    

class UpdateProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.view = views.UpdateProfileView.as_view()
        self.resource = reverse('profiles:update')
        self.factory = RequestFactory()

    def test_get(self):
        req = self.factory.get(self.resource)
        req.user = self.user
        res = self.view(req)
        self.assertEqual(res.status_code, 200)


class UpsertTagMixin():
    def setUp(self):
        self.tag = self.tag_factory()
        self.user = UserFactory()
        self.view = self.view_class.as_view()
        self.resource = reverse('profiles:upsert-cause', kwargs={'pk': self.tag.pk})
        self.factory = RequestFactory()

    def test_get(self):
        req = self.factory.get(self.resource)
        req.user = self.user
        res = self.view(req, self.tag.pk)
        self.assertEqual(res.status_code, 200)


class UpsertSkillTestCase(UpsertTagMixin, TestCase):
    tag_factory = SkillFactory
    view_class = views.UpsertSkill


class UpsertCauseTestCase(UpsertTagMixin, TestCase):
    tag_factory = CauseFactory
    view_class = views.UpsertCause
