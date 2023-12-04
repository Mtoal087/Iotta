# .table shows all tables created
# .schema shows all attributes and tables
import sqlite3
from first import *

def main():
  connect = sqlite3.connect("Iotta.db")

  greeting()  # gives a warning, still works perfectly fine
  connect.commit()
  
if __name__ == "__main__":
  main()
