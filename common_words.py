filenames = ['mobydick.txt', 'sherlockholmes.txt', 'dracula.txt', 'test.txt']

for filename in filenames:
	try:
		with open(filename) as file_object:
			total = file_object.read().lower().count('the')
	except FileNotFoundError:
		print("File " + filename + " not found")
	else:
		print(filename + " contains the word 'the' " + str(total) + " times")
		
		
