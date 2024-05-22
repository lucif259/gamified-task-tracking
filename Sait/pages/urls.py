from django.urls import path

from .views import HomePageView, delete_task, profile_image_select, street

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tasks/<int:id>/", delete_task),
    path('profile_image_select', profile_image_select, name="profile"),
    path('street', street, name="street"),
]
