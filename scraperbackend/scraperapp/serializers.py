from rest_framework import serializers
from .models import ClassInfo

class ClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = ('id', 'CRN', 'StartTime', 'EndTime', 'Room', 'Building', 'Days')
