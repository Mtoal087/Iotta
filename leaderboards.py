# for options function
# allows the user to navigate through Iotta
# need a settings func to possibly rename, password, or delete account
# leaderboard
# etc...

import sqlite3

connect = sqlite3.connect("Iotta.db")


def leader_options(username):
	from first import options
	print("Type an option for Leaderboard!")
	print("/")
	print("| 1 - TOP 10 USERS")
	print("| 2 - SEARCH LEADERBOARD")
	print("| 3 - Back")
	print("\\")
	user = int(input())
	if user == 1:
		print()
		leaderboard(username)
	elif user == 2:
		print()
		search(username)
	elif user == 3:
		options(username)
	else:
		print("Invalid Option")
		print("Please try again")
		print()
		leader_options(username)




#puts users into leaderboard
#orders by rank (wins)
#shows user and rank

def leaderboard(username):
	cursor = connect.cursor()
	print("-- TOP 10 LEADERBOARD --")
	cursor.execute("SELECT * FROM Leaderboard ORDER BY rank DESC LIMIT 10")
	result = cursor.fetchall()
	print("RANK\tUSER")
	for i in result:
		print(f"{i[1]}|\t{i[2]}")
	print()
	leader_options(username)



# put searches in the search table
# output searches from leaderboard table
	# Search by rank - all players with a certain rank
	# Search by username - single player with extra info (# of creatures,)


def search(username):
	print("Search by:")
	print("/")
	print("| 1 - Rank")
	print("| 2 - Username")
	print("| 3 - Back")
	print("\\")
	user = input()
	if user == '1':
		print("Enter a rank to view all players with that rank:", end = " ")
		rank = input()
		search_by_rank(username, rank)

	elif user == '2':
		print("Enter a username to view that player's stats:", end = " ")
		uN = input()
		search_by_username(username, uN)

	elif user == '3':
		print()
		leader_options(username)

	else:
		print("Invalid Input")
		print("Please try again")
		print()
		search(username)


def search_by_rank(username, rank):
	cursor = connect.cursor()
	rank = int(rank)
	cursor.execute("SELECT rank, user FROM Leaderboard WHERE rank =?", (rank,))
	results = cursor.fetchall()
	print()
	if len(results) == 0:
		print("NO USERS WITHIN THIS RANK")
	else:
		print("RANK\tUSER")
		for result in results:
			print(f"{result[0]}|\t{result[1]}")
	print()
	search(username)

def search_by_username(username, uN):
	cursor = connect.cursor()
	cursor.execute("SELECT rank, user, noOfCreatures, joinedDate FROM User WHERE user = ?", (uN,))
	result = cursor.fetchone()
	if result is None:
		print("NO USER WITH THIS USERNAME")

	else:
		print(f"RANK\t\tUSER\t\tCREATURES CREATED\t\tJOINED DATE")
		print(f"{result[0]}\t\t{result[1]}\t\t{result[2]}\t\t\t\t{result[3]}")

	print()
	search(username)
