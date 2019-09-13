import json

def register_acc(requested_user):
	filepath = './user_accounts/user_accounts.json'

	try:
		with open(filepath) as file_object:
			accs = json.load(file_object)
	except FileNotFoundError:
		print("Error searching for user: User accounts file not found.")
		sys.exit(0)

	usernames = []
	for user_id, password in accs.items():
		usernames.append(user_id)

	while True:
		if requested_user not in usernames:
			break
		else:
			requested_user = input("Username currently in use. Try another username: ")

	while True:
		new_password = input("Enter your password (at least 8 characters) in length: ")
		if len(new_password) >= 8:
			break

	accs[requested_user] = new_password

	try:
		with open(filepath, 'w') as file_object:
			json.dump(accs, file_object)
	except FileNotFoundError:
		print("Error adding user: User accounts file not found.")
		sys.exit(0)

	confirmation_msg = "Successfully created your account, " 
	confirmation_msg += requested_user
	print(confirmation_msg)

