dream_vacation = {}

while True:
	name = input("Your name? ")
	if name == 'quit':
		break
	place = input("If you could visit one place in the world, where would you go? ")
	dream_vacation[name] = place

print("\nPoll result")
for name, place in dream_vacation.items():
	print(str(name) + " likes to go to " + str(place))