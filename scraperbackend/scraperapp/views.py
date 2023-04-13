from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ClassInfoSerializer# , ClassQuerySerializer
from .models import ClassInfo# , ClassQuery
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClassForm
from .forms import BuildingForm
from datetime import datetime
from dal import autocomplete
from dal_select2.views import Select2ListView
raw_buildings = ['', '1010 W Nevada', '1203 1/2 W Nevada', '1205 W Nevada', '1205 W Oregon', '1207 W Oregon', '1208 W Nevada', '614 E. Daniel', '901 W Oregon', '907 1/2 W Nevada', 'ACES Lib, Info & Alum Ctr', 'Activities & Recreation Center', 'Agricultural Engr Sciences Bld', 'Allen Residence Hall', 'Altgeld Hall', 'Animal Sciences Laboratory', 'Architecture Annex', 'Architecture Building', 'Armory', 'Art and Design Building', 'Astronomy Building', 'Beckman Institute', 'Bevier Hall', 'Burrill Hall', 'Business Instructional Fac', 'Campbell Hall', 'Campus Instructional Facility', 'Campus Recreation Center East', 'Ceramics Building', 'Ceramics Kiln House', 'Chemical and Life Sci Lab', 'Chemistry Annex', 'Chicago IL', 'Child Development Laboratory', 'Christopher Hall', 'Civil Eng Hydrosystems Lab', 'Dance Studio', 'Danville IL', 'Davenport Hall', 'David Kinley Hall', 'Digital Computer Laboratory', 'Discovery Partners Inst. CHI', 'Education Building', 'Electrical & Computer Eng Bldg', 'Engineering Hall', 'Engineering Sciences Building', 'English Building', 'Everitt Laboratory', 'Expanded Child Dev Lab', 'FAR Meeting Space', 'Flagg Hall', 'Foellinger Auditorium', 'Foreign Languages Building', 'Freer Hall', 'GYM Campus Recreation Center East', 'Grad Sch of Lib & Info Science', 'Grainger Engineering Library', 'Gregory Hall', 'Harding Band Building', 'Henry Administration Bldg', 'Huff Hall', 'Ice Arena', 'Illini Center', 'Illini Union', 'Illinois Street Residence Lng', 'Inst Labor &  Industrial Rel', 'Institute for Genomic Biology', 'Japan House', 'Krannert Art Museum', 'Krannert Center for Perf Arts', 'LAB Art-East Annex, Studio 2', 'Law Building', 'Library', 'Lincoln Hall', 'Loomis Laboratory', 'Materials Science & Eng Bld', 'Meat Science Laboratory', 'Mechanical Engineering Lab', 'Medical Sciences Building', 'Micro & Nanotechnology Lab', 'Mumford Hall', 'Music Building', 'National Soybean Res Ctr', 'Natural History Building', 'Newmark Civil Engineering Bldg', 'Noble Hall', 'Noyes Laboratory', 'Outdoor Space', 'Pennsylvania Lounge Bld - PAR', 'Plant Sciences Laboratory', 'Psychology Building', 'Richmond Studio', 'Roger Adams Laboratory', 'Seitz Materials Research Lab', 'Sidney Lu Mech Engr Bldg', 'Siebel Center for Comp Sci', 'Siebel Center for Design', 'Smith Memorial Hall', 'South Farms', 'Speech & Hearing Science Bldg', 'Spurlock Museum', 'Stock Pavilion', 'Student Dining & Res Program', 'Talbot Laboratory', 'Temple Hoyne Buell Hall', 'Transportation Building', 'Turner Hall', 'Vet Med Basic Sciences Bldg', 'Veterinary Teaching Hospital', 'Weston Hall', 'Wohlers Hall']
BUILDINGS= [(building, building) for building in raw_buildings]




class ClassInfoView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassInfoSerializer
    queryset = ClassInfo.objects.all()





def get_class(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClassForm(request.POST)
        if form.is_valid():
            # print(set(list(ClassInfo.objects.values_list('Building', flat=True))))
            SubjectCode = form.cleaned_data['SubjectCode']
            CourseNumber = form.cleaned_data['CourseNumber']
            CRN = form.cleaned_data['CRN']
            StartTime = form.cleaned_data['StartTime']
            EndTime = form.cleaned_data['EndTime']
            Days = form.cleaned_data['Days'] 
            Building = form.cleaned_data['Building'] 
            Room = form.cleaned_data['Room']
            info = ClassInfo.objects.all()
            # print(CRN, StartTime, EndTime, Days, Building, Room)
            if SubjectCode != "":
                info = info.filter(SubjectCode__icontains=SubjectCode)
            if CourseNumber != None:
                info = info.filter(CourseNumber__icontains=str(CourseNumber))
            if CRN != None:
                info = info.filter(CRN__icontains=str(CRN))
                # could change the database parsing to store CRN as an integer
#TODO Decide on logic for when a course should be filtered based on start and end time,
# Ex: if the start time entered is after the start time and before the end time of a class, should it be included 
            if StartTime != "":
                info = info.filter(StartTime__icontains=StartTime)
            if EndTime != "":
                info = info.filter(EndTime__icontains=EndTime)
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
        # print(set(list(ClassInfo.objects.values_list('Building', flat=True))))
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
        if StartTime != "":
            info = info.filter(StartTime__icontains=StartTime)
        if EndTime != "":
            info = info.filter(EndTime__icontains=EndTime)
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