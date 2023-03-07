#PLEASE PUSH BACK TO GITHUB AFTER CODE
from flask import Flask, render_template, jsonify, request
from database import engine, load_items_from_db, load_item_from_db, add_reservation_to_db, add_new_item
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
@app.route("/newitem", methods=['post'])
def newitem():
  data = request.form
  add_new_item(data)
  return render_template('newitem_submitted.html', 
                         newitemdata=data,)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

