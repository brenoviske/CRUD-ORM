from task_manager.crud.models.base import db, session,engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Task(db):

    __tablename__ = 'tasks'

    id = Column(Integer,primary_key = True,nullable = False, autoincrement = True)
    name = Column(String(200),nullable = False) 
    description = Column(String(200), nullable = False)

    user_id = Column(Integer,ForeignKey('users.id'))

    user = relationship("User",back_populates='tasks')

    def __repr__(self):
        return f'<(id ={self.id},name={self.name},description={self.description})'
    

    def getId(self) -> int:
       return self.id
 
    def getName(self) -> str:
        return self.name
    
    def setName(self,name:str) -> None:
        self.name = name
        session.commit() # commiting to the database

    def getDescription(self) -> str:
        return self.description
    
    def setDescription(self, description:str) -> None:
        self.description = description
        session.commit() # commiting to the database
    
    
