from app.models.schemas import Libro

class libroService:

    def __init__(self):
        self.lista_libros = []
        self.db_user = {}


    def almacenar_libros(self,libro:Libro) -> bool:   
        for i in self.lista_libros:
            if i['id'] == libro.id:
                print("Ese ID ya esta registrado")
                return False
        self.lista_libros.append(libro.__dict__)
        return True
    
    def listar_libros(self):
        return [libro for libro in self.lista_libros if libro["estado"].lower() != "deshabiltado"]
     
    
    def deshabilitar_libro(self, id) -> bool:
        filtro = list(filter(lambda x: x["id"] == id, self.lista_libros))
        if not filtro:
            return False
        
        libro = filtro[0]

        if libro['estado'] == "deshabiltado":
            return False

        libro['estado'] = "deshabiltado"
        return filtro


