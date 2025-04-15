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


class User(BaseModel):
    name: str 
    numero_documento:str
    email:str
    password:str    
    profile: str 
    
class Prestamo(BaseModel):
    usuario_id: str
    libro_id : str  
    fecha_prestamo: date =  date.today()
    estado : str =   Field(default="Prestado")


class LibroPrestadoOut(BaseModel):
    nombre_libro:str
    fecha_prestamo:date
    fecha_devolucion:Optional[date] = Field(default=None)
    fecha_publicacion:date
    
    