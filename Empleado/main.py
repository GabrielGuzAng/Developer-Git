from Lib_Empleado import Employee
from Lib_Tarjeta import Card

def main():
    card_number = input("\nEnter your card number, please: ")
    card = Card(card_number)

    employee_name = input("\nEnter your name, please: ")
    employee = Employee(employee_name, card)

    employee.clock_in()

if __name__ == "__main__":
    main()