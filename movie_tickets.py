age = input("Welcome to X Cinema! How old are you? \n")
while age != 'quit':
	age = int(age)
	if age > 12: 
		print("Ticket price is $15")
	elif age > 3 and age <= 12:
		print("Ticket price is $10")
	elif age <= 3:
		print("Ticket is free")
	age = input("Welcome to X Cinema! How old are you? \n")




# while True:
# 	age = input("Welcome to X Cinema! How old are you? \n")
# 	if age != "quit":
# 		age = int(age)
# 		if age > 12: 
# 			print("Ticket price is $15")
# 		elif age > 3 and age <= 12:
# 			print("Ticket price is $10")
# 		elif age <= 3:
# 			print("Ticket is free")
# 	else:
# 		break



# flag = True
# while flag:
# 	age = input("Welcome to X Cinema! How old are you? \n")
# 	if age != "quit":
# 		age = int(age)
# 		if age > 12: 
# 			print("Ticket price is $15")
# 		elif age > 3 and age <= 12:
# 			print("Ticket price is $10")
# 		elif age <= 3:
# 			print("Ticket is free")
# 	else:
# 		flag = False