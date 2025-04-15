from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import date, datetime
from uuid import uuid4


class LibroModel(SQLModel, table = True):
    __tablename__ =  "libros"
    id: str = Field(default_factory=lambda: str(uuid4()),primary_key=True)
  
    titulo: str
    author: str  
    estado:str
    categoria:str
    fecha_publicacion:date 
    
    prestamos: List["PrestamoModel"] = Relationship(back_populates="libro")

class UsuarioModel(SQLModel, table = True):
    __tablename__ =  "users"
    id: str = Field(default_factory=lambda: str(uuid4()),primary_key=True)
    name: str 
    numero_documento:str
    email:str
    password:str    
    profile: str = Field(default="DEFAULT")
    
    prestamos: List["PrestamoModel"] = Relationship(back_populates="usuario")

    
class PrestamoModel(SQLModel, table=True):
    __tablename__ = "prestamos"
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    
    usuario_id: str = Field(foreign_key="users.id")
    libro_id: str = Field(foreign_key="libros.id")
    
    fecha_prestamo: date = Field(default_factory=date.today)
    fecha_devolucion: Optional[date] = None
    estado: str = Field(default="Prestado")  # o "Devuelto", "Atrasado", etc.
    
    usuario: Optional["UsuarioModel"] = Relationship(back_populates="prestamos")
    libro: Optional["LibroModel"] = Relationship(back_populates="prestamos")
