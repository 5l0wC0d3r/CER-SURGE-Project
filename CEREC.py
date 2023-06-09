import csv
from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium webdriver with Chrome
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Navigate to the website
driver.get('https://cercind.gov.in/recent_orders.html')

# Wait for the page to load (adjust the sleep duration if needed)
driver.implicitly_wait(5)

# Get the page source after waiting for JavaScript rendering
html = driver.page_source

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the table containing the orders
table = soup.find('table', class_='display')

# Create a CSV file to store the data
with open('orders.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Order Number', 'Order Date', 'Description'])

    # Iterate over the rows in the table (excluding the header row)
    rows = table.find_all('tr')[1:]
    for row in rows:
        # Extract the data from each column
        columns = row.find_all('td')
        order_number = columns[0].text.strip()
        order_date = columns[1].text.strip()
        description = columns[2].text.strip()

        # Write the data to the CSV file
        writer.writerow([order_number, order_date, description])

# Close the Selenium webdriver
driver.quit()
