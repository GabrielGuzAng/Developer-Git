# test.py
import unittest
from Lib_Empleado import Employee
from Lib_Tarjeta import Card

class TestEmployeeCard(unittest.TestCase):

    def test_clock_in(self):
        # Test clock_in functionality
        card = Card("1234567890")
        employee = Employee("John Doe", card)

        # Verify that clock_in returns True
        self.assertTrue(employee.clock_in())

    def test_invalid_card(self):
        # Test case when the card is invalid
        card = Card("invalid_card_number")
        employee = Employee("John Doe", card)

        # Verify that clock_in returns False when the card is invalid
        self.assertFalse(employee.clock_in())

if __name__ == '__main__':
    unittest.main()