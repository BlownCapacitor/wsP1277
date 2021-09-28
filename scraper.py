from selenium import webdriver
from bs4 import BeautifulSoup 
import time 
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/swatiahuja/Desktop/c127/venv/chromedriver')
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ['Name','Distance', 'Mass','Radius']
    star_factors  = []
    for i in range(0,452):
        soupbrowser = BeautifulSoup(browser.page_source, 'html.parser')
        for th_tags in soupbrowser.find_all('th',attrs={'class', 'headerSort'}):
            td_tag = th_tags.find_all('td')
            temp_list = []
            for tr in star_factors: 
                td = tr.find_all('td') 
                row = [i.text.rstrip() 
                for i in td] 
                temp_list.append(row)
            for index,td_tags in enumerate(td_tag):
                if index == 0:
                    temp_list.append(td_tags.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tags.contents[0])
                    except:
                        temp_list.append('')
            star_factors.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table').click()
    with open('scraper3.csv','w') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(star_factors)
            
scrape()
