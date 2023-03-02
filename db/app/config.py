from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote 

#DATABASE_URL="postgresql://tuser:%s@localhost:5432/tdb"
#DATABASE_URL="postgresql://tuser:%s@172.18.0.3:5050/tdb"
#DATABASE_PWD="11223344"
db_name = 'tdb'
db_user = 'tuser'
db_pass = '11223344'
db_host = '172.18.0.2'
db_port = '5431'

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
#engine=create_engine( DATABASE_URL % quote(DATABASE_PWD))
engine=create_engine(db_string)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()