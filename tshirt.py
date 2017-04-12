def make_shirt(size,text):
	if size == 'large':
		text = 'I love Python'
	print("Your tshirt will be size " + str(size) + \
		" and have the text - " + str(text) + " - on it")

make_shirt('medium', 'go go power rangers')
make_shirt('large','test')
