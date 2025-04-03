from fastapi import FastAPI,HTTPException,status
from app.models.schemas import Libro,User
from app.repository import user_repo
def setup_users(app: FastAPI):
    @app.post("/api/register-user")
    def register_libro(user:User):
        try:
           verificar_user = user_repo.buscar_user(user.email)
           if  verificar_user:
               return {"message":"El usuario ya existe"}
           registro =  user_repo.create_user(user)
           if not registro:
                return {"message":"No se pudo crear el usuario"}
           return {"message":"persona registrada con exto","libro":user.dict()}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")
    
    @app.post("/api/login/{email}")
    def register_libro(email):
        try:
           verificar_user = user_repo.buscar_user(email)

           if not verificar_user:
               return {"message":"El usuario no existe"}
           return {"message":"Usuario encontrado","user":verificar_user}
        except Exception as e:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")
    