#python database.py
from sqlalchemy import create_engine
import os
db_connection_string = os.environ['Database_CONNECTION_str']
engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


