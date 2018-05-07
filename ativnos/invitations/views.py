from invitations.views import SendInvite

from ativnos.helpers.views import R400Mixin


class CaptchaSendInvite(R400Mixin, SendInvite):
    template_name = 'invitations/invite.html'
