from django.forms import ModelForm

from .models import UserTagAbstractBase


class UserTagForm(ModelForm):
    class Meta:
        model = UserTagAbstractBase
        fields = ['description']