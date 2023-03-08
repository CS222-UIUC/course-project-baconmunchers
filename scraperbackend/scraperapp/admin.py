from django.contrib import admin

# Register your models here.

from .models import ClassInfo



# Register your models here.
class ScraperAdmin(admin.ModelAdmin):
    list_display = ('CRN', 'StartTime', 'EndTime', 'Room', 'Building', 'Days')

admin.site.register(ClassInfo, ScraperAdmin)
