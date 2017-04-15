class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(str(self.restaurant_name) + 
				" is serving " + 
				str(self.cuisine_type)) 

	def open_restaurant():
		print("The restaurant is open")

	def set_number_served(self, number_customer):
		self.number_served = number_customer

	def increment_number_served(self, number_customer):
		self.number_served += number_customer


my_restaurant = Restaurant('McDonalds', 'fast food')

# print(my_restaurant.restaurant_name)

my_restaurant.describe_restaurant()

restaurant = Restaurant('Mek Shop', 'Malay')
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)
