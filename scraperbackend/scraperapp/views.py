from rest_framework import viewsets
from .serializers import ClassInfoSerializer
from .models import ClassInfo
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class ClassInfoView(viewsets.ModelViewSet):
    serializer_class = ClassInfoSerializer
    queryset = ClassInfo.objects.all()

def index(request):
    return HttpResponse("Hello, world. You're at the Course index.")