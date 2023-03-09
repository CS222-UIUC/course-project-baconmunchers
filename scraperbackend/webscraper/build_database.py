import requests
import re
from bs4 import BeautifulSoup
import json
from get_sections_from_class import get_sections_from_class
import mysql.connector



#TODO: Currently just writes everything to a file. Need to make it place into database.

#take a section given by get_sections_from_class and add it to the MySQL database.
def input_into_MySQL_database(section, file_name):
	with open(file_name, 'a') as file:
		file.write('|'.join(section))
		file.write('\n')

"""
conn = mysql.connector.connect(
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
			
conn.close()
"""

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
			input_into_MySQL_database(section, "ClassSections.txt")