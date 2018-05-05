from django.urls import path

from . import views

app_name = "profiles"
urlpatterns = [
    path('', views.ProfileListView.as_view(), name='list'),
    path('update/', views.ProfileUpdateView.as_view(), name='update'),
    path('cause/<int:pk>', views.CauseUpsertView.as_view(), name='upsert-cause'),
    path('skill/<int:pk>', views.SkillUpsertView.as_view(), name='upsert-skill'),
    path('cause/<int:pk>/delete', views.CauseDeleteView.as_view(), name='delete-cause'),
    path('skill/<int:pk>/delete', views.SkillDeleteView.as_view(), name='delete-skill'),
]
