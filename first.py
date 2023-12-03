import sqlite3
from datetime import date

def greeting():
  print("Welcome to Iotta")
  print("Are you an Iotta member?")
  print("Type \'y\' for yes or \'n\' for no")
  user = input()
  if user == 'y':
    login()
  elif user == 'n':
    create_user()
  else:
    print("Sorry. Your input is not one of the options.")
    greeting()
    
# login to IOTTA
def login():
  print("Login")
  print("Enter your username: ", end=" ")
  username = input()
  print("Enter your password: ", end=" ")
  password = input()
  cursor = connect.cursor()
  cursor.execute('SELECT * FROM User WHERE userName = ? AND userPassword = ?', (username,password))
  loggedOn = cursor.fetchone()
  if loggedOn:
    options()
  else:
    print("Invalid Credintials\nPlease try again.")
    login()
    
# create a user
def create_user():
  print("Sign up!")
  print()
  print("Create a user name!")
  userName = input()
  joinedDate = date.today()
  lastActive = joinedDate
  noOfCreatures = 0
  rank = 1
  print("Enter a valid email: ", end=" ")
  email = input()
  print("Enter a password: ", end = " ")
  password = input()

  # Input into database
  create_user_sql(userName, joinedDate, lastActive,
    noOfCreatures, rank, email, password)

connect = sqlite3.connect("Iotta.db")
cursor = connect.cursor()


def create_user_sql(uN, jD, lA, nOC, r, e, p):
  cursor = connect.cursor()
  cursor.execute('INSERT INTO User (userName, joinedDate, lastActive, noOfCreatures, userEmail, userPassword, rank) VALUES (?,?,?,?,?,?,?)',
  (uN, jD, lA, nOC, r, e, p))

def options():
  print()
  print("Login Successful!")
  print("Choose an option...")
  print("C")  # Create Creature
  print("B")  # Battle
  print("S")  # Settings