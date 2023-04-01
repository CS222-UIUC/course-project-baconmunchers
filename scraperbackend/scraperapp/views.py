from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClassInfoSerializer# , ClassQuerySerializer
from .models import ClassInfo# , ClassQuery
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClassForm
from .forms import BuildingForm
from datetime import datetime
# Create your views here.

class ClassInfoView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassInfoSerializer
    queryset = ClassInfo.objects.all()

"""
class ClassQueryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassQuerySerializer
    queryset = ClassQuery.objects.all() # .filter()
"""



def get_class(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassForm(request.POST)
        if form.is_valid():
            print(set(list(ClassInfo.objects.values_list('Building', flat=True))))
            SubjectCode = form.cleaned_data['SubjectCode']
            CourseNumber = form.cleaned_data['CourseNumber']
            CRN = form.cleaned_data['CRN']
            StartTime = form.cleaned_data['StartTime']
            EndTime = form.cleaned_data['EndTime']
            Days = form.cleaned_data['Days'] 
            Building = form.cleaned_data['Building'] 
            Room = form.cleaned_data['Room']
            info = ClassInfo.objects.all()
            print(CRN, StartTime, EndTime, Days, Building, Room)
            if SubjectCode != "":
                info = info.filter(SubjectCode__icontains=SubjectCode)
            if CourseNumber != None:
                info = info.filter(CourseNumber__icontains=str(CourseNumber))
            if CRN != None:
                info = info.filter(CRN__icontains=str(CRN))
                # could change the database parsing to store CRN as an integer
#TODO Decide on logic for when a course should be filtered based on start and end time,
# Ex: if the start time entered is after the start time and before the end time of a class, should it be included 
            if StartTime != None:
                info = info.filter(StartTime__icontains=StartTime.strftime('%I:%M'))
            if EndTime != None:
                info = info.filter(EndTime__icontains=EndTime.strftime('%I:%M'))
            if Days != "":
                for Day in Days:
                    info = info.filter(Days__icontains=Day)
            if Building != "":
                info = info.filter(Building__icontains=Building)
            if Room != "":
                info = info.filter(Room__icontains=Room)

            return render(request, 'classes.html', {'info': info})

            
        # should add a 404 exception if the form is invalid
    else:
        form = ClassForm()

    # get_class.html is a template, stored in the templates directory
    return render(request, 'get_class.html', {'form': form})


def building_page(request):
    form = ClassForm(request.POST)
    if form.is_valid():
        print(set(list(ClassInfo.objects.values_list('Building', flat=True))))
        SubjectCode = form.cleaned_data['SubjectCode']
        CourseNumber = form.cleaned_data['CourseNumber']
        CRN = form.cleaned_data['CRN']
        StartTime = form.cleaned_data['StartTime']
        EndTime = form.cleaned_data['EndTime']
        Days = form.cleaned_data['Days'] 
        Building = form.cleaned_data['Building'] 
        Room = form.cleaned_data['Room']
        info = ClassInfo.objects.all()
        print(CRN, StartTime, EndTime, Days, Building, Room)
        if SubjectCode != "":
            info = info.filter(SubjectCode__icontains=SubjectCode)
        if CourseNumber != None:
            info = info.filter(CourseNumber__icontains=str(CourseNumber))
        if CRN != None:
            info = info.filter(CRN__icontains=str(CRN))
            # could change the database parsing to store CRN as an integer
#TODO Decide on logic for when a course should be filtered based on start and end time,
# Ex: if the start time entered is after the start time and before the end time of a class, should it be included 
        if StartTime != None:
            info = info.filter(StartTime__icontains=StartTime.strftime('%I:%M'))
        if EndTime != None:
            info = info.filter(EndTime__icontains=EndTime.strftime('%I:%M'))
        if Days != "":
            for Day in Days:
                info = info.filter(Days__icontains=Day)
        if Building != "":
            info = info.filter(Building__icontains=Building)
        if Room != "":
            info = info.filter(Room__icontains=Room)

        return render(request, 'classes.html', {'info': info})
    return render(request, 'get_building.html', {'form': BuildingForm()})


def main_map_page(request):
    form = BuildingForm(request.POST)
    print('form made')
    if form.is_valid():
        print('form valid')
        Building = form.cleaned_data['Building'] 
        html = f'{Building}.html'
        return render(request, html, {'form': ClassForm()})
    return render(request, 'get_building.html', {'form': BuildingForm()})


def get_building(request):
    print(request)
    if request.method == 'POST' and len(request.POST) == 2:
        return main_map_page(request)
    if request.method == 'POST' and len(request.POST) > 2:
        return building_page(request)
    return render(request, 'get_building.html', {'form': BuildingForm()})

def main_page_redirect(request):
    return redirect('/get_building/')