from django.db import models
from django.urls import reverse


class AbstractTag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def add_user_tag_url(self):
        raise NotImplementedError

    @property
    def delete_user_tag_url(self):
        raise NotImplementedError


class Cause(AbstractTag):
    @property
    def add_user_tag_url(self):
        return reverse('profiles:upsert-cause', kwargs={'pk': self.pk})

    @property
    def delete_user_tag_url(self):
        return reverse('profiles:delete-cause', kwargs={'pk': self.pk})


class Skill(AbstractTag):
    @property
    def add_user_tag_url(self):
        return reverse('profiles:upsert-skill', kwargs={'pk': self.pk})

    @property
    def delete_user_tag_url(self):
        return reverse('profiles:delete-skill', kwargs={'pk': self.pk})
