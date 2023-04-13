"""Module providing models to admin site view"""
from django.contrib import admin

# Register your models here.

from .models import ClassInfo #, ClassQuery



# Register your models here.
# class ScraperAdmin(admin.ModelAdmin):
#     list_display = ('CRN', 'StartTime', 'EndTime', 'Room', 'Building', 'Days')

admin.site.register(ClassInfo)
# admin.site.register(ClassQuery)
