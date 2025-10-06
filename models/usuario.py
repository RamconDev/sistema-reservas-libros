class Usuario:
    def __init__(self, id, nombre, identificacion, f_registro):
        self.__id = id
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__f_registro = f_registro

    def __str__(self):
        return f'Usuario ("id": {self.__id}, "nombre": {self.__nombre}, "identificacion": {self.__identificacion}, "registro": {self.__registro})'

class Docente(Usuraio):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)
    
    def __str__(self):
        return f'Docente ("id": {self.__id}, "nombre": {self.__nombre}, "identificacion": {self.__identificacion}, "registro": {self.__f_registro})'


class Estudiante(Usuraio):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)

    def __str__(self):
        return f'Estudiante ("id": {self.__id}, "nombre": {self.__nombre}, "identificacion": {self.__identificacion}, "registro": {self.__f_registro})'