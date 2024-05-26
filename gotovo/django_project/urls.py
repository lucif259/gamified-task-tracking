from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from accounts.views import rating_view, rating
from pages import views
from pages.views import  create_task


urlpatterns = [
  path("admin", admin.site.urls),
  path("accounts/", include("allauth.urls")),
  path("", include("pages.urls")),
  path('rating/', rating_view, name='rating'),
  path('rating/', rating, name='rating'),
  path('create_task/', views.create_task, name='create_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


