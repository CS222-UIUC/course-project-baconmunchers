import requests
import re
from bs4 import BeautifulSoup
import json

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