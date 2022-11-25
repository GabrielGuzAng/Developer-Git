# -*- coding: utf-8 -*-


class Empleado:
    def __init__(self,nombre,tarjeta):
        self.nombre=nombre
        self.tarjeta=tarjeta
        
    def fichar(self):
        self.tarjeta.fichar()
        