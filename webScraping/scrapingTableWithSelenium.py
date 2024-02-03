import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os


def initialize_driver():
    # Function to initialize and return a Chrome WebDriver instance
    return webdriver.Chrome()


def find_required_table(driver, caption_text):
    # Function to find the required table based on its caption text
    for table in driver.find_elements(By.TAG_NAME, 'table'):
        if caption_text in table.find_element(By.TAG_NAME, 'caption').text:
            return table
    return None


def extract_data_from_table(table):
    # Function to extract headers and data from a table
    headers = [head.text.replace('\n', '') for head in table.find_elements(By.TAG_NAME, 'th')]  # 'th' table header
    data = []

    for row_data in table.find_elements(By.TAG_NAME, 'tr'):
        value_text = [db.text.strip() for db in row_data.find_elements(By.TAG_NAME, 'td')]  # 'td' table data

        if len(value_text) > 0:
            data.append(value_text)

    return headers, data


def main():
    # Main function to initialize the web scraping process
    browser = initialize_driver()

    try:
        # Navigate to the Wikipedia page
        browser.get('https://es.wikipedia.org/wiki/Anexo:Idiomas_por_n%C3%BAmero_de_hablantes_nativos')

        # Find the required table
        required_table = find_required_table(browser, 'Idiomas con al menos 10 millones de hablantes como idioma nativo')

        if required_table:
            # Extract data from the table
            headers, data = extract_data_from_table(required_table)

            # Construct the path dynamically using os library
            current_script_directory = Path(os.path.dirname(os.path.abspath(__file__)))
            csv_path = current_script_directory / "wikiPedia.csv"

            # Writing data to a CSV file
            with open(csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(data)
            print("Data written to CSV successfully at:", csv_path)

        else:
            print("Required table not found.")

    finally:
        # Close the browser window
        browser.quit()


if __name__ == "__main__":
    main()
