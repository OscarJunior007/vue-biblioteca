import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from sqlmodel import Session,create_engine,SQLModel



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.repository.models import LibroModel,UsuarioModel

DB_FILE = os.path.join(BASE_DIR, "db.sqlite3")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)


def get_session():
    return Session(engine)



def inserta_user():
    with get_session() as session:
        user = UsuarioModel(name="Oscar Mejia",numero_documento="1082856284",email="oscar@gmail.com",password="12345",profile="ADMIN")
        user2 = UsuarioModel(name="Diego",numero_documento="1082856285",email="diego@gmail.com",password="12345",profile="DEFAULT")
        
        session.add(user)  
        session.add(user2)  
        session.commit()
    print("Usuario creado con éxito")    
    return

def create_table():
    SQLModel.metadata.create_all(engine)
    
if __name__ == '__main__':
    create_table()
    inserta_user()