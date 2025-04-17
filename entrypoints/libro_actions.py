from fastapi import FastAPI,HTTPException,status,APIRouter
from fastapi.encoders import jsonable_encoder
from app.repository.database import LibroModel,get_session,UsuarioModel
from app.repository.models import PrestamoModel
from fastapi.responses import JSONResponse
from app.models.schemas import Libro,LibroPrestadoOut,Prestamo,editLibro
from app.services import libro_service
from datetime import date
from typing import List

router = APIRouter(tags=["Rutas libros"])    

@router.post("/api/register-libro")
def register_libro(libro:Libro):
    try:
       with get_session() as session:
           session.add(LibroModel(**libro.dict()))
           session.commit()
       return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Libro registrado con exito","libro":jsonable_encoder(libro)})
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")

@router.get("/api/listar-libros")
def listar_libros():
    try:
       with get_session() as session:
           return session.query(LibroModel).all()
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
    
@router.get("/api/listar-libros-by-id-users/{id}",response_model=List[LibroPrestadoOut])
def listar_libros_by_id(id):
    try:    
        with get_session() as session:  
          
            libro = libro_service.libros_prestados_by_user(session,id)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"libros":jsonable_encoder(libro)})

    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
        
@router.post("/api/prestar-libro", response_model=PrestamoModel)
def prester_libro(data:Prestamo):
    try:
        with get_session() as session: 
            libro = session.query(LibroModel).filter(LibroModel.id == data.id_libro).first()
            user =  session.query(UsuarioModel).filter(UsuarioModel.numero_documento == data.doc_user).first()
            if not libro or not user:
                return JSONResponse(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content={"message": "Libro o usuario no encontrados"}
                )
            if libro.estado != "Disponible":
                return JSONResponse(
                    status_code=status.HTTP_409_CONFLICT,
                    content={"message": "El libro no está disponible para préstamo"}
                ) 
            nuevo_prestamo = PrestamoModel(
                usuario_id=user.id,
                libro_id=libro.id,
                fecha_prestamo=date.today(),
                estado="Prestado"
            )
            session.add(nuevo_prestamo)
            libro.estado = "Prestado"
            session.commit()
            
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message":"libro prestado con exito","libro":jsonable_encoder(data.dict())}
            )
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Error interno en el servido {e}")
   
    
@router.put("/api/edit-libro")
def editar_libro(libro:editLibro):
    try:
        with get_session() as session: 
            
            libros_recibidos =  session.query(LibroModel).filter(LibroModel.id == libro.id).first()
            if libros_recibidos:
                libros_recibidos.titulo = libro.titulo
                libros_recibidos.author = libro.author
                libros_recibidos.categoria = libro.categoria
                libros_recibidos.fecha_publicacion = libro.fecha_publicacion
                session.commit()
                return JSONResponse(status_code=status.HTTP_200_OK, content={"libros":jsonable_encoder(libro.dict())})
                
            return {"message":"No se encontro el libro"}
                
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"No se pudo extraer los libros :{e}")


@router.get("/api/libro/{estado}",response_model=List[LibroModel])
def obtener_libros_by_estado(estado: str):
    try:    
        with get_session() as session:
            libros = session.query(LibroModel).filter(LibroModel.estado == estado).all()
            if not libros:
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"Message":"No se encontro libros con ese estado"})  
            return JSONResponse(status_code=status.HTTP_200_OK, content={"libros":jsonable_encoder(libros)})
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"No se pudo extraer los libros :{e}")
    
@router.put("/api/libro/disabled/{id}")
def deshabilitar_libro(id:str):
    try:
        with get_session() as session:
            libro = session.query(LibroModel).filter(LibroModel.id == id).first()
            if not libro:
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"Message":"No se encontro el libro con ese id"})
            if libro.estado.lower() != "disponible":
                return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"Message":"No puedes deshabilitar este libro su estado no es disponible"})  
                
            libro.estado = "Deshabilitado"  
            session.commit()
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"Libro":jsonable_encoder(libro)})
               
            
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"No se pudo deshabilitar el libro {e}")
    
@router.put("/api/libro/devolver/{id}")
def devolver_libro(id:str): 
    try:    
        with get_session() as session:
             libro_prestado = session.query(PrestamoModel).filter(PrestamoModel.libro_id == id).first()
             libro = session.query(LibroModel).filter(LibroModel.id == id).first()
             
             if not libro_prestado:
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={"Message":"No se encontro el libro con ese id"})
            
             if libro_prestado.estado != "Prestado":
                return JSONResponse(status_code=status.HTTP_200_OK,content={"Message":"El estado del libro no es Prestado"})
            
             libro_prestado.estado = "Devuelto" 
             libro_prestado.fecha_devolucion = date.today()
             libro.estado ="Disponible"
             session.commit()
             return JSONResponse(status_code=status.HTTP_200_OK,content={"Message":"Libro devuelto"})
             
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"No se pudo devolver el libro {e}")
            
                

            
               
            
            