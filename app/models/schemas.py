from pydantic import BaseModel,Field
from uuid import uuid4

class Libro(BaseModel):
    id:str = Field(default_factory=lambda:str(uuid4()))
    titulo:str
    categoria:str
    author:str
    fecha_publicacion:str
    estado:str | None = "habilitado"


class User(BaseModel):
    id:str = Field(default_factory=lambda:str(uuid4()))
    name:str
    email:str
    password:str
    profile:int | None = 2
