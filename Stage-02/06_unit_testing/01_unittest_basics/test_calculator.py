#unit test is use for chec if our function runs correctly or not

import unittest
from calculator import add,subtract,multiply,divide

class testFunc(unittest.TestCase):
    def setUp(self):        #calls before every test method
        print("setup called")

    def tearDown(self):          #calls after every test method
        print("Teardown called")

    def test_add(self):
        print("test runs")
        self.assertEqual(add(10,5),15)

    def test_substract(self):
        self.assertEqual(subtract(2,5),-3)

    def test_multiply(self):
        self.assertEqual(multiply(10,5),50)

    def test_divide(self):
        self.assertEqual(divide(10,5),2)

# it checks "Does my function correctly raise ZeroDivisionError when someone tries to divide by zero?"
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError , divide ,10, 0 )

#when file runs this runs unittest test runner 
if __name__ == "__main__":
    unittest.main()