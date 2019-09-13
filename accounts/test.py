h = {}
h["cat"] = "dog"

try:
	print(h["cat"])
except KeyError:
	print("Username not found")
else:
	print("enter another user")
