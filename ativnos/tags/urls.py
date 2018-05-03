from django.urls import path

from . import views

app_name = "tags"
urlpatterns = [
    path('causes/', view=views.CauseListView.as_view(), name='causes'),
    path('skills/', view=views.SkillsListView.as_view(), name='skills'),
]
