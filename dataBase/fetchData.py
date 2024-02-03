import sqlite3
import csv
from pathlib import Path

# connect
sqliteConnection = sqlite3.connect(Path.home() / Path("OneDrive", "Escritorio", "DataBase.db"))
crsr = sqliteConnection.cursor()
print('Connection established')

crsr.execute("SELECT name, salary, dateOfEmployment FROM employees where salary > 850;")
# print(crsr.fetchall())  # this will fetch all the data in the database
# print(crsr.fetchone())  # this will fetch only the first line
# print(crsr.fetchmany(4))  # this will fetch the specific amount of lines indicated

answer = crsr.fetchall()
for i in answer:
    print(i)

crsr.close()
