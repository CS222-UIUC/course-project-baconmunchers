import requests
import re
from bs4 import BeautifulSoup
from scraperapp.models import ClassInfo
import json
# import mysql.connector


def get_sections_from_class(link):
	class_page = requests.get(link)
	class_page_soup = BeautifulSoup(class_page.text, 'html.parser')
	data = class_page_soup.body.find('script', type='text/javascript').text.split(';')[0][26:]
	# The [26:] removes "var sectionDataObj = " from the beginning of the text

	sections = []
	for section_dict in json.loads(data):
		crn = section_dict['crn']

		# TODO: do this with regex for better efficiency?
		time = BeautifulSoup(section_dict['time'], 'html.parser').div.text
		day = BeautifulSoup(section_dict['day'], 'html.parser').div.text.strip()
		location = BeautifulSoup(section_dict['location'], 'html.parser').div.text
		
		# TODO: handle if location == 'n.a.', day = 'n.a.', time == 'ARRANGED' 
		if location == 'n.a.':
			room, building = 'n.a', 'n.a'
		else:
			room, building = location.split(' ', 1)
		if time == 'ARRANGED':
			start, end = 'ARRANGED', 'ARRANGED'
		else:
			start, end = time.split(' - ', 1)
		if day == 'n.a.':
			pass

		sections.append([crn, start, end, day, building, room])
	return sections

# TODO: test get_sections_from_class

# print(get_sections_from_class('https://courses.illinois.edu/schedule/2023/spring/MACS/100'))
# [
# 	['63465', '09:00AM', '09:50AM', 'R', 'Gregory Hall', '329'], 
# 	['63466', '10:00AM', '10:50AM', 'R', 'Gregory Hall', '313'], 
# 	['63467', '11:00AM', '11:50AM', 'R', 'Gregory Hall', '327'], 
# 	['63468', '04:00PM', '04:50PM', 'R', 'n.a', 'n.a'], 
# 	['63470', 'ARRANGED', 'ARRANGED', 'n.a.', 'n.a', 'n.a'], 
# 	['63471', 'ARRANGED', 'ARRANGED', 'n.a.', 'n.a', 'n.a'], 
# 	['63472', '01:00PM', '01:50PM', 'R', 'Gregory Hall', '313'], 
# 	['63473', '02:00PM', '02:50PM', 'R', 'Gregory Hall', '313'], 
# 	['63474', '03:00PM', '03:50PM', 'R', 'Gregory Hall', '313'], 
# 	['63835', '10:00AM', '10:50AM', 'F', 'Gregory Hall', '327'], 
# 	['63836', '11:00AM', '11:50AM', 'F', 'Gregory Hall', '327'], 
# 	['63837', '12:00PM', '12:50PM', 'F', 'Gregory Hall', '327'], 
# 	['63838', 'ARRANGED', 'ARRANGED', 'n.a.', 'n.a', 'n.a'], 
# 	['67935', '02:00PM', '02:50PM', 'R', 'n.a', 'n.a'], 
# 	['67938', '12:00PM', '12:50PM', 'F', 'n.a', 'n.a'], 
# 	['63464', 'ARRANGED', 'ARRANGED', 'n.a.', 'n.a', 'n.a']
# ]


#take a section given by get_sections_from_class and add it to the MySQL database.
def input_into_SQLite_database(section):
	input = ClassInfo(CRN=section[0],StartTime=section[1],EndTime=section[2],Days=section[3],Building=section[4],Room=section[5])
	input.save()

	"""conn = mysql.connector.connect(
				   user='root', password='dAta4Cs22SmySQ', host='127.0.0.1', database='mydb')
			
				cursor = conn.cursor()
			
				insert_stmt = (
				   "INSERT INTO DATA(CRN, TIME_START, TIME_END, DAY, LOCATION, ROOM_NUMBER)"
				   "VALUES (%s, %s, %s, %s, %s, %s)"
				)
			
				data = (crn, time_start, time_end,day,location,room_number)
			
				try:
				   cursor.execute(insert_stmt, data)
				   conn.commit()
			
				except:
				   conn.rollback()
			
				print("Data inserted")
			
				conn.close()"""
# every django script must have a run function in order to be ran
def run():	
	classes = {}

	#read classes from ClassLinks.txt
	with open("ClassLinks.txt", 'r') as file:
		subject_count = int(file.readline())
		for _ in range(subject_count):
			subject_code, class_count = file.readline().split()
			classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]


	#input every class section into MySQL Database

	for subject_code in classes:
		for link in classes[subject_code]:
			sections = get_sections_from_class(link)
			for section in sections:
				input_into_SQLite_database(section)