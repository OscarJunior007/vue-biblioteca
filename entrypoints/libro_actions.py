from fastapi import FastAPI,HTTPException,status,APIRouter
from fastapi.encoders import jsonable_encoder
from app.repository.database import LibroModel,get_session,UsuarioModel
from app.repository.models import PrestamoModel
from fastapi.responses import JSONResponse
from app.models.schemas import Libro,LibroPrestadoOut
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
        
@router.get("/api/prestar-libro/{id_libro}/{doc_user}")
def prester_libro(id_libro,doc_user):
    try:
        with get_session() as session: 
            libro = session.query(LibroModel).filter(LibroModel.id == id_libro).first()
            user =  session.query(UsuarioModel).filter(UsuarioModel.numero_documento == doc_user).first()
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
                content={"message": "Libro prestado con éxito!"}
            )
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Error interno en el servido {e}")
   
# @router.put("/api/edit-estado-libro/{id}/{estado}")
# def deshabilitar_libro(id,estado):
#     try:
#         libros_recibidos =  libro_repo.estado_libro(id,estado)
#         if not libros_recibidos:
#             return {"message":"No se pudo encontrar ese libro"}
#         return {"message":"Estado del libro actualizado con exito","libro":libros_recibidos}
#     except Exception as e:
#         raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo extraer los libros :{e}")
    
# @router.put("/api/edit-libro")
# def deshabilitar_libro(libro:Libro):
#     try:
#         libros_recibidos =  libro_repo.edit_libro(libro)
#         if not libros_recibidos:
#             return {"message":"No se pudo encontrar ese libro"}
#         return {"message":"Estado del libro actualizado con exito","libro":libro.dict()}
#     except Exception as e:
#         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"No se pudo extraer los libros :{e}")
