while True:	
	number1 = input("Enter first number(or q to quit): ")
	if number1 == 'q':
		break 
	number2 = input("Enter second number(or q to quit): ")
	if number2 == 'q':
		break 
	try:
		answer = int(number1) + int(number2)
	except TypeError:
		print("Enter only numbers please")
	except ValueError:
		print("Enter only numbers please")
	else:
		print("Sum of " + number1 + " and " + number2 + " is "\
			+ str(answer))