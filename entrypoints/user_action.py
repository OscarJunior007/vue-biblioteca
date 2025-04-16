from fastapi import FastAPI,HTTPException,status, APIRouter
from app.models.schemas import Libro,User,UserOut,UserLogin
from app.repository.models import UsuarioModel
from app.repository.database  import get_session
from app.services.user_service import verificar_user,verificar_password
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router =  APIRouter()

@router.post("/api/register-user")
def register_user(user:User):
    try:
        with get_session() as session:
            usuario = UsuarioModel(**user.dict())
            existe_user =  verificar_user(session,usuario.email)
            if existe_user:
                return {"El usuario ya existe"}   
            
            session.add(usuario)
            session.commit()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"Message":"Usuario creado con exito!","user":jsonable_encoder(usuario)})
    except HTTPException as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Ocurrio un error en el servidor {e}")
    
@router.post("/api/login",response_model=UserOut)
def login_user(data:UserLogin):
    try:
        with get_session() as session:
            verificar_email =  verificar_user(session,data.email)
            verificar_pass = verificar_password(session,data.password)
            
        if not verificar_email or not verificar_pass:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Message":"Correo o contra mal escritas"})

        return UserOut(
            id=verificar_email.id,
            documento_user =  verificar_email.numero_documento,
            profile=verificar_email.profile
        ) 
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail=f"No se pudo ingresar el libro :{e}")
