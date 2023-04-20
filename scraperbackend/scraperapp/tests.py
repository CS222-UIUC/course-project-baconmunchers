from django.test import TestCase
from .forms import ClassForm
from .models import ClassInfo
# Create your tests here.

class ClassInfoTestCase(TestCase):
    """Test Case for usage of the ClassInfo model"""

    def setUp(self):
        """Class Info initialization for a sample database"""
        ClassInfo.objects.create(
            SubjectCode="CS", 
            CourseNumber="124", 
            CRN="74481",
            StartTime="10:00AM",
            EndTime="10:50AM",
            Days="T",
            Building="Campus Instructional Facility",
            Room="4029")
        ClassInfo.objects.create(
            SubjectCode="CS", 
            CourseNumber="128", 
            CRN="74479",
            StartTime="09:30AM",
            EndTime="10:45AM",
            Days="F",
            Building="Campus Instructional Facility",
            Room="1035")

    def test_get_different(self):
        """Test for queries of different values"""
        cs124 = ClassInfo.objects.get(CourseNumber="124")
        cs128 = ClassInfo.objects.get(CourseNumber="128")
        self.assertNotEqual(cs124, cs128)
    
    def test_get_same(self):
        """Test for query of a value not in the database"""
        cs124_1 = ClassInfo.objects.get(Room="4029")
        cs124_2 = ClassInfo.objects.get(CourseNumber="124")