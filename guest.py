filename = 'guest.txt'
flag = True

with open(filename, 'a') as file_object:
	while(flag == True):
		name = input("Name: ")
		file_object.write(str(name) + "\n")
		print("Welcome, " + name.title())
		output = input("Fill another name? (y/n) ")
		if(output == 'n' or output == 'N'):
			flag = False
