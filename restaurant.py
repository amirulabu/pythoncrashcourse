class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(str(self.restaurant_name) + 
				" is serving " + 
				str(self.cuisine_type)) 

	def open_restaurant():
		print("The restaurant is open")


my_restaurant = Restaurant('McDonalds', 'fast food')

# print(my_restaurant.restaurant_name)

my_restaurant.describe_restaurant()