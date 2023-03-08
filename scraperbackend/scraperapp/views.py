from rest_framework import viewsets
from .serializers import ClassInfoSerializer
from .models import ClassInfo
from django.shortcuts import render

# Create your views here.

class ClassInfoView(viewsets.ModelViewSet):
    serializer_class = ClassInfoSerializer
    queryset = ClassInfo.objects.all()
