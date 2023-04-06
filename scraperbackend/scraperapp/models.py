from django.db import models

# Create your models here.

class ClassInfo(models.Model):
    # CourseNumber = models.CharField(max_length=10)   
    # # CS 225
    # Name = models.CharField(max_length=100)           
    # # Data Structures
    SubjectCode = models.CharField(max_length=10, blank=True)
    CourseNumber = models.CharField(max_length=5, blank=True)
    CRN = models.CharField(max_length=10, primary_key=True, blank=True)        
    # 31208
    # Type = models.CharField(max_length=20)           
    # # Lecture
    # Section = models.CharField(max_length=10)        
    # # AL1

    StartTime = models.CharField(max_length=10, blank=True)
    # 11:00 AM
    EndTime = models.CharField(max_length=10, blank=True)
    # 11:00AM - 11:50AM, might be worth to make it a timefield or datetimefield
    
    Days = models.CharField(max_length=10, blank=True)
    # MWF
    
    Building = models.CharField(max_length=30, blank=True)
    
    Room = models.CharField(max_length=10, blank=True)
    # THEAT
    
"""
class ClassQuery(models.Model):
    CRN = models.IntegerField(null=True, blank=True, help_text="5-digit class code\n")
    StartTime = models.TimeField(null=True, blank=True, help_text="In the form of 09:00AM\n")
    EndTime = models.TimeField(null=True, blank =True, help_text="In the form of 04:00PM\n")
    
    Days = models.CharField(max_length=10, null=True, blank=True, help_text="In the form of MTWRF\n")
    Building = models.CharField(max_length=30, null=True, blank=True)
    Room = models.CharField(max_length=10, null=True, blank=True)

"""

    
