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
        return f'Libro ("id": "{self.__id}", "codigo": "{self.__codigo}", "nombre": "{self.__nombre}", "disponibilidad": {self.__disponibilidad}, "f_registro": {self.__f_registro})'
    
    # 🧩
    def get_id(self):
        return self.__id

    # 🧩
    def get_nombre(self):
        return self.__nombre
    
    # 🧩
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # 🧩
    def get_codigo(self):
        return self.__codigo

    # 🧩
    def set_codigo(self, codigo):
        self.__codigo = codigo

    # 🧩    
    def get_disponibilidad(self):
        return self.__disponibilidad

    # 🧩
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad