from random import randint

def roll_die(sides,times):
	counter = 1
	while(counter <= times):
		random_number = randint(1, sides)
		print(random_number)
		counter+= 1


print("Roll a dice with 6 sides, 10 times")
roll_die(6,10)

print("Roll a dice with 10 sides, 10 times")
roll_die(10,10)

print("Roll a dice with 20 sides, 10 times")
roll_die(20,10)