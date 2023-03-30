from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('get_class/', views.get_class, name='get_class'),

    
]

urlpatterns += staticfiles_urlpatterns()