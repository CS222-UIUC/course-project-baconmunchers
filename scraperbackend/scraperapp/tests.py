from django.test import TestCase
from .forms import ClassForm, BuildingForm
from .models import ClassInfo   
from django.test import Client
from http import HTTPStatus

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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
        ClassInfo.objects.create(
            SubjectCode="CS", 
            CourseNumber="222", 
            CRN="71617",
            StartTime="01:00PM",
            EndTime="01:50PM",
            Days="W",
            Building="Electrical & Computer Eng Bldg",
            Room="1002")

    def test_get_different(self):
        """Test for queries of different values"""
        cs124 = ClassInfo.objects.get(CourseNumber="124")
        cs128 = ClassInfo.objects.get(CourseNumber="128")
        self.assertNotEqual(cs124, cs128)
    
    def test_get_same(self):
        """Test for queries of the same course in different ways"""
        cs124_1 = ClassInfo.objects.get(Room="4029")
        cs124_2 = ClassInfo.objects.get(CourseNumber="124")
    
    def test_doesnt_exist(self):
        """Test for query of a value not in the database"""
        self.assertRaises(ClassInfo.DoesNotExist, ClassInfo.objects.get, CourseNumber="173")
    
    def test_query_multiple(self):
        """Tests queries for multiple courses at once"""
        query = ClassInfo.objects.filter(Building="Campus Instructional Facility")
        self.assertEqual(len(query), 2)
        query = ClassInfo.objects.filter(SubjectCode="CS")
        self.assertEqual(len(query), 3)
        
class TestPages(TestCase):
    
    def test_building_exists(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/get_building/")
        driver.find_element(By.ID, 'id_Building').send_keys('Campus Instructional Facility')
        driver.find_element(By.ID, 'id_Building').submit()
        assert "Building page doesn't exist yet. Try Advanced Search!" not in driver.page_source
        driver.close()

    def test_building_doesnt_exist(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/get_building/")
        driver.find_element(By.ID, 'id_Building').send_keys('asdf')
        driver.find_element(By.ID, 'id_Building').submit()
        assert "Building page doesn't exist yet. Try Advanced Search!" in driver.page_source
        driver.close()
    

    def test_courses_exist(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/get_class/")
        driver.find_element(By.ID, 'id_SubjectCode').send_keys('CS')
        driver.find_element(By.ID, 'id_CourseNumber').send_keys('222')
        driver.find_element(By.ID, 'id_CourseNumber').submit()
        assert "No classes found. Are you sure you typed everything in correctly?" not in driver.page_source
        driver.close()

    def test_courses_dont_exist(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/get_class/")
        driver.find_element(By.ID, 'id_SubjectCode').send_keys('CS')
        driver.find_element(By.ID, 'id_CourseNumber').send_keys('223')
        driver.find_element(By.ID, 'id_CourseNumber').submit()
        assert "No classes found. Are you sure you typed everything in correctly?" in driver.page_source
        driver.close()
    
    