import hashlib
from urllib.parse import urlencode

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

DISPLAY_NAME_LENGTH = 50


def _generate_gravatar_url(email, size=16):
    gravatar_url = 'https://www.gravatar.com/avatar/{hash}?{qs}'.format(
        hash=hashlib.md5(email.lower().encode()).hexdigest(),
        qs=urlencode({
            'd': 'mm',
            's': str(size)
        }))
    return gravatar_url


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(
        _("Display Name"),
        blank=True,
        max_length=DISPLAY_NAME_LENGTH,
        help_text=_("Name displayed to other users"))
    description = models.TextField(
        _("Description"),
        blank=True,
        max_length=700,
        help_text=_(
            "Describe yourself. What have you done? What do you want to do? "
            "Include ways to be contacted if you want to help."))

    is_public = models.BooleanField(
        _("Viewable by public internet"),
        default=False,
        help_text=_(
            "Only logged in users can view your profile and tasks by default. "
            "If enabled, anyone can view your profile and tasks."))

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

    @property
    def avatar_url_small(self):
        return _generate_gravatar_url(self.email, 16)

    @property
    def avatar_url_medium(self):
        return _generate_gravatar_url(self.email, 50)
