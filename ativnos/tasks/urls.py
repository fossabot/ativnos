from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path('<int:pk>/', views.TaskView.as_view(), name="detail"),
]