"""Django's application configuration object for storing metadata for an app"""

from django.apps import AppConfig

"""Application configuration object with metadata for scraperapp"""
class ScraperappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraperapp'
