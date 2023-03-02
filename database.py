#python database.py
from sqlalchemy import create_engine
db_connection_string = "mysql+pymysql://ox38amsbwam5dy1vrzto:pscale_pw_4tPLDauwvCdDcj34XpB4fHrBTDrGoGzKGnQPjny1Agk@ap-southeast.connect.psdb.cloud/kellettschool_codify_lostnfound?charset=utf8mb4"
engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


