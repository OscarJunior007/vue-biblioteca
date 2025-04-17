from app.repository.models import UsuarioModel
from sqlmodel import Session


def verificar_user(session:Session,email_user:str):
    return session.query(UsuarioModel).filter(UsuarioModel.email == email_user).first()    

def verificar_password(session:Session, password:str):
    return session.query(UsuarioModel).filter(UsuarioModel.password == password).first()    