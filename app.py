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
#    /\
#   /  \
#  /_  _\
#   | |
#   | |
#   | |
#   |_|
#COnVERT THIS TO HTML SOMEONE

#CONVERT TO HTML WITH FORM

from flask import Flask, render_template, jsonify, request
from database import engine, load_items_from_db, load_item_from_db, add_reservation_to_db
from sqlalchemy import text
app = Flask(__name__)



def load_items_from_db():
  with engine.connect() as conn:
    result= conn.execute(text("select * from items"))

  
  items=[]
  for row in result.all():
    items.append(row)
  return items

@app.route("/")
def items_list():
  items = load_items_from_db()
  return render_template('home.html', 
                           items=items)

@app.route("/api/items")
def list_items():
  items=load_items_from_db()
  return jsonify(items)

@app.route("/item/<id>")
def about_item(id):
  item=load_item_from_db(id)
  return render_template('itempage.html', item =item)

@app.route("/item/<id>/apply", methods=['post'])
def apply_to_item(id):
  reservationid=id
  data = request.form
  item = load_item_from_db(reservationid)
  j=reservationid
  add_reservation_to_db(j, data)
  return render_template('reserving_items_submitted.html', 
                         reservation=data,
                         item=item)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

