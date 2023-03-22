import requests
import re
from bs4 import BeautifulSoup
from scraperapp.models import ClassInfo
import json

# import mysql.connector

# from get_sections_from_class import get_sections_from_class
def get_class_links():
	course_explorer = 'https://courses.illinois.edu'
	year = '2023'
	season = 'spring'

	subjects_page_link = course_explorer + f'/schedule/{year}/{season}'
	subjects_page = requests.get(subjects_page_link)

	#Parse through the course subjects page for all subject page links
	subjects_page_soup = BeautifulSoup(subjects_page.text, 'html.parser')
	subjects_page_links = [str(i.get('href')) for i in subjects_page_soup.find_all('a')]
	subject_links_regex = re.compile(f'/schedule/{year}/{season}/.*')
	subject_links = [course_explorer + link for link in subjects_page_links if not re.match(subject_links_regex, link) is None]

	#build dictionary of subject codes to lists of class linkes
	classes = {}

	for subject_page_link in subject_links:
		subject_code = re.split(r'/', subject_page_link)[-1]
		subject_page = requests.get(subject_page_link)
		subject_page_soup = BeautifulSoup(subject_page.text, 'html.parser')
		subject_page_link = [str(i.get('href')) for i in subject_page_soup.find_all('a')]
		class_links_regex = re.compile(f'/schedule/{year}/{season}/.*/\d\d\d')
		class_links = [course_explorer + link for link in subject_page_link
							if not re.match(class_links_regex, link) is None]
		classes[subject_code] = class_links


	#write classes to CLassLinks.txt for later use
	with open("ClassLinks.txt", 'w') as file:
		file.write(f"{len(classes)}\n")
		for subject_code in classes:
			file.write(f"{subject_code} {len(classes[subject_code])}\n")
			for link in classes[subject_code]:
				file.write(f"{link}\n")

def get_sections_from_class(link):
	"""Get non-online non-asynchronous sections of a class, given course explorer url.
	Data returned as list of sections, each section formatted as [crn, start, end, day, building, room]."""

	class_page = requests.get(link)
	class_page_soup = BeautifulSoup(class_page.text, 'html.parser')
	data = class_page_soup.body.find('script', type='text/javascript').text.split('\n')[1][25:-1]

	try:
		json_data = json.loads(data)
	except:
		print(link)
		return []

	sections = []
	for section_dict in json_data:
		crn = section_dict['crn']

		# TODO: do this with regex for better efficiency?
		time_soup = BeautifulSoup(section_dict['time'], 'html.parser')
		day_soup = BeautifulSoup(section_dict['day'], 'html.parser')
		location_soup = BeautifulSoup(section_dict['location'], 'html.parser')
		times = [i.text for i in time_soup.find_all('div')]
		days = [i.text.strip() for i in day_soup.find_all('div')]
		locations = [i.text for i in location_soup.find_all('div')]

		for time, day, location in zip(times, days, locations):
			if time != 'ARRANGED' and day != 'n.a.' and location != 'n.a.' and location != 'Location Pending':
				start, end = time.split(' - ', 1)
				room, building = location.split(' ', 1)
				sections.append([crn, start, end, day, building, room])	
	return sections




#take a section given by get_sections_from_class and add it to the MySQL database.

def input_into_SQLite_database(section):
	input = ClassInfo(CRN=section[0],StartTime=section[1],EndTime=section[2],Days=section[3],Building=section[4],Room=section[5])
	input.save()

def run(): 
	get_class_links()
	classes = {}
	# remove all existing class info objects
	ClassInfo.objects.all().delete()
	#read classes from ClassLinks.txt
	with open("ClassLinks.txt", 'r') as file:
		subject_count = int(file.readline())
		for _ in range(subject_count):
			subject_code, class_count = file.readline().split()
			classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]
			print(subject_code, class_count)
#clear ClassSections.txt
	"""
	with open("ClassSections.txt",'w') as file:
		pass


		#input every class section into MySQL Database

		for subject_code in classes:
			for link in classes[subject_code]:
				sections = get_sections_from_class(link)
				for section in sections:
					input_into_SQLite_database(section)
	"""
	
	
	

	#input every class section into MySQL Database
	for subject_code in classes:
		for link in classes[subject_code]:
			sections = get_sections_from_class(link)
			for section in sections:
				input_into_SQLite_database(section)
				print(section)
