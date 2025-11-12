from database import *
from controller import BankController
from base import Base , engine

# Creating all the database tables right here
Base.metadata.create_all(engine)


print("==========================")
print("WELCOME TO THE CASH IN APP")
print("==========================")


def get_name() -> str : return str(input('Input your bank name:'))


run = True
while run:

    print('1. Add Bank')
    print('2. Remove Bank')
    print('3. List all Banks')
    print('4. Get total Banks')
    print('5. Deposit to a Bank')
    print('6. Withdraw from a Bank')
    print('7. Exit')

    op = int(input("Select your option:"))

    if op == 7:
        run = False
    match op:
        case 1:
            name = str(input('Input bank name:'))
            balance = float(input('Input your bank balance:'))

            bank = Bank(name = name , balance = balance)
            BankController.add_bank(bank)
    

        case 2:
            name = get_name()
            BankController.remove_bank(name)
        
        case 3:
            BankController.get_all_banks() # This function right here just calls the method from the controller there is no need for nothing more

        case 4:
            BankController.get_total_banks()

        case 5:
            name = get_name()
            amount = float(input('Input your bank balance:'))
            BankController.deposit_bank(name,amount)

        case 6:
            name = get_name()
            amount = float(input('Input your bank balance:'))
            BankController.withdraw_bank(name,amount)

        case 7: run = False





