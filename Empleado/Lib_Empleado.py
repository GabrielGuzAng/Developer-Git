# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:38:17 2021

@author: PC-RN80
"""

class Empleado:
    def __init__(self,nombre,tarjeta):
        self.nombre=nombre
        self.tarjeta=tarjeta
        
    def fichar(self):
        self.tarjeta.fichar()
        