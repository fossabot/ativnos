from django.conf.urls import url

from . import views

app_name = "tags"
urlpatterns = [
    url(regex=r"^causes/$", view=views.CauseListView.as_view(), name="causes"),
    url(regex=r"^skills/$", view=views.SkillsListView.as_view(), name="causes"),
]
