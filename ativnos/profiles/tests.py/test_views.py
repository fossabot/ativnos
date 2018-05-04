from django.test import TestCase, RequestFactory
from django.urls import reverse

from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory

from ativnos.profiles import views


class ProfileDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.view = views.ProfileDetailView.as_view()
        self.resource = reverse('profile', kwargs={'pk': self.user.pk})
        self.factory = RequestFactory()

    def test_get(self):
        res = self.view(self.factory.get(self.resource), pk=self.user.pk)
        self.assertEqual(res.status_code, 200)
    

class ProfileUpdateViewTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.view = views.ProfileUpdateView.as_view()
        self.resource = reverse('profiles:update')
        self.factory = RequestFactory()

    def test_get(self):
        req = self.factory.get(self.resource)
        req.user = self.user
        res = self.view(req)
        self.assertEqual(res.status_code, 200)


class TagUpsertMixin():
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


class SkillUpsertViewTestCase(TagUpsertMixin, TestCase):
    tag_factory = SkillFactory
    view_class = views.SkillUpsertView


class CauseUpsertViewTestCase(TagUpsertMixin, TestCase):
    tag_factory = CauseFactory
    view_class = views.CauseUpsertView


class TagDeleteMixin():
    def setUp(self):
        self.user_tag = self.user_tag_factory()
        self.view = self.view_class.as_view()
        self.resource = reverse('profiles:upsert-cause', kwargs={'pk': self.user_tag.tag.pk})
        self.factory = RequestFactory()
    
    def test_post(self):
        pass
