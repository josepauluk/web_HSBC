from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('upload/', views.MultipleImages, name='upload'),
]