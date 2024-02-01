# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from csv import writer
from unidecode import unidecode

import threading
import time

start_time = time.time()


def superbet(root):


        # Use Selenium to make a request to the website
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.get(root)

        #asteapta sa fie incarcate toate meciurile 
        time.sleep(3)

        # Parse the HTML of the website
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        #Selecteaza tabelul cu meciuri viitoare si exclude meciurile live(wrapperul are o clasa diferita ceva cu prematch)
        tabelSoup = soup.find('div', class_='group-header__wrapper e2e-event-group-header is-grid-view-active section--prematch markets-optimized--3')
        meciuri = tabelSoup.find_all('div', class_='event-row-container')
         

        # Accepta cookie
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        butonAccepta = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        butonAccepta.click()

        #id pentru tip de cota(din lista de tip de pariu)
        idlista = ['547', '200734', '539']

        
        time.sleep(1)
        #butonul pentru schimbarea tipul de pariu
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'market-filters')))
        #Verificam ca e butonul bun(poate aparea un meci livea deasupra listei de meciuri cu butonul propriu )
    
        butonCote = driver.find_element(By.XPATH, '//div[@class="group-header__wrapper e2e-event-group-header is-grid-view-active section--prematch markets-optimized--3"]/div/div[@class="market-filters"]')
        """"
        for buton in butoaneCote:
            
            gasit = 0

            for id in idlista:
                
                buton.click()

                butonSelectie = driver.find_element(By.XPATH, "//div[@data-market-id='{}']".format(id))
                if(butonSelectie != None):
                    butonSelectie.click()
                    gasit += 1

            if(gasit == 3):
                butonCote = buton
                break        
                
        """    

        tabel = []

        #Cotele 1X2
        butonCote.click()
                
        time.sleep(1)
        butonFinal = driver.find_element(By.XPATH, "//div[@data-market-id='547']")
        butonFinal.click()

        #Loop pentru informatiile din fiecare meci
        for meci in meciuri:
                info = []
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class='event-summary__competitors-team1 e2e-event-team1-name']")))
                
                data = meci.find('span', class_='event-summary__match-indicator-day')
                ora = meci.find('span', class_='event-summary__match-indicator-time')
                echipa1 = meci.find('span', class_='event-summary__competitors-team1 e2e-event-team1-name')
                echipa2 = meci.find('span', class_='event-summary__competitors-team2 e2e-event-team2-name')
                
                
                #Bagam in row data, ora, echipa1 si echipa2
                try:
                    info.append(unidecode(data.text.replace('\n', '').replace(' ', '')))
                    info.append(ora.text.replace('\n', '').replace(' ', ''))
                except:
                    info.append(' ')
                    info.append(' ')
                info.append(unidecode(echipa1.text.replace('\n', '').replace(' ', '')))
                info.append(unidecode(echipa2.text.replace('\n', '').replace(' ', '')))


                for i in idlista:
                    butonCote.click()
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-market-id='{}']".format(i))))
                    butonFinal = driver.find_element(By.XPATH, "//div[@data-market-id='{}']".format(i))
                    butonFinal.click()
                    
                    soupmeciuri = BeautifulSoup(driver.page_source, 'html.parser')

                    cotemeci = soupmeciuri.find('div', { 'id' :  '{}'.format(meci['id'])})
                    time.sleep(1)

                    if(i == '200734'):

                        listacota = cotemeci.find_all('div', class_="pick__click-buffer e2e-odd-pick")
                        
                        if(len(listacota) > 2):
                            try:
                                cotesub = listacota[4].find('span', class_='value new actionable e2e-odd-current-value')
                                cotepeste = listacota[5].find('span', class_='value new actionable e2e-odd-current-value')
                            except:
                                cotesub = '0'
                                cotepeste = '0'
                        else:
                            try:
                                cotesub = listacota[0].find('span', class_='value new actionable e2e-odd-current-value')
                                cotepeste = listacota[1].find('span', class_='value new actionable e2e-odd-current-value')
                            except:
                                cotesub = '0'
                                cotepeste = '0'
                        
                        if(cotesub != None and cotepeste != None):
                            info.append(cotepeste.text.replace('\n', '').replace(' ', ''))
                            info.append(cotesub.text.replace('\n', '').replace(' ', ''))
                        continue

                    else:
                        try:
                            cote = cotemeci.find_all('span', class_='value new actionable e2e-odd-current-value') 
                        except:
                            cote = ['0', '0']
                        for cota in cote:
                            
                            info.append(cota.text.replace('\n', '').replace(' ', ''))    
                tabel.append(info)
            

        # Close the browser
        driver.quit()
        print("--- %s seconds ---" % (time.time() - start_time))
        
        
        return tabel
        
        

if __name__ == "__main__":

    
    

    betanotabel = superbet(root='https://superbet.ro/pariuri-sportive/fotbal/argentina')
    
    
    

    


