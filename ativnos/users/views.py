from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.views.generic.edit import FormView

from invitations.views import SendInvite
from ativnos.helpers.views import R400Mixin

from .forms import CaptchaInviteForm


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return self.request.user.get_absolute_url()


class CaptchaSendInvite(R400Mixin, SendInvite):
    template_name = 'users/invite.html'
    form_class = CaptchaInviteForm