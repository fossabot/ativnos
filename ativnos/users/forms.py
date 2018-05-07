from captcha.fields import ReCaptchaField

from invitations.forms import InviteForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import DISPLAY_NAME_LENGTH




class ExtraSignUpForm(forms.Form):
    name = forms.CharField(
        max_length=DISPLAY_NAME_LENGTH, label=_('Display Name'))

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()


class CaptchaInviteForm(InviteForm):
    captcha = ReCaptchaField()
