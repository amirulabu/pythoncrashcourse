favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")

people = ['amirul', 'jen', 'abu', 'sarah', 'edward', 'james']

for name,language in favorite_languages.items():
	if name in people:
		print("Sorry " + str(name) + " you have taken the poll.")
	else: 
		print("Hi, " + str(name) + " you are invited to take the poll")

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are: ")
	for language in languages:
		print("\t" + language.title())