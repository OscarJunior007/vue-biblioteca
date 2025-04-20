from pydantic import BaseModel,Field
from uuid import uuid4
from datetime import date
from typing import Optional
class Libro(BaseModel):
    titulo: str
    author: str  
    estado:str = Field(default="Disponible")
    categoria:str
    fecha_publicacion:date 

class editLibro(Libro):
    id:str
    
class User(BaseModel):
    name: str 
    numero_documento:str
    email:str
    password:str   
     
class UserLogin(BaseModel):
    email:str   
    password:str
        
class UserOut(BaseModel):
    id: str
    documento_user:str
    profile:str

class Prestamo(BaseModel):
    id_libro:str
    doc_user : str


class LibroPrestadoOut(BaseModel):
    id:str
    titulo:str
    fecha_prestamo:date
    fecha_devolucion:Optional[date] = Field(default=None)
    fecha_publicacion:date
    
    