from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote 

DATABASE_URL="postgresql://tuser:%s@localhost:5432/tdb"
DATABASE_PWD="11223344"


engine=create_engine( DATABASE_URL % quote(DATABASE_PWD))

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()