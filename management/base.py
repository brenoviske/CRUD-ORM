from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

engine = create_engine("mysql+pymysql://root:Ivimorcega1@localhost:3306/management")

Base  = declarative_base()
Session = sessionmaker( bind = engine )
db = Session()
