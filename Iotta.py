# .table shows all tables created
# .schema shows all attributes and tables
import sqlite3
connect = sqlite3.connect("Iotta.db")

def startProgram():
  from first import greeting
  greeting()

def closeProgram():
  connect.close()
  return

def main():
  startProgram()  
  
if __name__ == "__main__":
  main()
