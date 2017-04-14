magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	print(magician.title() + ", that was a great trick")

print("Thank you, everyone. That was a great magic show!")

# example for loops
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	great_magicians = []
	for magician in magicians:
		magician = "Great " + str(magician.title())
		great_magicians.append(magician)
	return great_magicians

great_magicians = make_great(magicians)

show_magicians(great_magicians)
show_magicians(magicians)