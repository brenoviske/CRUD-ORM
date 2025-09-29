from task_manager.crud.models.user import User
from task_manager.crud.models.base import session
from task_manager.crud.models.task import Task


class TaskManager:

    def __init__(self):
        pass

    @staticmethod
    def addUser(user:User) -> None:
        
        existing_user = session.query(User).filter_by(email = user.getEmail()).first()
        if existing_user: print('User already added')
        else:
            new_user = User(email = user.getEmail(),password = user.getPassword()) 
            session.add(new_user)
            session.commit()

    @staticmethod
    def removeUser(email:str) -> None:
        existing_user = session.query(User).filter_by( email = email).first()
        if not existing_user : print('User does not exist') 
        else:
            session.delete(existing_user)
            session.commit()
            print('User deleted.')

    @staticmethod
    def addTasks(email:str) -> None:
        
        existing_user = session.query(User).filter_by(email = email).first()

        if not existing_user:
            print('There is no user avaiable for you to add your task')
        else:
            name = str(input('Type the name of the task:'))
            description = str(input('Type the description of the task:'))

            new_task = Task(name = name,description = description)
            existing_user.addTask(new_task)


    @staticmethod
    def removeTask(email:str,name:str) -> None:
        existing_user = session.query(User).filter_by(email = email).first()

        if not existing_user: print('There is no such user')
        else:
            existing_user.removeTask(name)

    @staticmethod
    def getUser() -> list[str]:
        users = session.query(User).all()

        if len(users) == 0:
            return []
        else:
            return[user.email for user in users]
        

    @staticmethod
    def countUsers() -> int: return len(session.query(User).all())

    
    
