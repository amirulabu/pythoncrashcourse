import json

filename = "favorite_number.json"

favorite_number = input("What is your favorite number? ")

with open(filename) as file_object:
	if str(json.load(file_object)) == str(favorite_number)
		print("Your number is already stored! Your favorite number is " + str(favorite_number))
	else:
		with open(filename, 'w') as file_object:
			json.dump(favorite_number, file_object)
			print("Your favorite number is saved")



# with open(filename, 'w') as file_object:
# 	json.dump(favorite_number, file_object)

# lyeana was here