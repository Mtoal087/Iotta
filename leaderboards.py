# for options function
# allows the user to navigate through Iotta
# need a settings func to possibly rename, password, or delete account
# leaderboard
# etc...

import sqlite3

connect = sqlite3.connect("Iotta.db")

#puts users into leaderboard
#orders by rank (wins)
#shows user and rank

def leaderboard(username):
	from first import options
	cursor = connect.cursor()
	print()
	print("-- TOP 10 LEADERBOARD --")
	cursor.execute("SELECT * FROM Leaderboard ORDER BY rank DESC LIMIT 10")
	result = cursor.fetchall()
	print("RANK\tUSER")
	for i in result:
		print(f"{i[1]}\t{i[2]}")
	options(username)
