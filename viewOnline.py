import sqlite3

connect = sqlite3.connect("Iotta.db")

def choice(username):
	from first import options
	print()
	print("Choose an option for ONLINE")
	print("/")
	print("| A - View All")
	print("|")
	print("| T - Show how many total people are online")
	print("|")
	print("| B - Back to homepage")
	print("\\")

	user = input()
	if user == 'a' or user == 'A':
		all_online(username)
	elif user == 'T' or user == 't':
		sum_online(username)
	elif user == 'B' or user == 'b':
		options(username)
	else:
		print("That input is invalid")
		print("Try again please")
		choice(username)

def sum_online(username):
	from first import options
	cursor = connect.cursor()
	cursor.execute("SELECT COUNT(*) FROM Login WHERE login = 1") # COUNT
	peopleOnline = cursor.fetchone()[0]
	print()
	print(f"Number of people online is: {peopleOnline}")
	print()
	choice(username)

def all_online(username):
	cursor = connect.cursor()
	print("-- Everyone online --")
	cursor.execute("SELECT * FROM Login WHERE login = 1")
	result = cursor.fetchall()
	for i in result:
		print(f"\t{i[2]}")
	print()
	choice(username)