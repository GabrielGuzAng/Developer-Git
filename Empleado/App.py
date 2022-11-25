# -*- coding: utf-8 -*-


from Lib_Empleado import Empleado
from Lib_Tarjeta import Tarjeta

t1=Tarjeta(input("\n Enter your card number please \n"))
e1=Empleado((input("\n Enter your name please \n")),t1)
e1.fichar()
