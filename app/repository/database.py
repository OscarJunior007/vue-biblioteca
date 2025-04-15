import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from sqlmodel import Session,create_engine,SQLModel



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from app.repository.models import LibroModel,UsuarioModel

DB_FILE = os.path.join(BASE_DIR, "db.sqlite3")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)


def get_session():
    return Session(engine)




# def insertar():
#     with get_session() as session:
#         habitacion = HabitacionModel(tipo_habitacion="Sencilla", imagen="https://symphony.cdn.tambourine.com/_fusion/zuana-beach-resort/media/zuanabeachresort-habitaciones-estandar-gallery-02-64495380ef638.webp", precio=100000,disponibilidad=True,descripcion="Habitación cómoda y funcional para una persona, ideal para estancias cortas.",cantidad_personas=1)
#         habitacion_1 = HabitacionModel(
#             tipo_habitacion="Pent House",
#             imagen="https://symphony.cdn.tambourine.com/_fusion/zuana-beach-resort/media/zuanabeachresort-habitaciones-penthouse-gallery-01-644957b177361.webp",
#             precio=50000,
#             disponibilidad=True,
#             descripcion="Exclusiva y lujosa, con vistas panorámicas y todas las comodidades de alto nivel.",
#             cantidad_personas=4
#         )

#         habitacion_2 = HabitacionModel(
#             tipo_habitacion="Doble",
#             imagen="https://symphony.cdn.tambourine.com/_fusion/zuana-beach-resort/media/suitehotelzuana-64fa395d01f2d.webp",
#             precio=250000,
#             disponibilidad=True,
#             descripcion="Espaciosa y confortable, perfecta para dos personas, equipada con todo lo necesario.",
#             cantidad_personas=2
#         )

#         habitacion_3 = HabitacionModel(
#             tipo_habitacion="Suite",
#             imagen="https://symphony.cdn.tambourine.com/_fusion/zuana-beach-resort/media/suites-zuana-66e846a17e780.webp",
#             precio=300000,
#             disponibilidad=True,
#             descripcion="Elegante y sofisticada, con áreas separadas de dormitorio y sala de estar.",
#             cantidad_personas=4
#         )

#         habitacion_4 = HabitacionModel(
#             tipo_habitacion="Familiar",
#             imagen="https://www.hotelescolsubsidio.com/media/uploads/galeriahabitaciones/estandar-lanceros_8nt9r3n.jpg?q=pr:sharp/rs:fill/w:740/h:525/f:jpg",
#             precio=350000,
#             disponibilidad=True,
#             descripcion="Amplia y conveniente para familias, con espacio adicional para acomodar a todos.",
#             cantidad_personas=6
#         )

#         habitacion_5 = HabitacionModel(            
#             tipo_habitacion="Junior Suite",
#             imagen="https://d2apges1zx42ya.cloudfront.net/cache/img/hotel-le-basile-habitaciones-triples-127619-1920-1080-auto.jpg?q=1689700200",
#             precio=400000,
#             disponibilidad=True,
#             descripcion="Combinación perfecta de lujo y comodidad, ideal para viajeros de negocios y placer.",
#             cantidad_personas=2
#         ) 
#         session.add(habitacion)
#         session.add(habitacion_1) 
#         session.add(habitacion_2)
#         session.add(habitacion_3)
#         session.add(habitacion_4)
#         session.add(habitacion_5)
#         session.commit()
#     print("Habitación creada con éxito")    
#     return

def inserta_user():
    with get_session() as session:
        user = UsuarioModel(name="Oscar Mejia",numero_documento="1082856284",email="oscar@gmail.com",password="12345",profile="ADMIN")
        user2 = UsuarioModel(name="Diego",numero_documento="1082856285",email="diego@gmail.com",password="12345",profile="DEFAULT")
        
        session.add(user)  
        session.add(user2)  
        session.commit()
    print("Usuario creado con éxito")    
    return

def create_table():
    SQLModel.metadata.create_all(engine)
    
if __name__ == '__main__':
    create_table()
    inserta_user()