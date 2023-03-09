import requests
import re
from bs4 import BeautifulSoup
import json

def get_sections_from_class(link):
	class_page = requests.get(link)
	class_page_soup = BeautifulSoup(class_page.text, 'html.parser')
	data = class_page_soup.body.find('script', type='text/javascript').text.split('\n')[1][25:-1]

	sections = []
	try:
		json_data = json.loads(data)
	except:
		print(link)
		return []

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