import sqlite3

connect = sqlite3.connect("Iotta.db")


def login_bool(username):
	cursor = connect.cursor()
	boolean = True
	cursor.execute("UPDATE Login SET login = ? WHERE user = ?", (boolean, username))
	connect.commit()

def signIn_bool(username):
	cursor = connect.cursor()
	boolean = True
	cursor.execute("INSERT INTO Login (login, user) VALUES (?,?)", (boolean, username))
	connect.commit()

def logout(username):
	from first import greeting
	cursor = connect.cursor()
	boolean = False
	cursor.execute("UPDATE Login SET login = ? WHERE user = ?", (boolean, username))
	connect.commit()
	print("Return soon!")
	print("----------")
	greeting()