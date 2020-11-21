import unittest
from main import crud
from methods import methods

"""
By: Haliima Ahmed
Course:CST8333 Programming Language Research Project
Professor Name:Stanley Pieda
Assignment: 3
Due: March 4th,2020
This is the unit test of the program. using a testing framework this program will test one part (displaying the records) of the program 
"""

"""UNIT TEST FROM ASSIGNMENT #3"""
class Methods_test(unittest.TestCase):
    # local instance
    crud = methods()
    # csv records are loaded
    recordObj = crud.reload()

    # test the display function to check if the program is performing properly
    def testDisplay(self):
        crud.display()
        record = crud.main[len(crud.main)]
        test = methods(self.testDisplay)
        # testing using assertEquals. if it fails and the test failed and the user will be notified.
        self.assertEqual(test, record.REF_DATE)
        self.assertEqual(test, record.GEO)
        self.assertEqual(test, record.DGUID)
        self.assertEqual(test, record.Sex)
        self.assertEqual(test, record.Age_group)
        self.assertEqual(test, record.Student_response)
        self.assertEqual(test, record.UOM)
        self.assertEqual(test, record.UOM_ID)
        self.assertEqual(test, record.SCALAR_FACTOR)
        self.assertEqual(test, record.SCALAR_ID)
        self.assertEqual(test, record.VECTOR)
        self.assertEqual(test, record.COORDINATE)
        self.assertEqual(test, record.STATUS)
        self.assertEqual(test, record.VALUE)
        self.assertEqual(test, record.SYMBOL)
        self.assertEqual(test, record.TERMINATED)
        self.assertEqual(test, record.DECIMALS)
        print("unit test halima ahmed ")


if __name__ == '__main__':
    unittest.main()
