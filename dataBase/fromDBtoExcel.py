import sqlite3
import csv
from pathlib import Path
from openpyxl import Workbook

# Connect to SQLite database
sqliteConnection = sqlite3.connect(Path.home() / Path("OneDrive", "Escritorio", "DataBase.db"))
crsr = sqliteConnection.cursor()
print('Connection established')

# Execute the SQL query
crsr.execute("SELECT name, salary, dateOfEmployment FROM employees;")
data = crsr.fetchall()

# Define the path for the CSV file
csv_file_path = Path.home() / Path("OneDrive", "Escritorio", "employee_data.csv")

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(['Name', 'Salary', 'Date of Employment'])
    # Write data
    csv_writer.writerows(data)

# Close the SQLite connection
crsr.close()

# Convert CSV to Excel using openpyxl
excel_file_path = Path.home() / Path("OneDrive", "Escritorio", "employee_data.xlsx")
workbook = Workbook()
sheet = workbook.active

# Read data from CSV and write to Excel
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        sheet.append(row)

# Save the Excel file
workbook.save(excel_file_path)

print(f'Excel file created and saved at: {excel_file_path}')
