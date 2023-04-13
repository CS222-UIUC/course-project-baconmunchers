import requests
import re
from bs4 import BeautifulSoup

def run():
	print('Accessing all class page links')
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


	#write classes to ClassLinks.txt for later use
	with open("ClassLinks.txt", 'w') as file:
		file.write(f"{len(classes)}\n")
		for subject_code in classes:
			file.write(f"{subject_code} {len(classes[subject_code])}\n")
			for link in classes[subject_code]:
				file.write(f"{link}\n")