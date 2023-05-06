# Campus Scheduling Map

## Introduction
Empty classrooms are popular study spots, but you never know when there might be a class. Our website will show a map of several buildings on campus with class timings for each room, so students know when classes will be and how long they can stay. You can use it by either using our interactable campus map or an advanced search.

For more details, [here](https://drive.google.com/file/d/1LzHKvWhnw8I8y6qjavi56g3v_un8vb2g/view?usp=sharing) is the full project proposal, and [here](https://mediaspace.illinois.edu/media/t/1_lp25o0o4) is a video walkthrough of our project. 

## Technical Architecture
![Image of the technical architecture of the project](https://drive.google.com/uc?id=1wfIPZygM2DkgnpGCNprPILTJbG1vUljp)

## Developers
- **Peter Bremer-Feit**: Developed the web scaper and the class page creation tool
- **Ryan To**: Created and hosted the web server and generated all the maps used
- **Kaushik Varadharajan**: Developed the web scaper and much of the HTML and CSS basis
- **Daniel Zhang**: Created and integrated the SQLite database with Django

## Project Installation
First, if you do not have a version of Python3 installed, follow the steps [here](https://wiki.python.org/moin/BeginnersGuide/Download) to install it. Pip should also come installed, but if it doesn't, follow the steps [here](https://pip.pypa.io/en/stable/installation/) to install it. 

Clone this current git repository into a location where you want this stored on your local device. Run the following command.
```
git clone https://github.com/CS222-UIUC/course-project-baconmunchers
```

Navigate inside this directory, and then run the following commands one by one.
```
cd scraperbackend/
pip install django
pip install django-cors-headers
pip install djangorestframework
pip install django-extensions
pip install django-autocomplete-light
```

To run the server, run type the following command:
```
python manage.py runserver
```

Then in a brower, enter the following url:
http://localhost:8000/get_class/
