from django.urls import path

from .views import HomePageView, delete_task

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tasks/<int:id>/", delete_task),
]
