from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///banking.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

db = Session() # Initializing db to query and manipulate data from the database


