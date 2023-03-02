#PLEASE PUSH BACK TO GITHUB AFTER CODE
#do that by finding the tabs (near console/shell or near webview and press git)
#To Do List
# - The database
# - importing information to database
# - Styling
#    (optional after everything((polishing)) )
#    - add option to add photos to importing new items
#    - add a additional catalogue link with the catagories that lead to the names of the items (clicking name leads to jumping to the place on the main page where the item is)
#YOOO HERES THE APPENDINATOR
#ITEM = []
#hesthemap = {'type' : "",
#    'id': "",
#    'location_lastfound': "",
#    'is_ItemNamed' : False,
#    'item_name': "",
#    'nameOnItem':"",
#    'description' : ""}
#typ = int(input('''Type "1" for clothing, type "2" for items: '''))
#if typ == 1:
#    hesthemap['type'] = "1" 
#    typzoom = input('''Type "1" for Jackets, 
#    "2" for Ties/Accessories, 
#    "3" for PE related items,
#    "4" for Blazers: ''')
#    hesthemap['id'] = typzoom 
#elif typ == 2:
#  hesthemap['type'] = "2" 
#  typzoom = input('''Type "1" for Water Bottles, 
#  "2" for Books,
#  "3" for Stationery,
#  "4" for Electronic items
#  "5" for Lunchboxes: ''')
#  hesthemap['id'] = typzoom 
#location = input('Where was it found: ')
#hesthemap['location_lastfound'] = location
#name = input("What is the colour of the item and what is the item: ")
#hesthemap['item_name'] = name
#describir = input("What is a description of the item: ")
#hesthemap['description'] = describir
#yummy = input('''Does the item have a name (Y/N): ''')
#if yummy == 'Y':
#    hesthemap['is_ItemNamed'] = True
#    Dean_The_Duck = input('What is the name: ')
#    hesthemap['nameOnItem'] = Dean_The_Duck
#ITEM.append(hesthemap)


from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

ITEMS = [
  {
    'type' : "1",
    'id': "1",
    'location_lastfound': "Sky Pitch",
    'is_ItemNamed' : True,
    'item_name': "Black jacket",
    'nameOnItem':"Fong Hang",
    'description' : "The name on the jacket is Fong Hang"
  },
  {
   
   
    'type' : "2",
    'id': "1",
    'location_lastfound': "Sky Pitch",
    'is_ItemNamed' : False,
    'item_name': "Blue bottle",
    'nameOnItem':False,
    'description' : "The bottle is made of clear plastic"
  }
]

@app.route("/")
def items_list():
    return render_template('home.html', 
                           items=ITEMS)
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)