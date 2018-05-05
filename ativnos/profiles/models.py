from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ativnos.tags.models import Cause, Skill


class AbstractUserTag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    description = models.TextField(
        _("Description"), max_length=300, blank=True,
        help_text=_(
            "Describe your involvement. How have you been involved? "
            "What have you done? What would you like to do? You may Include links."
        ))

    class Meta:
        abstract = True
        unique_together = (('user', 'tag'),)

    def __str__(self):
        return f"{self.user}: {self.tag}"


class UserCause(AbstractUserTag):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='causes', related_query_name='cause')
    tag = models.ForeignKey(Cause, on_delete=models.CASCADE)


class UserSkill(AbstractUserTag):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills', related_query_name='skill')
    tag = models.ForeignKey(Skill, on_delete=models.CASCADE)
