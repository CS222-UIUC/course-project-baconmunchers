import sys

"""
In the file coords.txt, use copy and paste the result of https://www.image-map.net/. 
Only use the shape rectangle(If you need more complex geometry, just use multiple rectangles). 
In the title area, put the room number. Make sure it matches whats in the database(ie if the database has '35' in it but the diagram has '035', use '35')
Leave everything else blank. Then copy and past starting from <map nam...> to </map>.  
Paste them in the order of the floors with no newlines between them.
"""

#sys.stdin = open('in.txt', 'r') #Can be used if you don't want to type everything out each time.

fileName = input('Building Name(Use the same exect name as in the database): ') #Put in the exact string in the database
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
  </head>
  <body>
    <!-- <img src="{% static 'floorplans/masterMapMedium.png' %}" alt="masterMap"> -->
    <form action="/get_building/" method="post" id="class_info_form">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>

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

  </body>
</html>"""

with open(f'{fileName}.html', 'w') as file:
  file.write(html)