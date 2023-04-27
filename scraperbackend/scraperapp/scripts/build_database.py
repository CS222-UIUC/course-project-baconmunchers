"""Script that runs within the Django context to clear and repopulate the database"""
import re
import json
# from time import perf_counter
import requests
from bs4 import BeautifulSoup
#from scraperapp.models import ClassInfo #This doesn't work right now

course_explorer = 'https://courses.illinois.edu'
year = '2023'
season = 'spring'

def get_class_links(): # pylint: disable=too-many-locals
    """Function that gets links for classes from Course Explorer"""
    subjects_page_link = course_explorer + f'/schedule/{year}/{season}'
    subjects_page = requests.get(subjects_page_link, timeout=10)

	#Parse through the course subjects page for all subject page links
    subjects_page_soup = BeautifulSoup(subjects_page.text, 'html.parser')
    subjects_page_links = [str(i.get('href')) for i in subjects_page_soup.find_all('a')]
    subject_links_regex = re.compile(f'/schedule/{year}/{season}/.*')
    subject_links = [course_explorer + link for link in subjects_page_links
    						if not re.match(subject_links_regex, link) is None]

	#build dictionary of subject codes to lists of class linkes
    classes = {}

    for subject_page_link in subject_links:
        subject_code = re.split(r'/', subject_page_link)[-1]
        subject_page = requests.get(subject_page_link, timeout=10)
        subject_page_soup = BeautifulSoup(subject_page.text, 'html.parser')
        subject_page_link = [str(i.get('href')) for i in subject_page_soup.find_all('a')]
        class_links_regex = re.compile(fr'/schedule/{year}/{season}/.*/\d\d\d')
        class_links = [course_explorer + link for link in subject_page_link
							if not re.match(class_links_regex, link) is None]
        classes[subject_code] = class_links


	#write classes to ClassLinks.txt for later use
    with open("ClassLinks.txt", 'w', encoding='utf-8') as file:
        file.write(f"{len(classes)}\n")
        for subject_code, links in classes.items():
            file.write(f"{subject_code} {len(links)}\n")
            for link in links:
                file.write(f"{link}\n")

def get_sections_from_class(link): # pylint: disable=too-many-locals
    """Get non-online non-asynchronous sections of a class, given course explorer url.
    Data returned as list of sections.
    Each section is formatted as [crn, start, end, day, building, room].
    """

    subject_code, course_number = link.split('/')[-2:]
    class_page = requests.get(link, timeout=10)
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

        time_soup = BeautifulSoup(section_dict['time'], 'html.parser')
        day_soup = BeautifulSoup(section_dict['day'], 'html.parser')
        location_soup = BeautifulSoup(section_dict['location'], 'html.parser')
        times = [i.text for i in time_soup.find_all('div')]
        days = [i.text.strip() for i in day_soup.find_all('div')]
        locations = [i.text for i in location_soup.find_all('div')]
        for time, day, location in zip(times, days, locations):
            if time != 'ARRANGED' and day != 'n.a.' and location != 'n.a.' and location != 'Location Pending':
                start, end = time.split(' - ', 1)
                if location == 'MAC GYM Campus Recreation Center East':
                    room, building = 'MAC GYM', 'Campus Recreation Center East'
					# TODO: are there any more minor exceptions like this for when we re-generate the database
                else:
                    room, building = location.split(' ', 1)
                sections.append([subject_code, course_number, crn, start, end, day, building, room])
    return sections

def input_into_SQLite_database(section):
    """Take a section given by get_sections_from_class and add it to the MySQL database."""
    sqlite_input = ClassInfo(	SubjectCode=section[0], \
                        CourseNumber=section[1], \
                        CRN=section[2], \
                        StartTime=section[3], \
                        EndTime=section[4], \
                        Days=section[5], \
                        Building=section[6], \
                        Room=section[7])
    sqlite_input.save()

def run():
    """Django convention for running scripts"""
    # t0 = perf_counter()
    get_class_links()
    classes = {}
    # remove all existing class info objects
    ClassInfo.objects.all().delete()
    #read classes from ClassLinks.txt
    with open("ClassLinks.txt", 'r', encoding='utf-8') as file:
        subject_count = int(file.readline())
        for _ in range(subject_count):
            subject_code, class_count = file.readline().split()
            classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]
            print(subject_code, class_count)

    # # clear ClassSections.txt
    # with open("ClassSections.txt",'w', encoding='utf-8') as file:
    #     pass
    # # input every class section into MySQL Database
    # # input every class section into SQLite Database
    # for subject_code, links in classes.items():
    #     print(subject_code)
    #     for link in links:
    #         sections = get_sections_from_class(link)
    #         for section in sections:
    #             input_into_SQLite_database(section)
    # t1 = perf_counter()
    # print(t1 - t0)
