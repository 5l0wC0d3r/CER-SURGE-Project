from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

def CERC_FETCH():
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("https://cercind.gov.in/recent_orders.html")
    