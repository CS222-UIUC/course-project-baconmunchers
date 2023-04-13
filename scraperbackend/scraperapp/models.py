"""Django's builtin format for generating SQL tables using classes"""
from django.db import models
# Create your models here.
"""Django model to represent classes, each field corresponds to an SQLite column"""
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
