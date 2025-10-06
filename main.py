# 📦
from models import biblioteca as bib # importando modulo, [biblioteca.py]
import os

# ✅ Ejecutar al iniciar
def cargar_libros():
    mi_biblioteca.add_libro("Alamut")
    mi_biblioteca.add_libro("Lord of the rings")
    mi_biblioteca.add_libro("The Silmarillion")

    return True

# ✅👁️
def ver_libros():
    mi_biblioteca.ver_libros()

# ✅🔍
def buscar_libro() :
    buscar = input("Ingresa Nombre o Codigo de libro a buscar: \n")
    resultado = mi_biblioteca.buscar_libro(buscar);

    print(f"\nResultado Busqueda {len(resultado)}\n")
    for libro in resultado:
        print(f"{libro}")

    print("\n")

# ✅➕
def agregar_nuevo_libro():
    nombre_libro = input("Indique el nombre del libro: ")
    respuesta = mi_biblioteca.add_libro(nombre_libro)
    print (f"\n* Registrado:\n{respuesta}")

# ✅
def encabezado(r = 0):
    print("\n********** SISTEMA RESERVAS DE LIBROS ***************\n")

    if r == 1:
        print("** Lista de libros **\n")
    elif r == 2:
        print("** Agregar nuevo libro **\n")


mi_biblioteca = bib.Biblioteca()
cargar_libros()
# respuesta = "datos cargados correctamente." if cargar_libros() else "error al cargar los datos."
# print(f"* {respuesta}")

while True:
    os.system("cls")
    encabezado()

    print("1. Ver Lista de libros 👁️📚")
    print("2. Agregar nuevo libro ➕📗")
    print("3. Buscar libro 🔍📗")

    respuesta = int(input(""))
    os.system("cls")
    encabezado(respuesta)

    if respuesta == 1:
        ver_libros()
    elif respuesta == 2:
        agregar_nuevo_libro()
    elif respuesta == 3:
        buscar_libro()
    
    print("\n\n")
    os.system("pause")
