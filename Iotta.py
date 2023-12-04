# .table shows all tables created
# .schema shows all attributes and tables
import sqlite3
from first import greeting

def main():
  connect = sqlite3.connect("Iotta.db")

  greeting()  
  connect.commit()
  
if __name__ == "__main__":
  main()
