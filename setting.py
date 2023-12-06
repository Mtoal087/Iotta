import sqlite3

connect = sqlite3.connect("Iotta.db")

def settings(username):
	from first import options
	print()
	print("/")
	print("| Type an option...")
	print("| C - To edit/delete creatures")		######### working on
	print("| X - To delete your profile")		# done -
	print("| B - To go back to the main menu") # done -
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
		print("What creature would you like to edit/delete?")
		i = 1
		print("\tOption\tName of Creature")
		for creature in creatures:
			print(f'\t{i}\t{creature[2]}')
			i += 1
		option = int(input())
		print()
		editing_creature(username, option)



def editing_creature(username, option):
	cursor = connect.cursor()
	cursor.execute('''SELECT * FROM Creature WHERE user = ?''', (username,))
	creatures = cursor.fetchall()
	wantEdited = creatures[option -1]
	currentName = creatures[option -1][2]
	print("What would you like to edit?")
	print("/")
	print("| N - name")
	print("| P - photo")
	print("| C - cancel")
	print("| X - delete")
	print("\\")
	user = input()
	if user == 'N' or user == 'n':
		print("Enter character's new name: ", end=" ")
		name = input()
		cursor.execute('''UPDATE Creature SET name =? WHERE user =? AND name=?''', (name, username, currentName))
		connect.commit()
		settings(username)
	elif user == 'P' or user == 'p':
		print("Enter character's new photo url: ", end=" ")
		photo = input()
		cursor.execute('''UPDATE Creature SET photo =? WHERE user =? AND name=?''', (photo, username, currentName))
		connect.commit()
		settings(username)
	elif user == 'X' or user == 'x':
		print("Are you sure you want to delete this creature?")
		print("Type 'y' for yes or 'n' for no")
		confirm = input()
		if confirm == 'y':
			cursor.execute('''DELETE FROM Creature WHERE user =? AND name =?''', (username, wantEdited[2]))
			connect.commit()
			settings(username)
		else:
			settings(username)
	elif user == 'C' or user == 'c':
		settings(username)
	else:
		print("Invalid input")
		print()
		editing_creature(username, wantEdited)



def delete_profile(username):
    from first import greeting
    cursor = connect.cursor()
    print("Are you sure you want to delete your profile?")
    print("Type 'delete' for yes or 'n' for no")
    confirm = input()
    if confirm == 'delete':
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

