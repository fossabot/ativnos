from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from ativnos.helpers.testing import DetailViewMixin, get, post
from ativnos.profiles import views
from ativnos.profiles.models import UserCause, UserSkill
from ativnos.profiles.tests.factories import UserCauseFactory, UserSkillFactory
from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory


class ProfileDetailViewTestCase(TestCase):
    url_name = 'profile'
    view_class = views.ProfileDetailView

    def setUp(self):
        self.view = self.view_class.as_view()

    @parameterized.expand([(
        "other user public profile",
        UserFactory,
        lambda: UserFactory(is_public=True),
        True,
    ), (
        "non user public profile",
        AnonymousUser,
        lambda: UserFactory(is_public=True),
        True,
    ), (
        "other user non-public profile",
        UserFactory,
        lambda: UserFactory(is_public=False),
        True,
    ), (
        "non user non-public profile",
        AnonymousUser,
        lambda: UserFactory(is_public=False),
        False,
    )])
    def test_get(self, name, get_user, get_profile_user, authorized):
        profile = get_profile_user()
        resource = reverse('profile', kwargs={'pk': profile.pk})
        req = get(resource, user=get_user())
        res = self.view(req, pk=profile.pk)
        if authorized:
            self.assertEqual(res.status_code, 200)
        else:
            self.assertEqual(res.status_code, 302)


class ProfileUpdateViewTestCase(TestCase):
    def setUp(self):
        self.view = views.ProfileUpdateView.as_view()
        self.resource = reverse('profiles:update')

    @parameterized.expand([
        (
            "user",
            UserFactory,
            True,
        ),
        (
            "non user public profile",
            AnonymousUser,
            False,
        ),
    ])
    def test_get(self, name, get_user, authorized):
        req = get(self.resource, user=get_user())
        res = self.view(req)
        if authorized:
            self.assertEqual(res.status_code, 200)
        else:
            self.assertEqual(res.status_code, 302)


class TagUpsertMixin():
    def setUp(self):
        self.tag = self.tag_factory()
        self.user = UserFactory()
        self.view = self.view_class.as_view()
        self.resource = reverse(self.url_name, kwargs={'pk': self.tag.pk})

    def test_get(self):
        req = get(self.resource)
        req.user = self.user
        res = self.view(req, pk=self.tag.pk)
        self.assertEqual(res.status_code, 200)


class CauseUpsertViewTestCase(TagUpsertMixin, TestCase):
    url_name = 'profiles:upsert-cause'
    tag_factory = CauseFactory
    view_class = views.CauseUpsertView


class SkillUpsertViewTestCase(TagUpsertMixin, TestCase):
    url_name = 'profiles:upsert-skill'
    tag_factory = SkillFactory
    view_class = views.SkillUpsertView


class TagDeleteMixin():
    def setUp(self):
        self.user_tag = self.user_tag_factory()
        self.view = self.view_class.as_view()
        self.resource = reverse(
            self.url_name, kwargs={'pk': self.user_tag.tag.pk})

    def test_post(self):
        req = post(self.resource)
        req.user = self.user_tag.user
        res = self.view(req, pk=self.user_tag.tag.pk)
        self.assertFalse(
            self.model.objects.filter(
                user=self.user_tag.user, tag=self.user_tag.tag).exists())
        self.assertEqual(res.status_code, 302)


class CauseDeleteViewTestCase(TagDeleteMixin, TestCase):
    url_name = 'profiles:delete-cause'
    view_class = views.CauseDeleteView
    user_tag_factory = UserCauseFactory
    model = UserCause


class SkillDeleteViewTestCase(TagDeleteMixin, TestCase):
    url_name = 'profiles:delete-skill'
    view_class = views.SkillDeleteView
    user_tag_factory = UserSkillFactory
    model = UserSkill
