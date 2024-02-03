import sqlite3
from pathlib import Path

# if the file DataBase.db exists it will connect to, if not it will create one on the desktop
sqliteConnection = sqlite3.connect(Path.home() / Path("OneDrive", "Escritorio", "DataBase.db"))
crsr = sqliteConnection.cursor()
print('Connection established')

# SQL command to create a table in the database
sql_command = """CREATE TABLE if not exists students(
firstName VARCHAR(20),
lastName VARCHAR(20),
age INTEGER)"""

crsr.execute(sql_command)

# insert data
crsr.execute('INSERT INTO students VALUES("Mohamed", "Farahat", 42);')
crsr.execute('INSERT INTO students VALUES("Amira", "Abdalla", 40);')
crsr.execute('INSERT INTO students VALUES("Yassin", "Mohamad", 13);')
crsr.execute('INSERT INTO students VALUES("Frida", "Mohamad", 12);')

# remember that you have to save
sqliteConnection.commit()

# close connection
sqliteConnection.close()
