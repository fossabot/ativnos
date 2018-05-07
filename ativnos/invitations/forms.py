from captcha.fields import ReCaptchaField
from invitations.forms import InviteForm


class CaptchaInviteForm(InviteForm):
    captcha = ReCaptchaField()