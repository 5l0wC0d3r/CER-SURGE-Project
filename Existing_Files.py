from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

def CER_FETCH(username, password):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("https://cer.iitk.ac.in/login")
    # finish the code to login into cer and navigate to regulatory tracker using selenium and beautiful soup 
    driver.find_element("name","username").send_keys(username)
    driver.find_element("name","password").send_keys(password)
    driver.find_element("type", "submit").click()
    driver.get("https://cer.iitk.ac.in/regulatory-tracker")
    orders = []
    tag1s = []
    tag2s = []
    tag3s = []
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for a in soup.findAll('a', href=True, attrs={'class': 'card-action action1'}):
        order = a.find('span', attrs={'class': 'card-title'})
        tag1 = a.find('span', attrs={'class': 'init c-pill c-pill--success'})
        tag2 = a.find('span', attrs={'class': 'init c-pill c-pill--warning'})
        tag3 = a.find('span', attrs={'class': 'init c-pill c-pill--danger'})
        orders.append(a.text)
        tag1s.append(tag1.text)
        tag2s.append(tag2.text)
        tag3s.append(tag3.text)
    print(orders)
    df = pd.DataFrame({'Orders': orders, 'tag1': tag1s, 'tag2': tag2s, 'tag3': tag3s})
    df.to_csv('CER DATASET.csv', index=False, encoding='utf-8')


CER_FETCH("chetanya21@iitk.ac.in","Saibaba123")
