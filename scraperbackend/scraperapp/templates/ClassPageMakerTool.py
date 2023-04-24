import sys

"""
In the file coords.txt, use copy and paste the result of https://www.image-map.net/. 
Only use the shape rectangle(If you need more complex geometry, just use multiple rectangles). 
In the title area, put the room number. Make sure it matches whats in the database(ie if the database has '35' in it but the diagram has '035', use '35')
Leave everything else blank. Then copy and past starting from <map nam...> to </map>.  
Paste them in the order of the floors with no newlines between them.
"""

#sys.stdin = open('in.txt', 'r') #Can be used if you don't want to type everything out each time.

fileName = input('Building Name(Use the same exact name as in the database): ') #Put in the exact string in the database
numFloors = int(input('Number of Floors: '))
imgFolder = input('What folder are the floor plans in?: ')
imgFileNames = [input('What is the file name? EG: "cifb.png": ') for _ in range(numFloors)] #Please put them in order(top to bottom)
floorNames = [input('What should the floors be named? EG: "CIF Floor 1": ') for _ in range(numFloors)]

hitboxes = [[] for _ in range(numFloors)]
with open('coords.txt', 'r') as file: #use https://www.image-map.net/ ; put room number in title area
  lines = file.readlines()
  floor = 0
  for line in lines:
    if line == '<map name="image-map">\n':
      continue
    if line == '</map>\n' or line == '</map>':
      floor += 1
      continue
    attributes = line.split()
    roomNumber = attributes[3].split('"')[1]
    coords = attributes[5]
    hitboxes[floor].append((roomNumber, coords))
    


html = """{% load static %}
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>Get Class</title>
    <style>
      img {
          width: 100%;
          height: 100%;
          object-fit: contain;
      }
    </style>
<<<<<<< HEAD
    <script
    src="https://code.jquery.com/jquery-3.6.4.min.js"
    integrity="sha256-oP6HI9z1XaZNBrJURtCoUT5SUnxFr8s3BzRl+cbzUq8="
    crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/ui/1.13.2/jquery-ui.js"></script>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
=======
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

>>>>>>> 9d0560933d794ab366d67778f890e56ef7031af9
  </head>
  <body>
  
    <nav class="navbar navbar-light" style="background-color: #e84a27;">
  """ + f'<span class="navbar-brand mb-0 h1">&ensp;{fileName}</span>' + """
      <a class="nav-link mb=0" href="/get_class/">Advanced Search&emsp;</a>
    </nav>

    <!-- <img src="{% static 'floorplans/masterMapMedium.png' %}" alt="masterMap"> -->
    <form action="/get_building/" method="post" id="class_info_form" hidden>
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>
    <script>    
      $( "#id_SubjectCode" ).autocomplete({
        source: ['AAS', 'ABE', 'ACCY', 'ACE', 'ACES', 'ADV', 'AE', 'AFAS', 'AFRO', 'AFST', 'AGCM', 'AGED', 'AHS', 'AIS', 'ANSC', 'ANTH', 'ARAB', 'ARCH', 'ART', 'ARTD', 'ARTE', 'ARTF', 'ARTH', 'ARTJ', 'ARTS', 'ASRM', 'ASTR', 'ATMS', 'BADM', 'BASQ', 'BCOG', 'BCS', 'BDI', 'BIOC', 'BIOE', 'BSE', 'BTW', 'BUS', 'CB', 'CDB', 'CEE', 'CHBE', 'CHEM', 'CHIN', 'CHLH', 'CHP', 'CI', 'CLCV', 'CMN', 'CPSC', 'CS', 'CSE', 'CW', 'CWL', 'CZCH', 'DANC', 'EALC', 'ECE', 'ECON', 'EDPR', 'EDUC', 'EIL', 'ENG', 'ENGL', 'ENVS', 'EPOL', 'EPS', 'EPSY', 'ERAM', 'ESE', 'ESL', 'ETMA', 'EURO', 'FAA', 'FIN', 'FLTE', 'FR', 'FSHN', 'GC', 'GEOL', 'GER', 'GGIS', 'GLBL', 'GRK', 'GRKM', 'GS', 'GSD', 'GWS', 'HDFS', 'HEBR', 'HIST', 'HNDI', 'HORT', 'HT', 'HUM', 'IB', 'IE', 'IHLT', 'INFO', 'IS', 'ITAL', 'JAPN', 'JOUR', 'JS', 'KIN', 'KOR', 'LA', 'LAS', 'LAST', 'LAT', 'LAW', 'LEAD', 'LER', 'LING', 'LLS', 'MACS', 'MATH', 'MCB', 'MDIA', 'MDVL', 'ME', 'MICR', 'MILS', 'MIP', 'MSE', 'MUS', 'MUSC', 'MUSE', 'NE', 'NEUR', 'NPRE', 'NRES', 'NS', 'NUTR', 'PATH', 'PERS', 'PHIL', 'PHYS', 'PLPA', 'POL', 'PORT', 'PS', 'PSM', 'PSYC', 'QUEC', 'REES', 'REHB', 'REL', 'RHET', 'RST', 'RUSS', 'SAME', 'SCAN', 'SE', 'SHS', 'SLAV', 'SOC', 'SOCW', 'SPAN', 'SPED', 'STAT', 'SWAH', 'TAM', 'TE', 'THEA', 'TMGT', 'TRST', 'TURK', 'UKR', 'UP', 'VCM', 'VM', 'WGGP', 'WRIT']
      });
      </script>
    <script>    
      $( "#id_Building" ).autocomplete({
        source: ['1010 W Nevada', '1203 1/2 W Nevada', '1205 W Nevada', '1205 W Oregon', '1207 W Oregon', '1208 W Nevada', '614 E. Daniel', '901 W Oregon', '907 1/2 W Nevada', 'ACES Lib, Info & Alum Ctr', 'Activities & Recreation Center', 'Agricultural Engr Sciences Bld', 'Allen Residence Hall', 'Altgeld Hall', 'Animal Sciences Laboratory', 'Architecture Annex', 'Architecture Building', 'Armory', 'Art and Design Building', 'Astronomy Building', 'Beckman Institute', 'Bevier Hall', 'Burrill Hall', 'Business Instructional Fac', 'Campbell Hall', 'Campus Instructional Facility', 'Campus Recreation Center East', 'Ceramics Building', 'Ceramics Kiln House', 'Chemical and Life Sci Lab', 'Chemistry Annex', 'Chicago IL', 'Child Development Laboratory', 'Christopher Hall', 'Civil Eng Hydrosystems Lab', 'Dance Studio', 'Danville IL', 'Davenport Hall', 'David Kinley Hall', 'Digital Computer Laboratory', 'Discovery Partners Inst. CHI', 'Education Building', 'Electrical & Computer Eng Bldg', 'Engineering Hall', 'Engineering Sciences Building', 'English Building', 'Everitt Laboratory', 'Expanded Child Dev Lab', 'FAR Meeting Space', 'Flagg Hall', 'Foellinger Auditorium', 'Foreign Languages Building', 'Freer Hall', 'GYM Campus Recreation Center East', 'Grad Sch of Lib & Info Science', 'Grainger Engineering Library', 'Gregory Hall', 'Harding Band Building', 'Henry Administration Bldg', 'Huff Hall', 'Ice Arena', 'Illini Center', 'Illini Union', 'Illinois Street Residence Lng', 'Inst Labor &  Industrial Rel', 'Institute for Genomic Biology', 'Japan House', 'Krannert Art Museum', 'Krannert Center for Perf Arts', 'LAB Art-East Annex, Studio 2', 'Law Building', 'Library', 'Lincoln Hall', 'Loomis Laboratory', 'Materials Science & Eng Bld', 'Meat Science Laboratory', 'Mechanical Engineering Lab', 'Medical Sciences Building', 'Micro & Nanotechnology Lab', 'Mumford Hall', 'Music Building', 'National Soybean Res Ctr', 'Natural History Building', 'Newmark Civil Engineering Bldg', 'Noble Hall', 'Noyes Laboratory', 'Outdoor Space', 'Pennsylvania Lounge Bld - PAR', 'Plant Sciences Laboratory', 'Psychology Building', 'Richmond Studio', 'Roger Adams Laboratory', 'Seitz Materials Research Lab', 'Sidney Lu Mech Engr Bldg', 'Siebel Center for Comp Sci', 'Siebel Center for Design', 'Smith Memorial Hall', 'South Farms', 'Speech & Hearing Science Bldg', 'Spurlock Museum', 'Stock Pavilion', 'Student Dining & Res Program', 'Talbot Laboratory', 'Temple Hoyne Buell Hall', 'Transportation Building', 'Turner Hall', 'Vet Med Basic Sciences Bldg', 'Veterinary Teaching Hospital', 'Weston Hall', 'Wohlers Hall']
      });
      </script>
    <select id="floorselection">
      <option value="">Select Floor</option>
"""

for floorName, imgFileName in zip(floorNames, imgFileNames):
  floorID = imgFileName.split('.')[0]
  html += f'      <option value="{floorID}">{floorName}</option>\n'
html += '    </select>\n'  

for floorName, imgFileName, floor in zip(floorNames, imgFileNames, range(numFloors)):
  floorID = imgFileName.split('.')[0]
  div = f'    <div id="{floorID}" class="floor">\n'
  div += '      <img src="{% static ' + "'" + f'floorplans/{imgFolder}/{imgFileName}' + "'%}" + f'" alt="{floorName}" usemap="#{floorID}map"/>\n'
  #div += f'      <img src="{% static \'floorplans/{imgFolder}/{imgFileName}\' %}" alt="{floorName}" usemap="#{floorID}map"/>\n'
  div += f'      <map name="{floorID}map">\n'
  for roomNumber, coords in hitboxes[floor]:
    div += f'          <area alt="{roomNumber}" title="{roomNumber}" {coords} shape="rect" onclick="fillOutRoom(' + "'" + f'{fileName}' + "', '" + f'{roomNumber}' + "'" + ');">\n'
  div += f'      </map>\n    </div>\n'

  html += div

html += """    <script>
      function fillOutRoom(building, room) {
        document.getElementById('id_Building').value = building;
        document.getElementById('id_Room').value = room;
        document.forms[0].submit();
      }
    </script>
    
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script type="text/javascript" src= "{% static 'imageMapResizer.min.js' %}"></script>
    <script type="text/javascript">
      imageMapResize();
    </script>
    <script>
      // https://codeamend.com/blog/show-hide-div-based-on-dropdown-selected-using-jquery/#:~:text=If%20you%20want%20to%20hide,of%20the%20selected%20dropdown%20option.
      $(document).ready(function() {
          $('#floorselection').bind('change', function() {
            $(".floor").hide();
            $("#" + $(this).val()).show();
          });
          $('#floorselection').trigger('change');
      });
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
</html>"""

with open(f'{fileName}.html', 'w') as file:
  file.write(html)