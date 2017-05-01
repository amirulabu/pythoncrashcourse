import json

filename = "favorite_number.json"


with open(filename) as file_object:
	print("Your favorite number is: " + str(json.load(file_object)))