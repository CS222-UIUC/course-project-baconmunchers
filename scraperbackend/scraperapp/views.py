from rest_framework import viewsets
from .serializers import ClassInfoSerializer, ClassQuerySerializer
from .models import ClassInfo, ClassQuery
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class ClassInfoView(viewsets.ModelViewSet):
    serializer_class = ClassInfoSerializer
    queryset = ClassInfo.objects.all()


class ClassQueryView(viewsets.ModelViewSet):
    serializer_class = ClassQuerySerializer
    queryset = ClassQuery.objects.all() # .filter()

def index(request):
    return HttpResponse("Hello, world. You're at the Course index.")