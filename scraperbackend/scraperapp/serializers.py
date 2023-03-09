from rest_framework import serializers
from .models import ClassInfo, ClassQuery

class ClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = ('id', 'CRN', 'StartTime', 'EndTime', 'Room', 'Building', 'Days')

class ClassQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassQuery
        fields = ('id', 'CRN', 'StartTime', 'EndTime', 'Room', 'Building', 'Days')
