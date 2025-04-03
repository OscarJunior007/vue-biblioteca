import mysql.connector
from fastapi import HTTPException,status

class Database:
    def __init__(self,user, password, database, port):
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        self.cursor = None

    def conectar_db(self) ->  bool:
        try:
           conexion = self.connection = mysql.connector.connect(
                user = self.user,
                password = self.password,
                database =  self.database,
                port = self.port
            )

           if not conexion:
              print("No se conecto a la db")  
              return False
           
           self.cursor = self.connection.cursor(dictionary=True)
           print("Se conecto a la db")
           return True
              
        except mysql.connector.Error as e:
            print(f"Ocurrio un error {e}")
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Ocurrio un error {e}")
        
    def ejecutar_consulta(self,query,valores = None):
        "SELECT,UPDATE,DELETE,INSERT"
        try:
            self.cursor.execute(query,valores)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.rowcount
        except mysql.connector.Error as e:
            print(f"Ocurrio un error{e}")
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Ocurrio un error {e}")

    
    def cerrar_conexion(self):
     
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexión cerrada")