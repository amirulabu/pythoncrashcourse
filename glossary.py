from collections import OrderedDict

dictionary = OrderedDict()
# ordered dictionary ensure the order of the key pair when created

# dictionary = {
# 	'if': 'A type of statement that will pass when true',
# 	'loop': 'To repeat an action',
# 	'string': 'text',
# 	'integer': 'round number including negative numbers',
# 	'dictionary': 'A type of data type with key and pair value'
# }

dictionary['if'] = 'A type of statement that will pass when true'
dictionary['loop'] = 'To repeat an action'
dictionary['string'] = 'text'
dictionary['integer'] = 'round number including negative numbers'
dictionary['dictionary'] = 'A data type with key and pair value'

print("Integer: " + str(dictionary['integer']))

for word,meaning in dictionary.items():
	print(str(word) + ": " + str(meaning))
