# .table shows all tables created
# .schema shows all attributes and tables
import sqlite3
from datetime import date
from first import *

def main():

  print("Welcome to Iotta")
  greeting()  # gives a warning, still works perfectly fine

  connect = sqlite3.connect("Iotta.db")
  connect.commit()
  
if __name__ == "__main__":
  main()
