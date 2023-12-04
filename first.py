import sqlite3
from datetime import date
from second import *

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
    options()
  else:
    print("-- Invalid Credentials!\tPlease try again. --")
    login()
    
# create a user
def create_user():
  print("Sign up!")
  print()
  print("Create a user name: ", end=" ")
  userName = input()
  joinedDate = date.today()
  noOfCreatures = 0
  rank = 1
  print("Create a password: ", end = " ")
  password = input()

  # Input into database
  create_user_sql(userName, joinedDate, noOfCreatures, rank, password)


def create_user_sql(uN, jD, nOC, r, p):
  cursor = connect.cursor()
  cursor.execute('INSERT INTO User (userName, joinedDate, noOfCreatures, userPassword, rank) VALUES (?,?,?,?,?)',
  (uN, jD, nOC, p, r))
  connect.commit()
  options()

def options():
  print()
  print("/")
  print("| Type an option...")
  print("|")
  print("| C - create creature")  # Create Creature
  print("| L - look at leaderboards")  # Battle
  print("| S - show settings")  # Settings
  print("\\")