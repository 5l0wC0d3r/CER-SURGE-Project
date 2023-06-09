import requests
import csv
from bs4 import BeautifulSoup

def scrape_derc_regulations():
    url = 'https://www.derc.gov.in/regulations/derc-Regulations'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the total number of pages
    last_page = int(soup.find('li', class_='pager-last').find('a').get('href').split('=')[-1])
    
    # Open the CSV file for writing
    with open('derc_regulations.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(['S. No.', 'Title', 'Date', 'Public Notices / Other Details', 'Amendments'])
        
        # Iterate over each page
        for page in range(0, last_page + 1):
            page_url = f'{url}?page={page}'
            response = requests.get(page_url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the regulation rows
            rows = soup.find_all('tr')
            
            # Iterate over each row and extract the required data
            for row in rows:
                columns = row.find_all('td')
                
                if len(columns) == 5:
                    s_no = columns[0].text.strip()
                    title = columns[1].text.strip()
                    date = columns[2].text.strip()
                    details = columns[3].text.strip()
                    amendments = columns[4].text.strip()
                    
                    # Write the data row to the CSV file
                    writer.writerow([s_no, title, date, details, amendments])
    
    print('Scraping completed. Data saved in derc_regulations.csv.')

# Run the scraping function
scrape_derc_regulations()
