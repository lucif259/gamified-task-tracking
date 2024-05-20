from django.urls import path

from .views import HomePageView, delete_task, some_page, current_task

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tasks/<int:id>/", delete_task),
    path('some_page', some_page, name='some'),
    path('some_page/<int:id>', current_task,)
]
