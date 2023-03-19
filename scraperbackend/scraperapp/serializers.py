from rest_framework import serializers
from .models import ClassInfo# , ClassQuery

class ClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = ('CRN', 'StartTime', 'EndTime', 'Days', 'Building', 'Room',)

"""
class ClassQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassQuery
        fields = ('id', 'CRN', 'StartTime', 'EndTime', 'Days', 'Building', 'Room',)


"""
