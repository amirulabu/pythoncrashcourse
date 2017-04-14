# import cars_function
from cars_function import *

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'ferarri'? I predict False")
print(car == 'ferarri')

print("Is 'audi' in cars? I guess True.")
print('audi' in cars)

print("Is 'ferarri' not in cars? I guess True.")
print('ferarri' not in cars)

print("Is 'bmw' and 'subaru in cars? I guess True")
print('bmw' in cars and 'subaru' in cars)

print("Is 'nissan' or 'honda' in cars? I guess False")
print('nissan' in cars or 'honda' in cars)




my_car = make_car('Nissan', 'Almera', engine=1.5, color='white')
print(my_car)
