#python database.py
from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['Database_CONNECTION_str']
engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_items_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from items"))
    items = []
    for row in result.all():
      items.append(dict(row))
    return items

def load_item_from_db(theid):
  values={'val':theid}
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM items WHERE id = :val"), values)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]
def add_reservation_to_db(reservationid, data):
  with engine.connect() as conn:
    values={'full_name':data['full_name'],
            'email':data['email'],
           'reservationidval':reservationid}
    query=text("UPDATE `kellettschool_codify_lostnfound`.`items` SET `isitemclaimed` = '1', `reserverfullname` = :full_name, `reserveremail` = :email WHERE (`id` = :reservationidval);")
    conn.execute(query, values)
def add_new_item(data):
  with engine.connect() as conn:
    if data['nameOnItem']=="":
      values={'itemname':data['itemname'],
             'catagory':data['catagory'],
             'itemtype':data['type'],
             'location_lastfound':data['location_lastfound'],
             'nameOnItem':'No Name',
             'itemdescription':data['itemdescription'],
             'isitclaimed':'0'}
      query=text("INSERT INTO `kellettschool_codify_lostnfound`.`items` (`itemname`, `catagory`, `itemtype`, `location_lastfound`, `nameOnItem`, `itemdescription`, `isitemclaimed`) VALUES (:itemname, :catagory, :itemtype, :location_lastfound, :nameOnItem, :itemdescription, :isitclaimed);")
      conn.execute(query,values)
    else:
      values={'itemname':data['itemname'],
             'catagory':data['catagory'],
             'itemtype':data['type'],
             'location_lastfound':data['location_lastfound'],
             'nameOnItem':data['nameOnItem'],
             'itemdescription':data['itemdescription'],
             'isitclaimed':'0'}
      query=text("INSERT INTO `kellettschool_codify_lostnfound`.`items` (`itemname`, `catagory`, `itemtype`, `location_lastfound`, `nameOnItem`, `itemdescription`, `isitemclaimed`) VALUES (:itemname, :catagory, :itemtype, :location_lastfound, :nameOnItem, :itemdescription, :isitclaimed);")
      conn.execute(query,values)
      
    
      