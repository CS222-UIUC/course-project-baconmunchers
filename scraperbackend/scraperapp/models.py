from django.db import models

# Create your models here.

class ClassInfo(models.Model):
    # CourseNumber = models.CharField(max_length=10)   
    # # CS 225
    # Name = models.CharField(max_length=100)           
    # # Data Structures
    CRN = models.CharField(max_length=10)        
    # 31208
    # Type = models.CharField(max_length=20)           
    # # Lecture
    # Section = models.CharField(max_length=10)        
    # # AL1

    StartTime = models.CharField(max_length=10)
    # 11:00 AM
    EndTime = models.CharField(max_length=10)
    # 11:00AM - 11:50AM, might be worth to make it a timefield or datetimefield
    
    Days = models.CharField(max_length=10)
    # MWF
    
    Building = models.CharField(max_length=30)
    
    Room = models.CharField(max_length=10)
    # THEAT
    
    
class ClassQuery(models.Model):
    CRN = models.IntegerField()
    StartTime = models.TimeField(null=True, blank=True)
    EndTime = models.TimeField(null=True, blank =True)
    
    Days = models.CharField(max_length=10, null=True, blank=True)
    Building = models.CharField(max_length=30, null=True, blank=True)
    Room = models.CharField(max_length=10, null=True, blank=True)

    
