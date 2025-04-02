import mysql.connector
from app.models.schemas import User
from fastapi import HTTPException

def ActualiozarBD():
    connection = mysql.connector.connect(user='root', password='12345',
                                         database='biblioteca_python',
                                         port='3306')
    return connection


def create_user(datos: User):
     conexion = ActualiozarBD()
     cursor = conexion.cursor()

     try:
        query = """
            INSERT INTO users (id,name,email,password,profile)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        values =(
            datos.id,
            datos.name,
            datos.password,
            datos.profile
        )   

        cursor.execute(query, values)
        conexion.commit()       
     except Exception as e:
        print(f"error:{e}")
        raise HTTPException(status_code=500, detail=f"ERROR GUARDAR LOS DATOS EN LA DB: {e}")
     finally:
          cursor.close()
          conexion.close()