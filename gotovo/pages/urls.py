from django.urls import path

from .views import HomePageView, delete_task, profile_image_select, street, shop, tasking, CentralStreet, rating, shopi, create_task, task_list, task_details, view_task, completed_tasks


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
    path('shopi', shopi, name="shopi"),
    path('create_task', create_task, name="create_task"),
    path('task_list/', task_list, name='task_list'),
    path('view_task/<int:task_id>/', task_details, name='view_task'),
    path('task_details/<int:task_id>/details/', view_task, name='task_details'),
    path('completed_tasks', completed_tasks, name='completed_tasks'),
]
