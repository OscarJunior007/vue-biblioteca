from fastapi import FastAPI,HTTPException,status
from app.repository import libro_repo
from app.models.schemas import Libro
from app.services.libro_service import libroService
def setup_register_libros(app: FastAPI):
    

    @app.post("/api/register-libro")
    def register_libro(libro:Libro):
        try:
           registro =  libro_repo.create_libro(libro)
           if not registro:
                return {"message":"No se pudo ingresar ningun libro"}
           return {"message":"Libro registrado con exito","libro":libro.dict()}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")
    
    @app.get("/api/listar-libros")
    def listar_libros():
        try:
            libros_recibidos =  libro_repo.listar_libros()
            if not libros_recibidos:
                return {"message":"No hay ningun libro para mostrar", "libros":libros_recibidos}
            return {"message":"Libro registrado con exto","libro":libros_recibidos}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
        
    @app.put("/api/edit-estado-libro/{id}/{estado}")
    def deshabilitar_libro(id,estado):
        try:
            libros_recibidos =  libro_repo.estado_libro(id,estado)
            if not libros_recibidos:
                return {"message":"No se pudo encontrar ese libro"}
            return {"message":"Estado del libro actualizado con exito","libro":libros_recibidos}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
        
    @app.put("/api/edit-libro")
    def deshabilitar_libro(libro:Libro):
        try:
            libros_recibidos =  libro_repo.edit_libro(libro)
            if not libros_recibidos:
                return {"message":"No se pudo encontrar ese libro"}
            return {"message":"Estado del libro actualizado con exito","libro":libro.dict()}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
