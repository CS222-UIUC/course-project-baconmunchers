from django.db import models

# Create your models here.

class ClassInfo(models.Model):
    # CourseNumber = models.CharField(max_length=10)   
    # # CS 225
    # Name = models.CharField(max_length=100)           
    # # Data Structures
    CRN = models.IntegerField()        
    # 31208
    # Type = models.CharField(max_length=20)           
    # # Lecture
    # Section = models.CharField(max_length=10)        
    # # AL1

    StartTime = models.CharField(max_length=10)
    # 11:00 AM
    EndTime = models.CharField(max_length=10)
    # 11:00AM - 11:50AM, might be worth to make it a timefield or datetimefield
    Room = models.CharField(max_length=10)
    # THEAT
    Building = models.CharField(max_length=30)
    Days = models.CharField(max_length=10)
    # MWF
    

    
