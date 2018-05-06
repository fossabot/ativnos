from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ativnos.tags.models import Cause, Skill


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(
        _("Task Title"),
        max_length=140,
        help_text=_("Describe what needs to be done."))
    description = models.TextField(
        _("Description"),
        max_length=600,
        help_text=_(
            "Explain what needs to be done. How will it help? "
            "How should people interested in helping contact you or get involved?"
        ))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        related_query_name='task')

    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.pk})
