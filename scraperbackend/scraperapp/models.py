from django.db import models

# Create your models here.

class ClassInfo(models.Model):
    CourseNumber = models.CharField(max_length=10)   
    # CS 225
    Name = models.CharField(max_length=100)           
    # Data Structures
    CRN = models.IntegerField()        
    # 31208
    Type = models.CharField(max_length=20)           
    # Lecture
    Section = models.CharField(max_length=10)        
    # AL1
    Time = models.CharField(max_length=20)           
    # 11:00AM - 11:50AM, might be worth to make it a timefield or datetimefield
    Day = models.CharField(max_length=10)
    # MWF
    Location = models.CharField(max_length=30)
    # THEAT Lincoln Hall

