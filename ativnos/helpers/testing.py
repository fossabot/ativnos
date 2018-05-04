"""
Helper functions and classes for tests. They should only be used in tests.
"""

from django.test import RequestFactory
from django.urls import reverse

get = RequestFactory().get

post = RequestFactory().post


class DetailViewMixin():
    """
    a mixin for testing DetailView descendants

    Attributes:
        url_name (str): name of url used by `reverse`
        object_factory (DjangoModelFactory): factory to generate object displayed in view
        view_class (View): django View class. Usually a DetailView
    """
    def setUp(self):
        self.object = self.object_factory()
        self.view = self.view_class.as_view()
        self.resource = reverse(self.url_name, kwargs={'pk': self.object.pk})        

    def test_get(self):
        res = self.view(get(self.resource), pk=self.object.pk)
        self.assertEqual(res.status_code, 200)


class ListViewMixin():
    """
    a mixin for testing ListView descendants

    Attributes:
        url_name (str): name of url used by `reverse`
        object_factory (DjangoModelFactory): factory to generate object displayed in view
        view_class (View): django View class. Usually a ListView
    """
    def setUp(self):
        self.object = self.object_factory()
        self.view = self.view_class.as_view()
        self.resource = reverse(self.url_name)

    def test_get(self):
        res = self.view(get(self.resource))
        self.assertEqual(res.status_code, 200)
