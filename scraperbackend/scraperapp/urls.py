from django.urls import path, re_path, reverse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('get_class/', views.get_class, name='get_class'),
    path('get_building/', views.get_building, name='get_building'),
    re_path(r'^get_building_v2/', views.BuildingAutoComplete.as_view(), name='get_building_v2'),

    path('', views.main_page_redirect, name='main_page_redirect'),
]

urlpatterns += staticfiles_urlpatterns()