# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from csv import writer
from unidecode import unidecode
import threading
import time

start_time = time.time()




# Use Selenium to make a request to the website
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get("https://superbet.ro/pariuri-sportive/fotbal/spania/spania-laliga/toate")

driver.implicitly_wait(10)


# Parse the HTML of the website
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
tabelSoup = soup.find('div', class_='group-header__wrapper e2e-event-group-header is-grid-view-active section--prematch markets-optimized--3')
meciuri = soup.find_all('div', class_='event-row-container')
        
# Accepta cookie
driver.implicitly_wait(10)
butonAccepta = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
butonAccepta.click()

for meci in meciuri:
    print(meci.text.replace('\n', ' '))
    butonCote = driver.find_element(By.XPATH, '//div[@class="group-header__wrapper e2e-event-group-header is-grid-view-active section--prematch markets-optimized--3"]/div/div[@class="market-filters"]')
    butonCote.click()





# Close the browser
driver.quit()
print("--- %s seconds ---" % (time.time() - start_time))

