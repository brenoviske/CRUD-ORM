from database import Bank
from database import session


print("==========================")
print("WELCOME TO THE CASH IN APP")
print("==========================")



def get_accNum()-> int:
    return int(input("Enter your acc number:"))

def get_bank(accNum:int) -> Bank:
    return session.query(Bank).filter_by(accNumber = accNum).first()


isRunning: bool = True
while isRunning:

    print("1.Register your bank")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Get Balance")
    print("5.Delete Bank")
    print("6 See banks")
    print("7.Exit")

    op = int(input("Select your option:"))

    match op:
        case 1: 
            accNum = get_accNum()
            balance = float(input("Enter your bank balance"))

            bank = get_bank(accNum)

            if bank:
                print("This bank already exists\n")
            else:
                new_bank = Bank(accNumber = accNum, balance = balance)
                session.add(new_bank)
                session.commit()
                
                print("Bank sucessfully added\n")
    

        case 2:
            accNum = get_accNum()

            bank = get_bank(accNum)

            if bank :
                print("Bank Successfully found")
                deposit = float( input ( "What is the total amount of your deposit:"))
                bank.deposit(deposit)
                session.commit()
                print("Deposit sucessfully made it\n")
            else:
                print("Bank was not found among our database\n")
            
        
        case 3:
            
            accNum = get_accNum()


            bank = get_bank(accNum)
            if bank:
                print("Bank sucessfully found")
                withdraw = float ( input ("What is the total amount you wish to withdraw:"))
                bank.withdraw(withdraw)
                session.commit()
                print("Withdraw sucessfully made\n")
            else:
                print("Bank was not found\n")


        case 4:

            accNum = get_accNum
            bank = get_bank(accNum)

            if not bank:
                print("Bank was not found")
            else:
                print(bank.getBalance())
        
        case 5:

            accNum = get_accNum()

            bank = get_bank(accNum)
            if bank:
                session.delete(bank)
                session.commit()
                print("Bank successfully deleted\n")
            else:
                print("Bank was not found\n")

        case 6:

            all_banks = session.query(Bank).all()
            print(all_banks,"\n")

        case 7:
            isRunning = False;





