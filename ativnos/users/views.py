from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return self.request.user.get_absolute_url()