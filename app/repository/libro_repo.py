from app.services.db_service import Database
from app.models.schemas import Libro
from fastapi import HTTPException,status


def create_libro(libro:Libro):


    db = Database('root','12345','biblioteca_python','3307','127.0.0.1')

    
    try:
        
        connection = db.conectar_db()

        if connection:
            db.ejecutar_consulta("INSERT INTO libros (id,titulo,author,estado,categoria,fecha_publicacion) VALUES(%s,%s,%s,%s,%s,%s)",(libro.id,libro.titulo,libro.author,libro.estado,libro.categoria,libro.fecha_publicacion))
            db.cerrar_conexion()
            return True
        return False

        
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f" ocurrio un error {e}")
    

def estado_libro(estado,id):
    db = Database('root','12345','biblioteca_python','3307','127.0.0.1')

    
    try:
        
        connection = db.conectar_db()

        if connection:
            libro_actualizado = db.ejecutar_consulta("UPDATE libros SET estado = %s where id = %s",(id,estado,))
            db.cerrar_conexion()
            return libro_actualizado
        return False

        
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f" ocurrio un error {e}")
    
def listar_libros():
    db = Database('root','12345','biblioteca_python','3307','127.0.0.1')

    
    try:
        
        connection = db.conectar_db()

        if connection:
            libros = db.ejecutar_consulta("SELECT * FROM libros")
            db.cerrar_conexion()
            return [libro for libro in libros if libro["estado"] != "deshabilitado"]
        return False

        
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f" ocurrio un error {e}")
