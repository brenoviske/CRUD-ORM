from models import Manager, User
from base import db



# --------- Making the Manager Controller ------- #

class ManagerController:
    def __init__(self):
        pass

    @staticmethod
    def addManager(manager:Manager):
        manager = db.query(Manager).filter_by(email = manager.email).first()
        if manager:
            print('User already exists')
            return

        try:
            db.add(manager)
            db.commit()
            print('User added successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def removeManager(email:str):
        manager = db.query(Manager).filter_by(email = email).first()
        if not manager:
            print('User does not exist')
            return
        try:
            db.delete(manager)
            db.commit()
            print('User removed successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def editManager(email:str, password:str , sector:str):
        manager = db.query(Manager).filter_by(email = email).first()
        if not manager:
            print('User does not exist')
            return
        try:
            manager.email = email
            manager.password = password
            manager.sector = sector
            db.commit()
            print('User edited successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def get_all():
        managers = db.query(Manager).all()
        for manager in managers:
            print(manager.to_dict())

    @staticmethod
    def addUser(email:str,cpf:str, name:str, sector:str):
        manager = db.query(Manager).filter_by(email = email).first()
        if not manager:
            print('The user Manager does not exist')
            return

        try:
            user = User(cpf = cpf, name = name, sector = sector, manager_email = email)
            db.add(user)
            db.commit()
            print('User added successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def removeUser(email:str,cpf:str):
        user = db.query(User).filter_by(cpf =cpf ,manager_email= email).first()
        if not user:
            print('User not found for this manager')
            return
        try:
            db.delete(user)
            db.commit()
            print('User removed successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def editUser(email:str,cpf:str,name:str,sector:str):
        user = db.query(User).filter_by(cpf= cpf,manager_email = email).first()
        if not user:
            print('User does not exist')
            return
        try:
            user.cpf = cpf
            user.name = name
            user.sector = sector
            user.manager_email = email
            db.commit()
            print('User edited successfully')
        except Exception as e:
            db.rollback()
            print(e)

    @staticmethod
    def get_all_users(email:str):
        users = db.query(User).filter_by(manager_email = email).all()
        for user in users:
            print(user.to_dict())

    @staticmethod
    def getUser(cpf:str,email:str):
        user = db.query(User).filter_by(cpf =cpf,manager_email = email).first()
        if not user:
            print('User does not exist')
            return
        print(user.to_dict())