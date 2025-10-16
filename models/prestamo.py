from datetime import date

class Prestamo:
    # 🧩
    def __init__(self, id, libro_id, usuario_id, f_est_devolucion):
        self.__id = id
        self.__libro_id = int(libro_id)
        self.__usuario_id = int(usuario_id)
        self.__f_prestamo = date.today()
        self.__f_est_devolucion = f_est_devolucion
        self.__f_devolucion = ""
    
    def __str__(self):
        return f'Prestamo [id: {self.__id}, libro_id: {self.__libro_id}, usuario_id: {self.__usuario_id}, f_prestamo: {self.__f_prestamo}, f_est_devolucion: {self.__f_est_devolucion}, f_devolucion: {self.__f_devolucion}]'
    
    # 🧩
    @property
    def id(self):
        return self.__id
    
    # 🧩
    @property
    def libro_id(self):
        return self.__libro_id
    
    # 🧩
    @property
    def usuario_id(self):
        return self.__usuario_id
    
    # 🧩
    @property
    def f_prestamo(self):
        return self.__f_prestamo
    
    # 🧩
    @property
    def f_est_devolucion(self):
        return self.__f_est_devolucion
    
    # 🧩
    @property
    def f_devolucion(self):
        return self.__f_devolucion
    @f_devolucion.setter
    def f_devolucion(self, nueva_fecha):
        self.__f_devolucion = nueva_fecha