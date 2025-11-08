from sqlalchemy import Column , String , ForeignKey
from sqlalchemy.orm import relationship
from base import Base

# ------- Creating the Manager table in the database ----- #
class Manager(Base):

    __tablename__ = 'managers'

    email = Column(String(200),primary_key = True)
    password = Column(String(200), nullable = False)
    sector = Column(String(200) , nullable = False)

    users = relationship("User",back_populates="manager")

    def to_dict(self):
        return {
            "email" : self.email,
            "sector" : self.sector,
        }


# ---------- Creating the User table in the database ------ #
class User(Base):
    __tablename__ = 'users'

    cpf = Column( String(11), primary_key = True , nullable = False)
    name = Column(String(200), nullable = False)
    sector = Column( String(200) , nullable = False)

    manager_email = Column(String(200),ForeignKey("managers.email"))
    manager = relationship("Manager",back_populates = "users")

    def to_dict(self):
        return {
            "cpf" : self.cpf,
            "name" : self.name,
            "sector" : self.sector,
            "manager_email" : self.manager_email,
        }

