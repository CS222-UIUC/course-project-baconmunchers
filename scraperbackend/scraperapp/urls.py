from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('get_class/', views.get_class, name='get_class'),
    path('get_building/', views.get_building, name='get_building')
    
]

urlpatterns += staticfiles_urlpatterns()