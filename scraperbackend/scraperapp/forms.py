from django import forms
from django.forms import ModelForm, Textarea
from dal import autocomplete
from .models import ClassInfo

raw_buildings = ['', '1010 W Nevada', '1203 1/2 W Nevada', '1205 W Nevada', '1205 W Oregon', '1207 W Oregon', '1208 W Nevada', '614 E. Daniel', '901 W Oregon', '907 1/2 W Nevada', 'ACES Lib, Info & Alum Ctr', 'Activities & Recreation Center', 'Agricultural Engr Sciences Bld', 'Allen Residence Hall', 'Altgeld Hall', 'Animal Sciences Laboratory', 'Architecture Annex', 'Architecture Building', 'Armory', 'Art and Design Building', 'Astronomy Building', 'Beckman Institute', 'Bevier Hall', 'Burrill Hall', 'Business Instructional Fac', 'Campbell Hall', 'Campus Instructional Facility', 'Campus Recreation Center East', 'Ceramics Building', 'Ceramics Kiln House', 'Chemical and Life Sci Lab', 'Chemistry Annex', 'Chicago IL', 'Child Development Laboratory', 'Christopher Hall', 'Civil Eng Hydrosystems Lab', 'Dance Studio', 'Danville IL', 'Davenport Hall', 'David Kinley Hall', 'Digital Computer Laboratory', 'Discovery Partners Inst. CHI', 'Education Building', 'Electrical & Computer Eng Bldg', 'Engineering Hall', 'Engineering Sciences Building', 'English Building', 'Everitt Laboratory', 'Expanded Child Dev Lab', 'FAR Meeting Space', 'Flagg Hall', 'Foellinger Auditorium', 'Foreign Languages Building', 'Freer Hall', 'GYM Campus Recreation Center East', 'Grad Sch of Lib & Info Science', 'Grainger Engineering Library', 'Gregory Hall', 'Harding Band Building', 'Henry Administration Bldg', 'Huff Hall', 'Ice Arena', 'Illini Center', 'Illini Union', 'Illinois Street Residence Lng', 'Inst Labor &  Industrial Rel', 'Institute for Genomic Biology', 'Japan House', 'Krannert Art Museum', 'Krannert Center for Perf Arts', 'LAB Art-East Annex, Studio 2', 'Law Building', 'Library', 'Lincoln Hall', 'Loomis Laboratory', 'Materials Science & Eng Bld', 'Meat Science Laboratory', 'Mechanical Engineering Lab', 'Medical Sciences Building', 'Micro & Nanotechnology Lab', 'Mumford Hall', 'Music Building', 'National Soybean Res Ctr', 'Natural History Building', 'Newmark Civil Engineering Bldg', 'Noble Hall', 'Noyes Laboratory', 'Outdoor Space', 'Pennsylvania Lounge Bld - PAR', 'Plant Sciences Laboratory', 'Psychology Building', 'Richmond Studio', 'Roger Adams Laboratory', 'Seitz Materials Research Lab', 'Sidney Lu Mech Engr Bldg', 'Siebel Center for Comp Sci', 'Siebel Center for Design', 'Smith Memorial Hall', 'South Farms', 'Speech & Hearing Science Bldg', 'Spurlock Museum', 'Stock Pavilion', 'Student Dining & Res Program', 'Talbot Laboratory', 'Temple Hoyne Buell Hall', 'Transportation Building', 'Turner Hall', 'Vet Med Basic Sciences Bldg', 'Veterinary Teaching Hospital', 'Weston Hall', 'Wohlers Hall']
BUILDINGS= [(building, building) for building in raw_buildings]

class ClassForm(ModelForm): # forms.Form):
    #"""
    class Meta:
        model = ClassInfo
        fields = ('SubjectCode', 'CourseNumber', 'CRN', 'StartTime', 'EndTime', 'Days', 'Building', 'Room')
        widgets = {
            'CourseNumber': forms.NumberInput(attrs={'type': 'number'}),
            'CRN': forms.NumberInput(attrs={'type': 'number'}),
            'StartTime': forms.TimeInput(attrs={'type': 'time'}),
            'EndTime': forms.TimeInput(attrs={'type': 'time'}), 
            # 'Days':
            'Building': forms.Select(choices=BUILDINGS)
            
            # 'Room': 
        }
        labels = {
            'SubjectCode': "Subject Code", 
            'CourseNumber': "Course Number", 
            'CRN': "CRN", 
            'StartTime': "Start Time", 
            'EndTime': "End Time", 
            'Days': "Days", 
            'Building': "Building", 
            'Room': "Room"
        }
        help_texts = {
            'SubjectCode': "<br/>",
            'CourseNumber': "3-digit Course Number <br/>", 
            'CRN': "5-digit Class Code <br/>", 
            'StartTime': "<br/>", 
            'EndTime': "<br/>", 
            'Days': "Formatted like MTWRF <br/>", 
            'Building': "<br/>", 
            'Room': "<br/>"
        }
        


    """
    SubjectCode = forms.CharField(label="Subject Code", required=False, help_text="<br/>")
    CourseNumber = forms.IntegerField(   label="Course Number", required=False, 
                                        help_text="3-digit Course Number <br/>",
                                        widget=forms.NumberInput(attrs={'type': 'number'}))
    CRN = forms.IntegerField(   label="CRN", required=False, 
                                help_text="5-digit Class Code <br/>",
                                widget=forms.NumberInput(attrs={'type': 'number'}))
    StartTime = forms.TimeField(label="Start Time", required=False, 
                                help_text="<br/>",#Formatted like 09:00AM",
                                # input_formats=['%I:%M%p'],
                                widget= forms.TimeInput(attrs={'type': 'time'}))
    EndTime = forms.TimeField(  label="End Time", required=False, 
                                help_text="<br/>", #Formatted like 04:00PM", 
                                # input_formats=['%I:%M%p'],
                                widget= forms.TimeInput(attrs={'type': 'time'}))

    Days = forms.CharField(label="Days", required=False, help_text="Formatted like MTWRF <br/>")
    Building = forms.CharField(label="Building", required=False, widget=forms.Select(choices=BUILDINGS)) 
    # would probably be ideal to replace this with a drop-down list of the buildings
    Room = forms.CharField(label="Room", required=False, )
    # would probably be ideal to have this pop up depending on the building that was entered
    
    """

def get_choice_list():
    print(raw_buildings)
    return raw_buildings
class BuildingForm(forms.Form):
    # Building2 = forms.CharField(label="Building", required=False, widget=forms.Select(choices=BUILDINGS)) 
    Building = forms.CharField(label="Building", required=False, widget= forms.TextInput(attrs={'id':'building', 'class': 'building'})) 

    # forms.CharField(label="Building", required=False, widget=forms.Select(choices=BUILDINGS))