# 🏛️
class Usuario:
    def __init__(self, id, nombre, identificacion, f_registro):
        self.__id = int(id)
        self.__nombre = nombre.lower()
        self.__identificacion = identificacion.lower()
        self.__f_registro = f_registro
        self.__libros_prestados = 0

    def __str__(self):
        return f'{str("usuario"):11} [id: {self.__id}, libros_prestados: {self.__libros_prestados}, registro: {self.__f_registro}, identificacion: {str(self.__identificacion):9}, nombre: {self.__nombre}]'

    # 🧩
    @property
    def id(self):
        return self.__id

    # 🧩
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre.lower()

    # 🧩
    @property
    def identificacion(self):
        return self.__identificacion
    @identificacion.setter
    def identificacion(self, nueva_identificacion):
        self.__identificacion = nueva_identificacion
    
    # 🧩
    @property
    def f_registro(self):
        return self.__f_registro
    
    @property
    def libros_prestados(self):
        return self.__libros_prestados
    @libros_prestados.setter
    def libros_prestados(self, se_presto = True):
        if se_presto:
            self.__libros_prestados += 1
        else:
            self.__libros_prestados -= 1

# 🏛️
class Docente(Usuario):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)
        self.__max_libros = 8
    
    def __str__(self):
        return f'{str("Docente"):11} [id: {self.id}, registro: {self.f_registro}, max_libros: {self.__max_libros}, libros_prestados: {self.libros_prestados}, identificacion: {self.identificacion}, nombre: {self.nombre}]'
    
    @property
    def max_prestamos(self):
        return self.__max_libros
    @max_prestamos.setter
    def max_prestamos(self, nuevo_max_libros):
        self.__max_libros = nuevo_max_libros

# 🏛️
class Estudiante(Usuario):
    def __init__(self, id, nombre, identificacion, f_registro):
        super().__init__(id, nombre, identificacion, f_registro)
        self.__max_libros = 3

    def __str__(self):
        return f'{str("Estudiante"):11} [id: {self.id}, registro: {self.f_registro}, max_libros: {self.__max_libros}, libros_prestados: {self.libros_prestados}, identificacion: {self.identificacion}, nombre: {self.nombre}]'
    
    @property
    def max_prestamos(self):
        return self.__max_libros
    @max_prestamos.setter
    def max_prestamos(self, nuevo_max_libros):
        self.__max_libros = nuevo_max_libros