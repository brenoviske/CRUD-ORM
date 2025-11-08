#===========================
# This will be the main page for my python CRUD
#===========================
from controllers import ManagerController
from management.models import Manager

print("WELCOME TO THE MANAGEMENT SYSTEM")

def option()-> int:
    return int(input("Type your option of choice:"))

def email()-> str:
    return str(input("The email of the manager:"))
    
def get_cpf() -> str:
    return str(input("Type the CPF of the manager:")).lower()

isRunning : bool = True

while isRunning:

    print("1. Add manager")
    print("2. Delete Manager")
    print("3. Edit Manager")
    print("4. See managers")
    print("5. Add User")
    print("6. Delete User")
    print("7. Edit User")
    print("8. See users")
    print("9. Exit")

    op = option()
    match op:
        case 1:
            e_mail = email()
            name = str(input("Type the name of the manager:")).lower()
            password = str(input("Type the password of the manager:")).lower()
            sector = str(input("Type the name of the manager:")).lower()

            new_manager = Manager(e_mail=e_mail, name=name, password=password, sector=sector)
            ManagerController.addManager(new_manager)
        case 2:
            
            email = email()
            ManagerController.removeManager(email)

        case 3:
            email = email()
            password = str(input("Type the password of the manager:")).lower()
            sector = str(input("Type the name of the manager:")).lower()

            ManagerController.editManager(email, password, sector)

        case 4:
            ManagerController.get_all()
        case 5:
            email = email()
            cpf = get_cpf()
            name = str(input("Type the name of the user:")).lower()
            sector = str(input("Type the sector of th user:")).lower()
            ManagerController.addUser(email, cpf, name, sector)

        case 6:
            email = email()
            cpf = get_cpf()
            ManagerController.removeUser(email, cpf)

        case 7:
            email = email()
            cpf = get_cpf()
            name = str(input("Type the new name of the user:")).lower()
            sector = str(input("Type the new sector of the user:")).lower()
            ManagerController.editUser(email, cpf, name, sector)

        case 8:
            email = email()
            ManagerController.get_all_users(email)

        case 9:
            isRunning = False
            print('Thanks for using our system')
