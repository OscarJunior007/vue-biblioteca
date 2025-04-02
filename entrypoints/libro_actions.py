from fastapi import FastAPI,HTTPException,status
from app.models.schemas import Libro
from app.services.libro_service import libroService
def setup_register_libros(app: FastAPI):
    
    libros =  libroService()
    @app.post("/api/register-libro")
    def register_libro(libro:Libro):
        try:
           registro =  libros.almacenar_libros(libro)
           if not registro:
                return {"message":"El libro que intentas ingresar ya existe"}
           return {"message":"Libro registrado con exto","libro":libro.dict()}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")
    
    @app.get("/api/listar-libros")
    def listar_libros():
        try:
            libros_recibidos =  libros.listar_libros()
            if not libros_recibidos:
                return {"message":"No hay ningun libro para mostrar", "libros":libros_recibidos}
            return {"message":"Libro registrado con exto","libro":libros_recibidos}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
        
    @app.put("/api/disable-libro")
    def deshabilitar_libro(libro:Libro):
        try:
            libros_recibidos =  libros.deshabilitar_libro(libro.id)
            if not libros_recibidos:
                return {"message":"No se pudo encontrar ese libro"}
            return {"message":"Libro deshabilitado con exto","libro":libros_recibidos}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
