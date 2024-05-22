from django.urls import path

from .views import HomePageView, delete_task, profile_image_select, street, shop, tasking, CentralStreet, rating


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("tasks/<int:id>/", delete_task),
    path('profile_image_select', profile_image_select, name="profile"),
    path('street', street, name="street"),
    path('shop', shop, name="shop"),
    path('tasking', tasking, name="tasking"),
    path('CentralStreet', CentralStreet, name="CentralStreet"),
    path('rating', rating, name='rating'),
    path('home', HomePageView.as_view(), name="home"),
]
