#===========================
# This will be the main page for the my python CRUD
#===========================
from models import  Manager,session, User

print("WELCOME TO THE MANAGEMENT SYSTEM")

def option()-> int:
    return int(input("Type your option of choice:"))


def email()-> str:
    return str(input("The email of the manager:"))
    
def error()-> None:
    print("Manager does not exist in our Data Base")

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
    print("9. Number of user")
    print("10. Exit")

    op = option()
    match op:
        case 1:

            e_mail = email()
            
            manager = session.query(Manager).filter_by(email = e_mail).first()
            
            if manager:
                print("Manager already exists in our DataBase")
            else:
                password = str(input("Type your password:"))
                sector = str(input("Type the manager sector:"))

                new_manager = Manager(email = e_mail, password = password , sector = sector)
                session.add(new_manager)
                session.commit() # Chaning the data on the Data Base
                print("Manager successfully added")

        case 2:
            
            e_mail = email()
            
            manager = session.query(Manager).filter_by(email = e_mail).first()
            if not manager:
                error()
            else:
                
                session.delete(manager)
                session.commit()
                print("The manager has been successfully deleted")

        case 3:
            e_mail = email()
            
            manager = session.query(Manager).filter_by(email = e_mail).first()
            if not manager: error()
            else:
                op = str(input("Select watch you want to changfe on the manager profile.")).lower()
                
                match op:
                    case "email": 
                        e_mail = str(input("Type the new e-mail:")).lower()
                        manager.email = e_mail
                    case "password":
                        password = str(input("Type the new password:")).lower()
                        manager.password = password
                    case "sector":
                        sector = str(input("Type the name of the new sector:")).lower()
                        manager.sector = sector

        
        case 4:
            managers = session.query(Manager).all() # This line can see it how many managers are there by acessing the SqlAlchemy query
            print(managers)
        
        case 5:
            
            e_mail = email()
            manager = session.query(Manager).filter_by(email = e_mail).first()
            
            if not manager:
                error()
            else:
                cpf = str(input("The cpf of the user:") )
                name = str(input("The name of the user:"))
                sector = str(input("The sector of the user:"))
                
                user = User(cpf = cpf , name = name , sector = sector)
                
                # Adding the user with the addUser method
                # If the user already exists it will return a message either for confirmation or failure

                manager.addUser(user)

        case 6:
            
            e_mail = email()
            manager = session.query(Manager).filter_by(email = e_mail).first()
            
            if not manager: error()
            else:
                cpf = str ( input ("Type the cpf of the user:") )
                manager.removerUser(cpf)

        
        case 7:
            e_mail = email()
            manager = session.query(Manager).filter_by(email = e_mail).first()

            if not manager : error()
            else:
                cpf = str(input("The cpf of the user, please:")).lower()
                existing_user = session.query(User).filter_by(cpf = cpf).first()

                if not existing_user : print("User was not found inside our Data Base")
                else:
                    op = str(input("Type what you want to change in your user:")).lower()
                    match op:
                        case "cpf" : 
                            existing_user.cpf = cpf
                        case "sector":
                            existing_user.sector = sector
                        case "name":
                            existing_user.name = name
        case 8:
            e_mail = email()
            manager = session.query(Manager).filter_by(email = e_mail).first()

            if not manager: error()
            else: print(manager.getUsers())
            
        case 8:
            e_mail = email()
            
            manager = session.query(Manager).filter_by( email = e_mail).first()
            if not manager:
                error()
            else: print(manager.getUsers())

        case 9:
            print("Thanks for using our system")
            isRunning = False
                    
        case 10:
            print("Thanks for using our system")
            isRunning = False

