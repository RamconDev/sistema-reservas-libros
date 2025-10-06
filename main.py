from models import biblioteca as bib # importando modulo, [biblioteca.py]
import os

os.system("cls")

print("\n********** SISTEMA RESERVAS DE LIBROS ***************\n")

mi_biblioteca = bib.Biblioteca()

# ✅ Ejecutar al iniciar
def cargar_libros():
    mi_biblioteca.add_libro("Alamut")
    mi_biblioteca.add_libro("Lord of the rings")
    mi_biblioteca.add_libro("The Silmarillion")

    return True

# ✅ Opcion menu
def ver_libros():
    mi_biblioteca.ver_libros()

# ✅ Opcion menu
def buscar_libro() :
    buscar = input("Ingresa Nombre o Codigo de libro a buscar: \n")
    resultado = mi_biblioteca.buscar_libro(buscar);

    print(f"\nResultado Busqueda {len(resultado)}\n")
    for libro in resultado:
        print(f"{libro}")

    print("\n")

respuesta = "datos cargados correctamente." if cargar_libros() else "error al cargar los datos."
print(f"* {respuesta}")