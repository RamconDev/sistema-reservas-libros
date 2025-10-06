# 📦
from . import libro as lib # importando modulo, [libro.py]
from . import usuario as us # importando modulo, [libro.py]
from datetime import date

class Biblioteca:
    # 🧩
    def __init__(self):
        self.__libros = []
        self.__id_libro = 0
        self.__usuarios = []
        self.__id_usuario = 0


    # 🧩📖
    def add_libro(self, nombre):
        id = self.__nuevo_id_libro()
        n_copia = 1
        codigo = f"LIB{self.__id_libro}-{n_copia}"
        nuevo_libro = lib.Libro(id, codigo, nombre, True, date.today())

        self.__libros.append(nuevo_libro)
        return nuevo_libro

    # 🧩📖
    def ver_libros(self):
        for libro in self.__libros:
            print(libro)

    # 🧩📖
    def buscar_libro(self, texto):
        libros_encontrados = [
            libro for libro in self.__libros
            if texto in libro.get_nombre() or texto in libro.get_codigo()
        ]
        return libros_encontrados
    
    # 🧩📖
    def __nuevo_id_libro(self):
        self.__id_libro += 1
        return self.__id_libro
    
    #🧩👤
    def add_usuario(self, nombre, identificacion, tipo):
        id = self.__nuevo_id_usuario()
        nuevo_usuario = ''
        
        if tipo == 0:
            nuevo_usuario = us.Docente(id,nombre,identificacion, date.today())
        elif tipo == 1:
            nuevo_usuario = us.Estudiante(id,nombre,identificacion, date.today())
            
        self.__usuarios.append(nuevo_usuario)
        
        return nuevo_usuario
        
    # 🧩👤
    def ver_usuarios(self):
        for usuario in self.__usuarios:
            print(usuario)
        
    def __nuevo_id_usuario(self):
        self.__id_usuario += 1
        return self.__id_usuario