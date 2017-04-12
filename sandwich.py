sandwich_orders = [
'Tuna', 'pastrami', 'Chicken Breast', 'pastrami', 
'Salad', 'pastrami', 'Meatball', 'Sardine'
]

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

for order in sandwich_orders:
	print("I made you a " + str(order) + " sandwich")
	finished_sandwiches.append(order)

for order in finished_sandwiches:
	print(order)