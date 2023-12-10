import sqlite3
from datetime import datetime
from creature import *
from leaderboards import *
from online import *
from viewOnline import *
from setting import *
from Iotta import *
from battlefield import *

# Logging in or signing up page


connect = sqlite3.connect("Iotta.db")

def greeting():
  print("----------------------------------------------------------------")
  print("Welcome to Iotta")
  print("Are you an Iotta member?")
  print("Type \'x\' to exit program.")
  print("Type \'y\' for yes or \'n\' for no")
  user = input()
  if user == 'y':
    print()
    print("Login")
    login()
  elif user == 'n':
    print()
    create_user()
  elif user == 'x':
    closeProgram()
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
  cursor.execute('SELECT * FROM User WHERE user = ? AND userPassword = ?', (username, password))
  result = cursor.fetchone()
  if result:
    cursor.execute('SELECT loss FROM User WHERE user =?', (username,))
    result = cursor.fetchone()
    print("-- Login Successful! --")
    if result[0] == 1:
      print()
      print()
      cursor.execute('UPDATE User SET loss = 0 WHERE user =?', (username,))
      connect.commit()
      cursor.execute("SELECT rank FROM User WHERE user =?", (username,))
      result = cursor.fetchone()
      print("You have been attacked!")
      print(f"Your rank is now {result[0]}")
      print()
    login_bool(username)
    options(username)
  else:
    print("-- Invalid Credentials!\tPlease try again. --")
    print()
    greeting()
    
# create a user
def create_user():
  print("Sign up!")
  print()
  print("Create a user name: ", end=" ")
  username = input()
  while len(username) > 16 or len(username) < 3:
    print("Username must be between 3 and 16 characters!")
    print("Please enter a valid username: ", end=" ")
    username = input()
  joinedDate = datetime.now()
  joinedDate = joinedDate.strftime("%m/%d/%Y")
  noOfCreatures = 0
  rank = 1
  print("Create a password: ", end = " ")
  password = input()

  # Input into database
  create_user_sql(username, joinedDate, noOfCreatures, password, rank)
  print("Thank you for making an account!")
  signIn_bool(username)
  add_to_leaderboard(username, rank)
  options(username)


def create_user_sql(username, joinedDate, noOfCreatures, password, rank):
  cursor = connect.cursor()
  cursor.execute('INSERT INTO User (user, joinedDate, noOfCreatures, userPassword, rank) VALUES (?,?,?,?,?)',
  (username, joinedDate, noOfCreatures, password, rank))
  connect.commit()

def options(username):
  print()
  print("/")
  print("| Type an option...")
  print("|")
  print("| B - Battle")
  print("| C - Creature")  # done -
  print("| L - Leaderboards")  # done - 
  print("| O - Online") # done -
  print("| S - Settings")  # done -
  print("| X - Logout") # done -
  print("\\")

  optionList = ['C', 'c', 'L', 'l', 'X', 'x', 'O', 'o', 'S', 's', 'B', 'b']
  user = input()
  while user not in optionList:
    print("Invalid input")
    print("Please try again!")
    print()
    user = input()
  if user == 'C' or user == 'c':
    create_creature(username)
  if user == 'L' or user == 'l':
    leader_options(username)
  if user == 'X' or user == 'x':
    logout(username)
  if user == 'O' or user == 'o':
    choice(username)
  if user == 'S' or user =='s':
    settings(username)
  if user == 'B' or user == 'b':
    battle(username)

def add_to_leaderboard(username, rank):
  cursor = connect.cursor()
  cursor.execute('''INSERT INTO Leaderboard (rank, user) VALUES (?,?)''', (rank, username))
  connect.commit()

