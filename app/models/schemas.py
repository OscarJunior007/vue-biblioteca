from pydantic import BaseModel

class Libro(BaseModel):
    id:int
    titulo:str
    categoria:str
    author:str
    year:str
    estado:str