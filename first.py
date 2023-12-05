import sqlite3
from datetime import date
from creature import *

# Logging in or signing up page


connect = sqlite3.connect("Iotta.db")

def greeting():
  print("Welcome to Iotta")
  print("Are you an Iotta member?")
  print("Type \'y\' for yes or \'n\' for no")
  user = input()
  if user == 'y':
    print("Login")
    login()
  elif user == 'n':
    print()
    create_user()
  else:
    print("Sorry. Your input is not one of the options.")
    greeting()
    
# login to IOTTA
def login():
  print("Enter your username: ", end=" ")
  username = input()
  print("Enter your password: ", end=" ")
  password = input()
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM User WHERE userName = ? AND userPassword = ?', (username, password))
  result = cursor.fetchone()
  if result:
    print("-- Login Successful! --")
    options(username)
  else:
    print("-- Invalid Credentials!\tPlease try again. --")
    login()
    
# create a user
def create_user():
  print("Sign up!")
  print()
  print("Create a user name: ", end=" ")
  username = input()
  joinedDate = date.today()
  noOfCreatures = 0
  rank = 1
  print("Create a password: ", end = " ")
  password = input()

  # Input into database
  create_user_sql(username, joinedDate, noOfCreatures, password, rank)


def create_user_sql(username, joinedDate, noOfCreatures, password, rank):
  cursor = connect.cursor()
  cursor.execute('INSERT INTO User (userName, joinedDate, noOfCreatures, userPassword, rank) VALUES (?,?,?,?,?)',
  (username, joinedDate, noOfCreatures, password, rank))
  connect.commit()
  options(username)

def options(username):
  print()
  print("/")
  print("| Type an option...")
  print("|")
  print("| C - create creature")  # Create Creature
  print("| L - look at leaderboards")  # Battle
  print("| S - show settings")  # Settings
  print("\\")

  optionList = ['C', 'c']
  user = input()
  while user not in optionList:
    print("Invalid input")
    print("Please try again!")
    user = input()
  if user == 'C' or user == 'c':
    create_creature(username)