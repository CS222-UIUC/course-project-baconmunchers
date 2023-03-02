import requests
import re
from bs4 import BeautifulSoup

classes = {}

#read classes from ClassLinks.txt
with open("ClassLinks.txt", 'r') as file:
	subject_count = int(file.readline())
	for _ in range(subject_count):
		subject_code, class_count = file.readline().split()
		classes[subject_code] = [file.readline()[:-1] for _ in range(int(class_count))]


#for subject_code in classes:
#	for class_page_link in classes[subject_code]:
#		class_page = requests.get(class_page_link)
#		class_page_soup = BeautifulSoup(class_page.text, 'html.parser')
#		class_table = str(i) for i in class_page_soup.find_all('script', attrs={'type':'text/javascript'})