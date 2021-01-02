# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:24:46 2021

@author: PC-RN80
"""

class Tarjeta():
    def __init__(self,numero):
        self.numero=numero
        
    def fichar(self):
        print(f"Fichando con tarjeta número {self.numero}")
    