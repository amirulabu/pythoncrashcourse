magicians = ['alice', 'david', 'carolina', 'copperfield', 'jones']
print(magicians[:3])
print(magicians[1:4])
print(magicians[2:])

pizzas = ['pepperoni', 'vegetable', 'extra cheese']
friends_pizzas = pizzas[:]

pizzas.append('hawaiian')
friends_pizzas.append('chicken supreme')

print(pizzas)
print(friends_pizzas) 

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
friends_foods.append('burger')

for x in my_foods:
	print(x)

for y in friends_foods:
	print(y)