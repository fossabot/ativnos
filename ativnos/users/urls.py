from django.urls import path, re_path

from . import views

app_name = "users"
urlpatterns = [
    re_path(
        r"^~redirect/$",
        view=views.UserRedirectView.as_view(),
        name="redirect"),
]
