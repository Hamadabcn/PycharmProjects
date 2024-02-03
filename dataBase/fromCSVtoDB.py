import sqlite3
import csv
from pathlib import Path

# connect
sqliteConnection = sqlite3.connect(Path.home() / Path("OneDrive", "Escritorio", "DataBase.db"))
crsr = sqliteConnection.cursor()
print('Connection established')

# create table of employees
sql_command = """CREATE TABLE if not exists employees (
id INTEGER,
Name VARCHAR(20),
Salary INTEGER,
DateOfEmployment TEXT)"""

crsr.execute(sql_command)

# read file
file = open(Path.home() / Path("OneDrive", "Escritorio", "employees.csv"))
rows = csv.reader(file)

# add data to table
crsr.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", rows)

sqliteConnection.commit()
sqliteConnection.close()
