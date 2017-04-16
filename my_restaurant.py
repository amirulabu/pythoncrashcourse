from restaurant import Restaurant, IceCreamStand
# or this, but not recomended ->  from restaurant import * 

my_restaurant = Restaurant('McDonalds', 'fast food')

# print(my_restaurant.restaurant_name)

my_restaurant.describe_restaurant()

restaurant = Restaurant('Mek Shop', 'Malay')
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)



my_ice_cream_stand = IceCreamStand('Baskin Robins', 'Ice Cream', ['vanilla', 'chocolate'])

print(my_ice_cream_stand.restaurant_name)
print(my_ice_cream_stand.cuisine_type)
print(my_ice_cream_stand.flavors)