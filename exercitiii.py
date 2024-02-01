from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
from unidecode import unidecode
import threading
import time

start_time = time.time()

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get('https://ro.betano.com/')
root = 'https://ro.betano.com'


#functie pentru sport specific facem query pe ligi
def getLigi(sport):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get(root + sport)
    
    
        
    driver.close()



# Parse the HTML of the website
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

listaSporturi = soup.find_all('li', class_= 'sport-picker__main__item')
listaLinkSporturi = []
for sport in listaSporturi[:4]:
    a = sport.find('a')
    listaLinkSporturi.append(a['href'])

for link in listaLinkSporturi:
    getLigi(link)    
     
    
driver.quit()

print("--- %s seconds ---" % (time.time() - start_time))




