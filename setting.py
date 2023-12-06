import sqlite3

connect = sqlite3.connect("Iotta.db")

def settings(username):
	from first import options
	print()
	print("/")
	print("| Type an option...")
	print("| C - To edit/delete creatures")
	print("| X - To delete your profile")
	print("| B - To go back to the main menu")
	print("\\")
	optionList = ['c', 'C', 'x', 'X', 'b', 'B']
	user = input()
	while user not in optionList:
		print("Invalid input")
		print("Please try again!")
		print()
		user = input()
	if user == 'c' or user == 'C':
		edit_creature(username)
	if user == 'x' or user == 'X':
		delete_profile(username)
	if user == 'b' or user == 'B':
		options(username)



def edit_creature(username):
	from creature import create_creature
	cursor = connect.cursor()
	cursor.execute('''SELECT * FROM Creature WHERE user = ?''', (username,))
	creatures = cursor.fetchall()

	if not creatures:
		print()
		print("You have not created any creatures!")
		print("Would you like to create a new one?")
		print("Type 'y' for yes or 'n' for no")
		confirm = input()
		if confirm == 'y':
			create_creature(username)
		else:
			settings(username)
	
	else:
		print("What creature would you like to edit?")
		i = 1
		for creature in creatures:
			print(f'{i}\t{creature[2]}')
			i += 1
		settings(username)


def delete_profile(username):
    from first import greeting
    cursor = connect.cursor()
    print("Are you sure you want to delete your profile?")
    print("Type 'y' for yes or 'n' for no")
    confirm = input()
    if confirm == 'y':
        from online import logout

        # Delete from related tables with CASCADE
        cursor.execute('''DELETE FROM Creature WHERE user = ?''', (username,))
        cursor.execute('''DELETE FROM Leaderboard WHERE user = ?''', (username,))
        cursor.execute('''DELETE FROM Login WHERE user = ?''', (username,))

        # Delete from the User table
        cursor.execute('''DELETE FROM User WHERE user = ?''', (username,))

        connect.commit()
        print("Your profile and related data have been deleted!")
        print("----------")
        logout(username)
    else:
        settings(username)
