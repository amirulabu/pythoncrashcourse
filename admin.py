usernames = ['Amirul','Iqram', 'admin', 'Khairul']
#usernames = ['']

for username in usernames:
	if username != '':
		if username == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + username + ", thank you for logging in again")
	else:
		print("We need to find some users!")

current_users = ['Amirul','Iqram', 'admin', 'Khairul', 'Mahfuz']
new_users = ['Ratan', 'Fahrin', 'iqram', 'Gerrit', 'Jules']

for new_user in new_users:
	if new_user in current_users \
	or new_user.title() in current_users \
	or new_user.upper() in current_users \
	or new_user.lower() in current_users:
		print("Username is not avaliable")

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")

		