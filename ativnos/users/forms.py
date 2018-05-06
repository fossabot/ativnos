from captcha.fields import ReCaptchaField
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import DISPLAY_NAME_LENGTH

# from allauth.account.forms import ResetPasswordForm


class ExtraSignUpForm(forms.Form):
    name = forms.CharField(
        max_length=DISPLAY_NAME_LENGTH, label=_('Display Name'))

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()


class CaptchaResetPasswordForm(forms.Form):
    captcha = ReCaptchaField()
