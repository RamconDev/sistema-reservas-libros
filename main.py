# 📦
from models import biblioteca as bib # importando modulo, [biblioteca.py]
import os

# ⏯️ Ejecutar al iniciar
def cargar_libros():
    mi_biblioteca.add_libro("Alamut")
    mi_biblioteca.add_libro("Lord of the rings")
    mi_biblioteca.add_libro("The Silmarillion")

    return True

# ⏯️ Ejecutar al iniciar
def cargar_usuarios():
    mi_biblioteca.add_usuario("hector", "2122", 1)
    mi_biblioteca.add_usuario("johan", "1913", 0)
    mi_biblioteca.add_usuario("ana", "1933", 0)
    mi_biblioteca.add_usuario("jose", "2141", 1)
    
    return True

# ✅📖👁️
def ver_libros():
    mi_biblioteca.ver_libros()

# ✅📖🔍
def buscar_libro() :
    buscar = input("Ingresa Nombre o Codigo de libro a buscar: \n")
    resultado = mi_biblioteca.buscar_libro(buscar);

    print(f"\nResultado Busqueda {len(resultado)}\n")
    for libro in resultado:
        print(f"{libro}")

    print("\n")

# ✅📖➕
def agregar_nuevo_libro():
    nombre_libro = input("Indique el nombre del libro: ")
    respuesta = mi_biblioteca.add_libro(nombre_libro)
    print (f"\n* Registrado:\n{respuesta}")

# ✅👤👁️
def ver_usuarios():
    mi_biblioteca.ver_usuarios()
    
# ✅👤🔎
def buscar_usuario():
    pass

# ✅👤➕
def agregar_nuevo_usuario():
    nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")
    es_docente = -1
    
    while es_docente != 0 and es_docente != 1:
        es_docente = int(input("0. Docente\n1 Estudiante\n"))
        
    mi_biblioteca.add_usuario(nombre,identificacion,es_docente)

# ✅
def encabezado(r = 0):
    print("********** SISTEMA RESERVAS DE LIBROS ***************\n")

    if r == 1:
        print("** Lista de libros **\n")
    elif r == 2:
        print("** Agregar nuevo libro **\n")
    elif r == 3:
        print("** Buscar libro 🔎 **\n")
    elif r == 4:
        print("** Lista de usuarios **\n")
    elif r == 5:
        print("** Agregar nuevo usuario **\n")
    elif r == 6:
        print("** Buscar usuario 🔎 **\n")


mi_biblioteca = bib.Biblioteca()
cargar_libros()
cargar_usuarios()
# respuesta = "datos cargados correctamente." if cargar_libros() else "error al cargar los datos."
# print(f"* {respuesta}")

while True:
    os.system("cls")
    encabezado()

    print("\t*** LIBROS 👤👥")
    print("\t1. Ver Lista de libros 👁️")
    print("\t2. Agregar nuevo libro ➕")
    print("\t3. Buscar libro 🔍")
    print("\n\t*** USUARIOS 📖📗")
    print("\t4. Ver Lista de Usuarios 👁️")
    print("\t5. Agregar nuevo usuario ➕")
    print("\t6. Buscar Usuario 🔍")
    print("\n\t*** PRESTAMOS 📝📅")
    print("\t7. Prestar Libro ➕")
    print("\t8. Devolver Libro ❌")
    print("\t8. Ver libros prestados 📝🔍")
    

    respuesta = int(input(""))
    os.system("cls")
    encabezado(respuesta)

    if respuesta == 1:
        ver_libros()
    elif respuesta == 2:
        agregar_nuevo_libro()
    elif respuesta == 3:
        buscar_libro()
    elif respuesta == 4:
        ver_usuarios()
    elif respuesta == 5:
        agregar_nuevo_usuario()
    elif respuesta == 6:
        buscar_usuario()
    
    print("\n\n")
    os.system("pause")
