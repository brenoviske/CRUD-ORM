from sqlalchemy import Column, String, Float
from base import Base



class Bank(Base):
    
    __tablename__ = "banks"


    name = Column(String(200) , primary_key=True , null = False )
    balance = Column(Float,nullable = False)

    def to_dict(self):
        return f'Bank Name: {self.name} Balance: {self.balance}'


    def deposit(self,amount:float):
        self.balance += amount


    def withdraw(self,amount:float):
        if amount > self.balance:
            print("You don't have enough money to withdraw")
        self.balance -= amount
        return



