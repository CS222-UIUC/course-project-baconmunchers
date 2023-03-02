import requests
import re
from bs4 import BeautifulSoup
import json

classes = {}

#read classes from ClassLinks.txt
with open("ClassLinks.txt", 'r') as file:
	subject_count = int(file.readline())
	for _ in range(subject_count):
		subject_code, class_count = file.readline().split()
		classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]

def get_data_from_class(link):
	class_page = requests.get(link)
	class_page_soup = BeautifulSoup(class_page.text, 'html.parser')
	data = class_page_soup.body.find('script', type='text/javascript').text.split(';')[0][26:]
	# The [26:] removes "var sectionDataObj = " from the beginning of the text
	list_of_dicts = json.loads(data)
	# list_of_dicts is a list of each section's information in dictionary form
	# TODO: some of the dictionary values are html divs that need to be scraped
	return list_of_dicts