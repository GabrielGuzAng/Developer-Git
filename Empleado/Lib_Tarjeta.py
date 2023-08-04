# -*- coding: utf-8 -*-


# Lib_Tarjeta.py
class Card():
    def __init__(self, number):
        self.number = number
        
        

    def validate_number(self, number):
        # Check if the number is a valid number
        try:
            int(number)
            return True
        except ValueError:
            return False

    def clock_in(self):
        if(self.validate_number(self.number)):
            print(f"Clocking in with card number {self.number}")
        else:
            print(f"Error: Invalid card number {self.number}")
        return self.validate_number(self.number)