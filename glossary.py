dictionary = {
	'if': 'A type of statement that will pass when true',
	'loop': 'To repeat an action',
	'string': 'text',
	'integer': 'round number including negative numbers',
	'dictionary': 'A type of data type with key and pair value'
}

print("Integer: " + str(dictionary['integer']))

for word,meaning in dictionary.items():
	print(str(word) + ": " + str(meaning))
