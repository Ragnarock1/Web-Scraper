# Import the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer
import threading
import time

start_time = time.time()

def betano(root):
        # Use Selenium to make a request to the website
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.get(root)

        # Parse the HTML of the website
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', 'events-list__grid')
        lists = soup.find_all('tr', 'events-list__grid__event')
        tabelfinal = []

        for list in lists:
                info = []
                th = list.find('th', class_='events-list__grid__info')
                datadiv = th.find('div', class_='events-list__grid__info__datetime')
                listsData = datadiv.find_all('span')
                for listData in listsData:
                    info.append(listData.text.replace('\n', '').replace(' ', ''))
                
                listsTeam = th.find_all('span', class_='events-list__grid__info__main__participants__participant-name')
                listaechipe = []
                for listTeam in listsTeam:
                    info.append(listTeam.text.replace('\n', '').replace(' ', ''))
                    

                cote = list.find_all('span', class_='selections__selection__odd')
                for cota in cote:
                    info.append(cota.text.replace('\n', '').replace(' ', ''))
                tabelfinal.append(info)

            
        
        # Close the browser
        driver.quit()
        print("--- %s seconds ---" % (time.time() - start_time))
        return tabelfinal

if __name__ == "__main__":
    

    print("Done!")
    

