# create creature


import random
import sqlite3

connect = sqlite3.connect("Iotta.db")



def create_creature_prompt():
	print("-----------")
	print("Select a class!")
	print("/")
	print("| Type a number...")
	print("|")
	print("| 1: Archer")
	print("| 2: Warrior")
	print("| 3: Tank")
	print("| 4: Mage")
	print("| 5: Healer")
	print("| 6: Bard")
	print("\\")


def create_creature(username):
	from first import options
	print("Enter a name for your creature")
	name = input()
	health = random.randint(100, 250)
	while health % 5 != 0:
		health += 1
	damage = random.randint(25,100)
	while damage % 5 != 0:
		damage += 1
	classOptions = ['archer', 'warrior', 'tank', 'mage', 'healer', 'bard']
	create_creature_prompt()

	classNum = int(input())
	while classNum > 6 or classNum < 1:
		print("Input invalid. Please try again!")
		create_creature_prompt()
		classNum = int(input())

	classNum -= 1

	weight = random.randint(100,1000)
	height = random.randint(24, 120)

	print("If you would like to import photo from the web, enter the url, other wise, enter 'n'")
	urlInput = input()
	if urlInput != 'n':
		photo = urlInput
	else:
		photo = ''

	username = username
	cursor = connect.cursor()
	cursor.execute('''INSERT INTO Creature 
				(damage, name, health, photo, height, weight, class, user) 
				VALUES (?,?,?,?,?,?,?,?)''', (damage, name, health, photo, height, weight, classNum, username))
	connect.commit()
	print(f"Congratulations on finding {name}!")
	print(f"Statistics of {name}")
	print(f"Class: {classOptions[classNum]}")
	print(f"Damage: {damage}")
	print(f"Health: {health}")
	print(f"Height: {height} in")
	print(f"Weight: {weight} lbs")
	update_noOfCreatures(username)
	options(username)

# need to update number of creatures within User table

def update_noOfCreatures(username):
    cursor = connect.cursor()
    cursor.execute("SELECT noOfCreatures FROM User WHERE user = ?", (username, ))
    result = cursor.fetchall()

    if result:
        numCreatures = result[0][0]  # Extract the value from the tuple
        numCreatures += 1

        cursor.execute("UPDATE User SET noOfCreatures = ? WHERE user = ?", (numCreatures, username))
        connect.commit()
    else:
        print(f"User with username {username} not found.")
