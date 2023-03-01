#PLEASE PUSH BACK TO GITHUB AFTER CODE
#do that by finding the tabs (near console/shell or near webview and press git)
#To Do List
# - The database
# - importing information to database
# - Styling
#    (optional after everything((polishing)) )
#    - add option to add photos to importing new items
#    - add a additional catalogue link with the catagories that lead to the names of the items (clicking name leads to jumping to the place on the main page where the item is)

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