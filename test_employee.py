import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		"""
		Create an employee profile
		"""
		self.employee = Employee("Amirul", "Abu", 60000)
		self.raise_amount = 1000

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 65000)

	def test_give_custom_raise(self):
		self.employee.give_custom_raise(self.raise_amount)
		self.assertEqual(self.employee.annual_salary, 61000)


unittest.main()