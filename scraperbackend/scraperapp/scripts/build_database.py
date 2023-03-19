import requests
import re
from bs4 import BeautifulSoup
from scraperapp.models import ClassInfo
import json

# import mysql.connector

# from get_sections_from_class import get_sections_from_class

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



#TODO: Currently just writes everything to a file. Need to make it place into database.

#take a section given by get_sections_from_class and add it to the MySQL database.

def input_into_SQLite_database(section):
	input = ClassInfo(CRN=section[0],StartTime=section[1],EndTime=section[2],Days=section[3],Building=section[4],Room=section[5])
	input.save()

def run():	
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
