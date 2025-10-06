# 📦
from . import libro as lib # importando modulo, [libro.py]
from datetime import date

class Biblioteca:
    # 🧩
    def __init__(self):
        self.__libros = []
        self.__id_libro = 0


    # 🧩
    def add_libro(self, nombre):
        id = self.__nuevo_id()
        n_copia = 1
        codigo = f"LIB{self.__id_libro}-{n_copia}"
        nuevo_libro = lib.Libro(id, codigo, nombre, True, date.today())

        self.__libros.append(nuevo_libro)
        return nuevo_libro

    # 🧩
    def ver_libros(self):
        for libro in self.__libros:
            print(libro)

    # 🧩
    def buscar_libro(self, texto):
        libros_encontrados = [
            libro for libro in self.__libros
            if texto in libro.get_nombre() or texto in libro.get_codigo()
        ]
        return libros_encontrados
    
    # 🧩
    def __nuevo_id(self):
        self.__id_libro += 1
        return self.__id_libro