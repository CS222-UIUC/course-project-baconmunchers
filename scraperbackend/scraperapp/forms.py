from django import forms
raw_buildings = ['Wohlers Hall', 'Gregory Hall', 'Child Development Laboratory', 'English Building', 'Flagg Hall', 'Ice Arena', 'Henry Administration Bldg', 'Roger Adams Laboratory', 'Turner Hall', 'Huff Hall', 'Architecture Annex', 'Speech & Hearing Science Bldg', '901 W Oregon', 'Campus Instructional Facility', 'Krannert Center for Perf Arts', 'Agricultural Engr Sciences Bld', 'Spurlock Museum', 'Digital Computer Laboratory', 'Micro & Nanotechnology Lab', 'Art and Design Building', 'Medical Sciences Building', 'Ceramics Building', 'Everitt Laboratory', 'Expanded Child Dev Lab', 'Talbot Laboratory', 'Civil Eng Hydrosystems Lab', 'Davenport Hall', 'Japan House', 'Lincoln Hall', 'Krannert Art Museum', 'Weston Hall', 'Smith Memorial Hall', 'Transportation Building', 'Newmark Civil Engineering Bldg', 'Beckman Institute', 'Temple Hoyne Buell Hall', 'Illini Center', 'Pennsylvania Lounge Bld - PAR', 'Education Building', 'Grad Sch of Lib & Info Science', 'Noble Hall', '1207 W Oregon', 'Business Instructional Fac', 'Electrical & Computer Eng Bldg', 'Inst Labor &  Industrial Rel', 'Psychology Building', 'FAR Meeting Space', 'Armory', 'Institute for Genomic Biology', 'Danville IL', '1203 1/2 W Nevada', 'Illinois Street Residence Lng', 'Grainger Engineering Library', 'Campus Recreation Center East', '1205 W Oregon', 'Activities & Recreation Center', 'David Kinley Hall', 'Allen Residence Hall', 'Illini Union', 'Outdoor Space', 'National Soybean Res Ctr', 'Harding Band Building', 'Altgeld Hall', '907 1/2 W Nevada', 'Student Dining & Res Program', 'Discovery Partners Inst. CHI', 'Library', 'Materials Science & Eng Bld', 'Chicago IL', 'Chemical and Life Sci Lab', 'ACES Lib, Info & Alum Ctr', 'Foreign Languages Building', 'Stock Pavilion', 'Mechanical Engineering Lab', 'Law Building', 'South Farms', 'Freer Hall', 'Plant Sciences Laboratory', 'Noyes Laboratory', 'Richmond Studio', 'Ceramics Kiln House', 'Sidney Lu Mech Engr Bldg', 'Mumford Hall', 'Foellinger Auditorium', 'Engineering Sciences Building', 'Siebel Center for Design', 'GYM Campus Recreation Center East', 'Natural History Building', 'Christopher Hall', 'Chemistry Annex', 'Siebel Center for Comp Sci', 'Meat Science Laboratory', '1205 W Nevada', 'Engineering Hall', 'Bevier Hall', 'Loomis Laboratory', 'Architecture Building', '614 E. Daniel', 'Burrill Hall', 'Vet Med Basic Sciences Bldg', 'LAB Art-East Annex, Studio 2', 'Music Building', '1208 W Nevada', 'Seitz Materials Research Lab', 'Animal Sciences Laboratory', 'Dance Studio', 'Campbell Hall', '1010 W Nevada', 'Veterinary Teaching Hospital', 'Astronomy Building']
raw_buildings.sort()
BUILDINGS= [(building, building) for building in raw_buildings]

class ClassForm(forms.Form):
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


class BuildingForm(forms.Form):
    Building = forms.CharField(label="Building", required=False, widget=forms.Select(choices=BUILDINGS))