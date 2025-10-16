class Libro:
    # 🧩
    def __init__(self, id, codigo, nombre, disponibilidad, f_registro):
        self.__id = int(id)
        self.__codigo = codigo.lower()
        self.__nombre = nombre.lower()
        self.__disponibilidad = bool(disponibilidad)
        self.__f_registro = f_registro

    # 🧩
    def __str__(self):
        return f'Libro [id: {self.__id}, codigo: {self.__codigo}, f_registro: {self.__f_registro}, disponibilidad: {str(self.__disponibilidad):5}, nombre: {self.__nombre}]'
    
    # 🧩
    @property
    def id(self):
        return self.__id

    # 🧩
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre.lower()

    # 🧩
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo.lower()

    # 🧩
    @property
    def disponibilidad(self):
        return self.__disponibilidad
    @disponibilidad.setter
    def disponibilidad(self, nueva_disponibilidad):
        self.__disponibilidad = nueva_disponibilidad