from django.conf.urls import url

from invitations import views
from .views import CaptchaSendInvite

app_name = 'invitations'
urlpatterns = [
    url(r'^send-invite/$', CaptchaSendInvite.as_view(),
        name='send-invite'),

    url(r'^accept-invite/(?P<key>\w+)/?$', views.AcceptInvite.as_view(),
        name='accept-invite'),
]