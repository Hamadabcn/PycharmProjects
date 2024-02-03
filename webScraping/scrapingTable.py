import csv
import bs4
import requests
from pathlib import Path
import sys

# Making a GET request to the Wikipedia page
try:
    res = requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
    res.raise_for_status()  # Raises an HTTPError for bad responses
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
    sys.exit(1)
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
    sys.exit(1)
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
    sys.exit(1)
except requests.exceptions.RequestException as err:
    print(f"An unexpected error occurred: {err}")
    sys.exit(1)

# Parsing the HTML content of the page using BeautifulSoup
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Selecting all tables on the page
table_soup = soup.find_all('table')

# Filtering tables with non-empty captions
filtered_table = [table for table in table_soup if table.caption is not None]
print("Tables with non-empty captions:", filtered_table)

# Finding the required table based on its caption
required_table = None

for table in filtered_table:
    if 'Languages with at least 50 million first-language speakers' in str(table.caption.text).strip():
        required_table = table
        break

# Checking if the required table is found
if required_table is not None:
    # Extracting headers from the table
    rows = required_table.find_all('tr')  # 'tr' means table row
    headers = [head.text.replace('\n', '') for head in rows[0].find_all('th')]  # 'th' table header
    print("Headers:", headers)

    # Extracting data from the table rows
    data = []

    for row_data in rows:
        value = row_data.find_all('td')  # 'td' table data
        value_text = [db.text.strip() for db in value]

        if len(value_text) == 0:
            continue
        data.append(value_text)

    # Writing data to a CSV file
    with open(Path.home() / Path("OneDrive", "Escritorio", "wikiPedia.csv"), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
    print("Data written to CSV successfully.")

else:
    print("Required table not found.")
