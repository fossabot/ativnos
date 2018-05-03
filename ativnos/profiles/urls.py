from django.urls import path

from . import views

app_name = "profiles"
urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='detail'),
    path('cause/<int:pk>', views.UpsertCause.as_view(), name='upsert-cause'),
    path('skill/<int:pk>', views.UpsertCause.as_view(), name='upsert-skill'),
    path('cause/<int:pk>/delete', views.DeleteCause.as_view(), name='delete-cause'),
    path('skill/<int:pk>/delete', views.DeleteCause.as_view(), name='delete-skill'),
]
