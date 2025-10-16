# 📦
from models import biblioteca as bib # importando modulo, [biblioteca.py]
import os

# ⏯️ Ejecutar al iniciar
def cargar_libros():
    mi_biblioteca.add_libro("Alamut")
    mi_biblioteca.add_libro("Lord of the rings")
    mi_biblioteca.add_libro("The Silmarillion")
    mi_biblioteca.add_libro("El principe")
    mi_biblioteca.add_libro("Romeo y mugrienta")
    mi_biblioteca.add_libro("Robinson Crusoe")

    return True

# ⏯️ Ejecutar al iniciar
def cargar_usuarios():
    mi_biblioteca.add_usuario("hector", "2122", 1)
    mi_biblioteca.add_usuario("johan", "1913", 0)
    mi_biblioteca.add_usuario("ana", "1933", 0)
    mi_biblioteca.add_usuario("jose", "2141", 1)
    
    return True

def cargar_prestamos():
    mi_biblioteca.add_prestamo(1,1)
    mi_biblioteca.add_prestamo(2,1)
    mi_biblioteca.add_prestamo(4,1)
    mi_biblioteca.add_prestamo(3,1)
    pass

def get_libro():
    resultado = []
    while not resultado:
        libro = input("Buscar libro por nombre o codigo: ")
        resultado = mi_biblioteca.buscar_libro(libro)
        if not resultado:
            print("* No hay resultados en la busqueda.\n")
    
    print("\n* Resultados de la busqueda:\n")
    for libro in resultado:
        print(libro)
    
    libro = 0
    while not libro:
        libro_input = int(input("\nindique el id del libro: "))
        for lib in resultado:
            if lib.id == libro_input:
                libro = lib
        if not libro:
            print("* no ha seleccionado un elemento del resuldato de la busqueda.\n")
        return libro

def get_usuario():
    resultado = []
    while not resultado:
        usuario = input("Buscar usuario por nombre o identificacion: ")
        resultado = mi_biblioteca.buscar_usuario(usuario)
        if not resultado:
            print("* No hay resultados en la busqueda.\n")
    
    print("\n* Resultados de la busqueda:\n")
    for usuario in resultado:
        print(usuario)
    
    user = 0
    while not user:
        usuario_input = int(input("\nindique el id del usuario: "))
        for usuario in resultado:
            if usuario.get_id() == usuario_input:
                user = usuario
        if not user:
            print("* no ha seleccionado un elemento del resuldato de la busqueda.\n")
    return user
    

# ✅📖👁️
def ver_libros():
    mi_biblioteca.ver_libros()

# ✅📖🔍
def buscar_libro() :
    buscar = input("Ingresa Nombre o Codigo de libro a buscar: \n")
    resultado = mi_biblioteca.buscar_libro(buscar)

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
    
# ✅👤🔍
def buscar_usuario():
    buscar = input("Ingresa Nombre o Identificacion del usuario: \n")
    resultado = mi_biblioteca.buscar_usuario(buscar);

    print(f"\nResultado Busqueda ({len(resultado)})\n")
    for usuario in resultado:
        print(f"{usuario}")

    print("\n")

# ✅👤➕
def agregar_nuevo_usuario():
    nombre = input("Nombre: ")
    identificacion = input("Identificacion: ")
    es_docente = -1
    
    while es_docente != 0 and es_docente != 1:
        es_docente = int(input("0. Docente\n1 Estudiante\n"))
        
    mi_biblioteca.add_usuario(nombre,identificacion,es_docente)
    
# ✅📝👁️
def ver_prestamos():
    respuesta = mi_biblioteca.ver_prestamos()
    if not respuesta:
        print("*** No hay registros")
    else:
        for prestamo in respuesta:
            print(prestamo)

# ✅📝👁️
def ver_prestamos_activos():
    respuesta = mi_biblioteca.ver_prestamos_activos()
    if not respuesta:
        print("*** Actualmente no hay prestamos activos")
    for prestamo in respuesta:
        print(prestamo)
        
# ✅📝➕
def hacer_prestamo():
    user = get_usuario()
    id_user = user.get_id()

    os.system("cls")
    
    libro = get_libro()
    
    respuesta = mi_biblioteca.add_prestamo(libro.id,id_user)

    if respuesta:
        print(respuesta)
    else:
        print("No se pudo registrar el prestamo")
    
# ✅📝❌
def deshacer_prestamo() :
    user = get_usuario()

    os.system("cls")

    prestamos_activos = mi_biblioteca.ver_prestamos_user(user.get_id())

    print(f"Usuario:\n{user}\n")
    print("* Lista de prestamos activos:\n")

    if prestamos_activos:
        for prestamo in prestamos_activos:
            print(prestamo)
        
        prestamo_id = 0
        while not prestamo_id:
            prestamo_id = int(input("\nIndique el id del prestamo del libro a devolver: "))

            os.system("cls")

            for prestamo in prestamos_activos:
                if prestamo.get_id() == prestamo_id:
                    prestamo_id = prestamo.get_id()
                    respuesta = mi_biblioteca.remove_prestamo(prestamo_id)
                    print(f"Devolicion Registrada:\n{respuesta}")
    else :
        print("* El usuario no tiene prestamos activos")


# ✅🚦 Encabezados para cada funcion
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
    elif r == 7:
        print("** Prestar Libro8 📝 **\n")
    elif r == 8:
        print("** Devolver Libro 📝 **\n")
    elif r == 9:
        print("** Prestamos activos 📝 **\n")
    elif r == 10:
        print("** Registros de Prestamos 📝 **\n")


mi_biblioteca = bib.Biblioteca()
cargar_libros()
cargar_usuarios()
cargar_prestamos()

while True:
    os.system("cls")
    encabezado()

    print("\t*** LIBROS 👤👥")
    print("\t1.  Ver Lista de libros 👁️")
    print("\t2.  Agregar nuevo libro ➕")
    print("\t3.  Buscar libro 🔍")
    print("\n\t*** USUARIOS 📖📗")
    print("\t4.  Ver Lista de Usuarios 👁️")
    print("\t5.  Agregar nuevo usuario ➕")
    print("\t6.  Buscar Usuario 🔍")
    print("\n\t*** PRESTAMOS 📝📅")
    print("\t7.  Prestar Libro ➕")
    print("\t8.  Devolver Libro ❌")
    print("\t9.  Ver libros prestados 📝🔍")
    print("\t10. Ver registro de todos los prestamos 📝🔍")
    

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
    elif respuesta == 7:
        hacer_prestamo()
    elif respuesta == 8:
        deshacer_prestamo()
    elif respuesta == 9:
        ver_prestamos_activos()
    elif respuesta == 10:
        ver_prestamos()
    
    print("\n\n")
    os.system("pause")