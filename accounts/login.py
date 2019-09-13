import json, sys

#locates and stores the current user accounts as a hash to be sent
#to the login_user function. 
def get_accounts():
	#gives the path of the json file that holds the usernames and passwords
	filepath = './user_accounts/user_accounts.json'

	#try to locate the file. catch an the error if file isn't found. 
	try:
		with open(filepath) as file_object:
			accs = json.load(file_object)
	except FileNotFoundError:
		print("User accounts file not found.")
		sys.exit(0)

	return accs

#This function calls the function get_accounts() to 
#obtain a hash of account users and passwords. 
#
#Using the parameter request_id, we match 
def login_user(request_id):
	all_accounts = get_accounts()
	attempts = 0

	#Find the correct password and validate the request_id
	while attempts < 3:
		try:
			valid_pass = all_accounts[request_id]		
		except KeyError:
			attempts += 1
			print("Username <" + request_id + "> not found.")
			request_id = input("Try another username: ")
		else:
			attempts = 0
			break

	#Request the user to enter the corresponding password
	#for request_id.
	while attempts < 3: 
		input_pass = input("Enter your password: ")

		if input_pass == valid_pass:
			attempts = 0
			break

	#If you failed either the 3-attempt limit (for pass or user id)
	#your session terminates. 
	if attempts:
		print("Too many failed password attempts.")
		sys.exit(0)
	else: 
		welcome_msg = "You have successfully gained access to your account, "
		welcome_msg += request_id + "."
		print(welcome_msg)

	#Successfully gained access to the account.

# login_user("1")
	









