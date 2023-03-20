from django import forms

class ClassForm(forms.Form):
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
    Building = forms.CharField(label="Building", required=False) 
    # would probably be ideal to replace this with a drop-down list of the buildings
    Room = forms.CharField(label="Room", required=False, )
    # would probably be ideal to have this pop up depending on the building that was entered