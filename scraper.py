    
from selenium import webdriver
from bs4 import BeautifulSoup 
import time 
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/swatiahuja/Desktop/c127/venv/chromedriver')
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = []
    '''
    name = []
    distance = []
    mass = []
    radius = []
    luminosity = []
    '''
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for i in range(0,452):
        
        star_table = soup.find('table')
        temp_list = []
        #table_rows = []
        headers = soup.find_all('th')
        for tr in star_table: 
            td = soup.find_all('td') 
            row = [i.text.rstrip() 
            for i in td] 
            temp_list.append(row)
        print(temp_list)
    with open('webscrapeRESULT.csv','w') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerows(headers)
        csvWriter.writerow(temp_list)
      
scrape()

