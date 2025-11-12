from base import db
from database import *

class BankController:
    def __init__(self):
        pass


    @staticmethod
    def add_bank(bank:Bank):
        existing_bank = db.query(Bank).filter_by(name=bank.name).first()
        if existing_bank:
            print('Bank already exists')
            return
        else:
            try:
                db.add(bank)
                db.commit()
                print('Bank added')
                return
            except Exception as e:
                print('Error:',e)
                return

    @staticmethod
    def remove_bank(name:str):
        existing_bank = db.query(Bank).filter_by(name=name).first()
        if existing_bank:
            try:
                db.delete(existing_bank)
                db.commit()
                print('Bank removed')
            except Exception as e:
                print('Error:',e)
        else:
            print('Bank does not exist')

    @staticmethod
    def get_all_banks():
        banks = db.query(Bank).all()
        for bank in banks:
            print(bank.to_dict())

    @staticmethod
    def get_bank(name:str):
        bank = db.query(Bank).filter_by(name=name).first()
        if bank:
            return bank.to_dict()
        else:
            print('Bank does not exist')

    @staticmethod
    def get_total_banks():
        banks = db.query(Bank).all()
        return len(banks)


    @staticmethod
    def deposit_bank(name:str,amount:float):
        bank = db.query(Bank).filter_by(name=name).first()
        if bank:
            bank.deposit(amount)
            db.commit()
            print('Money deposited')
            return
        print('Bank does not exist')


    @staticmethod
    def withdraw_bank(name:str,amount:float):
        bank = db.query(Bank).filter_by(name=name).first()
        if bank:
            bank.withdraw(amount)
            db.commit()
            print('Money withdrawn')
        else:
            print('Bank does not exist')


