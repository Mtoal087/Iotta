# for options function
# allows the user to navigate through Iotta
# need a settings func to possibly rename, password, or delete account
# create creature
# leaderboard
# etc...

import random
import sqlite3
from first import *

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
	creatureClass = classOptions[classNum]

	weight = random.randint(100,1000)
	height = random.randint(24, 120)

	markForDeletion = False

	print("If you would like to import photo from the web, enter the url, other wise, enter 'n'")
	urlInput = input()
	if urlInput != 'n':
		photo = urlInput
	else:
		photo = ''

	username = username

	cursor = connect.cursor()
	cursor.execute('''INSERT INTO Creature 
				(markForDeletion, damage, name, health, photo, height, weight, class, user) 
				VALUES (?,?,?,?,?,?,?,?,?)''', (markForDeletion, damage, name, health, photo, health, weight, classNum, username))
	connect.commit()
	print(f"Congratulations on finding {name}!")
	
	# need to update number of creatures within User table