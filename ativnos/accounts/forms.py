from allauth.account.forms import ResetPasswordForm
from captcha.fields import ReCaptchaField


class CaptchaResetPasswordForm(ResetPasswordForm):
    captcha = ReCaptchaField()