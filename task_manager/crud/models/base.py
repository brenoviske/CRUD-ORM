from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker , relationship

# Creating and configuring the database
engine = create_engine('sqlite:///management.db')
# Declaring the database
db = declarative_base()


# Creating session to edit and query data of the crud
Session = sessionmaker(bind = engine )
session = Session()
