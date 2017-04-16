class User():

	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print("Name: " + self.first_name.title() + " " \
				+ self.last_name.title() + ", "  \
				+ "\nAge: " + str(self.age) \
				+ "\nLocation: " + str(self.location))

	def greet_user(self):
		print("Hello " + self.first_name.title() + " " \
				+ self.last_name )

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):

	def __init__(self, first_name, last_name, age, location, privileges):
		super().__init__(first_name, last_name, age, location)
		self.privileges = Privileges(privileges)

	
class Privileges():

	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		print("Privileges: " + str(self.privileges))



