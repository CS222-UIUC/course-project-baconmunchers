from django.urls import path, re_path, reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('get_class/', views.get_class, name='get_class'),
    path('get_building/', views.get_building, name='get_building'),
    path('', views.main_page_redirect, name='main_page_redirect'),
]

urlpatterns += staticfiles_urlpatterns()