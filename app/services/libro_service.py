from app.models.schemas import Libro
from sqlmodel import Session
from app.repository.models import LibroModel
from app.repository.models import PrestamoModel
from app.models.schemas import LibroPrestadoOut

def libros_prestados_by_user(session:Session,id):
    prestamos = session.query(PrestamoModel).filter(PrestamoModel.usuario_id == id).all()

    libros_prestados = []

    for prestamo in prestamos:
        libro = session.query(LibroModel).filter(LibroModel.id == prestamo.libro_id).first()
        if libro:
            libros_prestados.append(LibroPrestadoOut(
                id=libro.id,
                titulo=libro.titulo,
                fecha_prestamo=prestamo.fecha_prestamo,
                fecha_devolucion=prestamo.fecha_devolucion,
                fecha_publicacion=libro.fecha_publicacion
            ))
    return libros_prestados 

    