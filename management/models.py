from sqlalchemy import Column , String , create_engine, ForeignKey
from sqlalchemy.orm import declarative_base , sessionmaker , relationship 


# Declaring the DataBase here
db = declarative_base()

class Manager(db):

    __tablename__ = 'managers'

    email = Column(String(200),primary_key = True)
    password = Column(String(200), nullable = False)
    sector = Column(String(200) , nullable = False)

    users = relationship("User",back_populates="manager")


    def __repr__(self):
        return f'<(Email ={self.email},password={self.password},sector={self.sector})'
    

    def getUsers(self)-> list[str]:
        if not self.users : 
            return []

        return [user.getName() for user in self.users]
    
    def getCount(self) -> int : return len(self.users) if self.users else 0


    def addUser(self,user:"User") -> None:
        
        existing_user = session.query(User).filter_by(cpf = user.getCPF()).first()

        if existing_user:
            print("This user already exists inside our database")
        else:
            session.add(user)
            session.commit()
            print("User sucessfully added")

    def removerUser(self,cpf:str) -> None:
        
        existing_user = session.query(User).filter_by(cpf = cpf).first()

        if not existing_user:
            print(f"The user does not exists in our Database")
        else:
            session.delete(existing_user)
            session.commit()
            
            print("The user was successfully deleted")

class User(db):
    
    __tablename__ = 'users'

    cpf = Column( String(11), primary_key = True , nullable = False)
    name = Column(String(200), nullable = False)
    sector = Column( String(200) , nullable = False)

    manager_email = Column(String(200),ForeignKey("managers.email"))
    manager = relationship("Manager",back_populates = "users")

    def __repr__(self):
        return f'<(cpf = {self.cpf}, Name = {self.name} , Sector = {self.sector})>'
    

    def getCPF( self ) -> str:
        return self.cpf
    

    def getName( self ) -> str:
        return self.name
    
    def getSector( self ) -> str:
        return self.sector
        

engine = create_engine("mysql+pymysql://root:Ivimorcega1@localhost:3306/management")

Session = sessionmaker( bind = engine )
session = Session()

db.metadata.create_all(engine)