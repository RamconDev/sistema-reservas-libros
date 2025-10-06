# 🏛️
class Usuario:
    def __init__(self, id, nombre, identificacion, f_registro):
        self.__id = int(id)
        self.__nombre = nombre.lower()
        self.__identificacion = identificacion.lower()
        self.__f_registro = f_registro

    def __str__(self):
        return f'Usuario ("id": {self.__id}, "nombre": {self.__nombre}, "identificacion": {self.__identificacion}, "registro": {self.__f_registro})'

    # 🧩
    def get_id(self):
        return self.__id

    # 🧩
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre.lower()

    # 🧩
    def get_identificacion(self):
        return self.__identificacion
    def set_identificacion(self, identificacion):
        self.__identificacion = identificacion.lower()
    
    # 🧩
    def get_f_registro(self):
        return self.__f_registro

# 🏛️
class Docente(Usuario):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)
        self.__max_libros = 8
    
    def __str__(self):
        return f'Docente ("id": {self.get_id()}, "nombre": {self.get_nombre()}, "identificacion": {self.get_identificacion()}, "registro": {self.get_f_registro()}, "max_libros": {self.__max_libros})'

# 🏛️
class Estudiante(Usuario):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)
        self.__max_libros = 3

    def __str__(self):
        return f'Estudiante ("id": {self.get_id()}, "nombre": {self.get_nombre()}, "identificacion": {self.get_identificacion()}, "registro": {self.get_f_registro()}, "max_libros": {self.__max_libros})'