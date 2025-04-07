from app.services.db_service import Database
from app.models.schemas import User
from fastapi import HTTPException,status


def create_user(user:User):


    db = Database('root','12345','biblioteca_python','3307','127.0.0.1')
    
    try:
        
        connection = db.conectar_db()

        if connection:
            db.ejecutar_consulta("INSERT INTO users (id,name,email,password,profile) VALUES(%s,%s,%s,%s,%s)",(user.id,user.name,user.email,user.password,user.profile))
            db.cerrar_conexion()
            return True
        return False

        
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f" ocurrio un error {e}")
    
def buscar_user(email):
     db = Database('root','12345','biblioteca_python','3307','127.0.0.1')

     try:
        db.conectar_db()  

       
        resultado = db.ejecutar_consulta("SELECT * FROM users WHERE email = %s", (email,))
        
 
        db.cerrar_conexion()  

        return [dato for dato in resultado]
      
     except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Ocurrió un error: {e}")
    