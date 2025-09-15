from sqlalchemy import Column, String, Float , create_engine,Integer
from sqlalchemy.orm import declarative_base , sessionmaker


Base = declarative_base()

class Bank(Base):
    
    __tablename__ = "banks"

    accNumber = Column(Integer,primary_key=True , nullable = False)
    balance = Column(Float,nullable = False)

    def __repr__(self):
        return f"<User(accNumber = {self.accNumber}, balance = {self.balance})>"
    
    def getBalance(self) -> float:
        return self.balance
    
    def deposit(self, deposit:float) -> None:
        self.balance += deposit

    def withdraw( self, withdraw:float) -> None:
        if ( withdraw > self.balance):
            print("Insuficient funds")
        else:
            self.balance -= withdraw


engine = create_engine("mysql+pymysql://root:Ivimorcega1@localhost:3306/banking")

Session = sessionmaker(bind = engine)
session = Session()
# Creating all the tables inside my sqlworkbench
Base.metadata.create_all(engine)
