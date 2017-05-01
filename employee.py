class Employee():
	"""docstring for Employee"""
	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
	
	def give_raise(self):
		self.annual_salary = self.annual_salary + 5000

	def give_custom_raise(self, raise_amount):
		self.annual_salary = self.annual_salary + raise_amount
