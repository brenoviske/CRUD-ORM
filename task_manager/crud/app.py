from taskmanager import TaskManager
from task_manager.crud.models.user import User

print('WELCOME TO THE TASK MANAGER SYSTEM')


isRunning:bool = True

def email() -> str: return str(input('Type the email of the user:')).lower()

def taskName() -> str: return str(input('Type the name of the task:'))
while isRunning:
    print('-------------------')
    print('1. Add user')
    print('2. Remove user')
    print('3. Add Task')
    print('4. Remove Task')
    print('5. Get Users')
    print('6. Users count')
    print('7. Quit CRUD')

    op = int ( input ('Select your option :'))
    match op:
        case 1:
            user_email = email()
            password = str(input('Type your password:'))

            # Creating the object
            new_user = User(email = user_email,password = password)

            # Now calling the method from the class TaskManager
            TaskManager.addUser(new_user)

        case 2 :
            user_email = email()
            
            TaskManager.removeUser(user_email)

        case 3:
            user_email = email()
            TaskManager.addTasks(user_email)
            
        case 4:
            user_email = email() 
            name = taskName()


            TaskManager.removeTask(user_email,name)

        case 5: print(TaskManager.getUser())

        case 6: print(TaskManager.countUsers())

        case 7: isRunning = False

print('Bye!')