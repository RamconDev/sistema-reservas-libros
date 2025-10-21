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

# ⏯️ Ejecutar al iniciar
def cargar_prestamos():
    mi_biblioteca.add_prestamo(1,1)
    mi_biblioteca.add_prestamo(2,1)
    mi_biblioteca.add_prestamo(4,1)
    mi_biblioteca.add_prestamo(3,1)
    pass

# ✅🌎
def get_elemento(entidad, buscar_fn):
    resultado = None
    while not resultado:
        texto = input(f"Buscar {entidad}: ")
        resultado = buscar_fn(texto)

        if not resultado:
            print(f"* No hay resultados de la busqueda")

    for item in resultado:
        print(f"{item}")

    while True:
        try:
            item_id = int(input(f"\nIndica el id de los resultados: "))
            
            item_encontrado = next(item for item in resultado if item.id == item_id)
            if item_encontrado:
                return item_encontrado
            print(" * ID no encontrado")
        except ValueError:
            print("⚠️ Debes ingresar un numero valido")    

# ✅🌎
def ver_elementos(elementos):
    if elementos:
        for e in elementos:
            print(e)
    else:
        print("* No hay registros para mostrar")

# ✅📖👁️
def ver_libros():
    resultado = mi_biblioteca.ver_libros()
    ver_elementos(resultado)

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
    resultado = mi_biblioteca.ver_usuarios()
    ver_elementos(resultado)
    
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
    user = get_elemento("usuario", mi_biblioteca.buscar_usuario)
    id_user = user.id

    os.system("cls" if os.name == "nt" else "clear")
    
    libro = get_elemento("libro", mi_biblioteca.buscar_libro)
    
    respuesta = mi_biblioteca.add_prestamo(libro.id,id_user)

    if respuesta:
        print(respuesta)
    else:
        print("No se pudo registrar el prestamo")
    
# ✅📝❌
def deshacer_prestamo() :
    user = get_elemento("usuario", mi_biblioteca.buscar_usuario)

    # os.system("cls")
    os.system("cls" if os.name == "nt" else "clear")

    prestamos_activos = mi_biblioteca.ver_prestamos_user(user.id)

    print(f"Usuario:\n{user}\n")
    print("* Lista de prestamos activos:\n")

    if prestamos_activos:
        for prestamo in prestamos_activos:
            print(prestamo)
        
        prestamo_id = 0
        while not prestamo_id:
            prestamo_id = int(input("\nIndique el id del prestamo del libro a devolver: "))

            # os.system("cls")
            os.system("cls" if os.name == "nt" else "clear")

            for prestamo in prestamos_activos:
                if prestamo.id == prestamo_id:
                    respuesta = mi_biblioteca.remove_prestamo(prestamo.id)
                    print(f"Devolucion Registrada:\n{respuesta}")
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
        print("** Prestar Libro 📝 **\n")
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
    # os.system("cls")
    os.system("cls" if os.name == "nt" else "clear")
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
    

    try:
        respuesta = int(input("* Selecciona una opcion: "))
    except ValueError:
        print(f"⚠️* Ingresa una opcion valida")

    # os.system("cls")
    os.system("cls" if os.name == "nt" else "clear")
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