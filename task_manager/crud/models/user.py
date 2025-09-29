from task_manager.crud.models.task import Task 
from task_manager.crud.models.base import db, session,relationship,engine
from sqlalchemy import Column,Integer,String ,ForeignKey




class User(db):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, nullable=False,autoincrement=True)
    email = Column(String(60),nullable=False)
    password = Column(String(60),nullable=False)

    tasks = relationship('Task', back_populates = 'user')

    def __repr__( self ):
        return f'<(id = {self.id},e-mail = {self.email} , password = {self.password})'
    

    def getId(self) -> int : return self.id

    def getEmail(self) -> str: return self.email

    def setEmail(self,email:str) -> None:
        self.email = email

    def getPassword(self) -> str: return self.password

    def setPassword(self,password:str) -> None:
        self.password = password

    def addTask(self,task:Task) -> None:
        existing_task  = session.query(Task).filter_by(name = task.getName()).first()

        # Makign a verification to see if the task already exists or no

        if existing_task : print('The task already exist in our database')
        else:
            new_task = Task( name = task.name , description = task.description)
            session.add(new_task) # Making the add change

            session.commit() # Sending it to thye database
            print('Task successfully added') # Making a verification to make it sure the task has been added

    def removeTask(self,name:str) -> None:

        task = session.query(Task).filter_by(name = name).first()

        if not task:
            print('Sorry, the task already does not exist in our database')
        else:
            session.delete(task)
            session.commit()
            print('Task Successfully deleted')


    def seeTasks(self) -> list[str]: return [task.name for task in self.tasks]
    
    def numberTasks(self) -> int: return len(self.tasks)

    def getTask(self,name:str) -> Task:
        
        existing_task = session.query(Task).filter_by(name = name).first()

        if not existing_task:
            pass
        else:
            return existing_task
        
    def setTask(self,name:str) -> None:
        existing_task = session.query(Task).filter_by(name = name).first()
        if not existing_task: print(f'The task with the name {name} does not exist in our database')
        else:
            op = str(input('What would you like to update in your Task?') ).lower()

            match op:
                case 'name':
                    new_name = str(input('Select the new name:'))
                    existing_task.setName(new_name)

                case 'description':
                    new_description = str(input('Select the new description :'))
                    existing_task.setDescription(new_description)   

    
