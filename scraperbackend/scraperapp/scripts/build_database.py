import requests
import re
from bs4 import BeautifulSoup
from scraperapp.models import ClassInfo
import json

# import mysql.connector

from get_sections_from_class import get_sections_from_class




#TODO: Currently just writes everything to a file. Need to make it place into database.

#take a section given by get_sections_from_class and add it to the MySQL database.

def input_into_SQLite_database(section):
	input = ClassInfo(CRN=section[0],StartTime=section[1],EndTime=section[2],Days=section[3],Building=section[4],Room=section[5])
	input.save()

def run():	
	classes = {}


	#read classes from ClassLinks.txt
	with open("ClassLinks.txt", 'r') as file:
		subject_count = int(file.readline())
		for _ in range(subject_count):
			subject_code, class_count = file.readline().split()
			classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]

#clear ClassSections.txt
	with open("ClassSections.txt",'w') as file:
		pass


		#input every class section into MySQL Database

		for subject_code in classes:
			for link in classes[subject_code]:
				sections = get_sections_from_class(link)
				for section in sections:
					input_into_SQLite_database(section)

	#input every class section into MySQL Database
	for subject_code in classes:
		for link in classes[subject_code]:
			sections = get_sections_from_class(link)
			for section in sections:
				input_into_SQLite_database(section, "ClassSections.txt")
