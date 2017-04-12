person = {'first_name': 'Amirul', 'last_name': 'Abu', 'age': 26, 'city': 'Melaka'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

phone_number = {'Amirul': 123321, 'Mary': 390241, 'Larry': 717320}

print(phone_number['Larry'])

person_1 = {'first_name': 'Arif', 'last_name': 'Ahmad', 'age': 33, 'city': 'Kedah'}
person_2 = {'first_name': 'Sean', 'last_name': 'David', 'age': 19, 'city': 'Penang'}
person_3 = {'first_name': 'Hakim', 'last_name': 'Samad', 'age': 23, 'city': 'Kuala Lumpur'}

person_list = [person, person_1, person_2, person_3]

for people in person_list:
	print("Full name: " + str(people['first_name']) + " " + str(people['last_name']))
	print("Age: " + str(people['age']))
	print("City: " + str(people['city'] + "\n"))