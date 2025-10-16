# 📦
from . import libro as lib # importando modulo, [libro.py]
from . import usuario as us # importando modulo, [usuario.py]
from . import prestamo as pre # importando modulo, [reserva.py]
from datetime import date, timedelta

class Biblioteca:
    # 🧩
    def __init__(self):
        self.__libros = []
        self.__id_libro = 0
        self.__usuarios = []
        self.__id_usuario = 0
        self.__prestamos = []
        self.__id_prestamo = 0


    # 🧩📗
    def add_libro(self, nombre):
        id = self.__nuevo_id_libro()
        n_copia = 1
        codigo = f"LIB{self.__id_libro}-{n_copia}"
        nuevo_libro = lib.Libro(id, codigo, nombre, True, date.today())

        self.__libros.append(nuevo_libro)
        return nuevo_libro

    # 🧩📗
    def ver_libros(self):
        for libro in self.__libros:
            print(libro)

    # 🧩📗
    # def ver_libros_disponibles(self):
    #     for libro in self.__libros:
    #         if libro.get_disponibilidad():
    #             print(libro)

    # 🧩📗
    def buscar_libro(self, texto):
        # Lista por comprension
        libros_encontrados = [
            libro for libro in self.__libros
            if (texto in libro.nombre or texto in libro.codigo) and libro.disponibilidad
        ]
        return libros_encontrados
    
    # 🧩📗
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
            
    # 🧩👤    
    def buscar_usuario(self, texto):
        usuarios_encontrados = [
            usuario for usuario in self.__usuarios
            if texto in usuario.nombre or texto in usuario.identificacion
        ]
        return usuarios_encontrados
    
    # 🧩👤    
    def __nuevo_id_usuario(self):
        self.__id_usuario += 1
        return self.__id_usuario
    
    # 🧩📝➕
    def add_prestamo(self, libro_id, usuario_id):
        for user in self.__usuarios:
            # Verificar si se puede prestar libro al usuario
            if user.id == usuario_id:
                if user.libros_prestados < user.max_prestamos:
                    today = date.today()
                    f_est_devolucion = today + timedelta(days=15)
                    nuevo_prestamo = pre.Prestamo(self.__nuevo_id_prestamo(), libro_id, usuario_id, f_est_devolucion)
                    
                    # Agregar libro a registro de prestamos
                    self.__prestamos.append(nuevo_prestamo)
                    # Cambiar disponibilidad del libro a no disponible
                    self.__libros[libro_id - 1].disponibilidad = False
                    # Sumar al contador de libros prestados del usuario
                    user.libros_prestados = True
                    return nuevo_prestamo
                else:
                    return f"No se puede hacer el prestamo ha alcanzado el limite permitido ({user.libros_prestados})"
        return False
    
    def remove_prestamo(self, prestamo_id):
        for prestamo in self.__prestamos:
            if (prestamo.id == prestamo_id) :
                prestamo.f_devolucion = date.today()
                user_id = prestamo.usuario_id
                libro_id = prestamo.libro_id

                for user in self.__usuarios:
                    if user.id == user_id:
                        user.libros_prestados = False

                for libro in self.__libros:
                    if libro.id == libro_id:
                        libro.disponibilidad = True

                return prestamo
        return False
            
        
    def ver_prestamos_user(self, id):
        prestamos_activos = []
        for prestamo in self.__prestamos:
            if(prestamo.usuario_id == id and not prestamo.f_devolucion) :
                prestamos_activos.append(prestamo)
        return prestamos_activos

    def ver_prestamos_activos(self):
        prestamos_activos = []
        for prestamo in self.__prestamos:
            if not prestamo.f_devolucion:
                prestamos_activos.append(prestamo)
        return prestamos_activos

    def ver_prestamos(self):
        prestamos_activos = []
        for prestamo in self.__prestamos:
            prestamos_activos.append(prestamo)
        return prestamos_activos
            
    def __nuevo_id_prestamo(self):
        self.__id_prestamo += 1
        return self.__id_prestamo