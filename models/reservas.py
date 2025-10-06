class Reserva:
    def __init__(self, id, libro_id, usuario_id, f_reserva, f_est_devolucion, f_devolucion):
        self.id = id
        self.libro_id = libro_id
        self.usuario_id = usuario_id
        self.f_reserva = f_reserva
        self.f_est_devolucion = f_est_devolucion
        self.f_devolucion = f_devolucion