# Import the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
from csv import writer
from unidecode import unidecode
import threading


with open('test.csv', 'w', encoding='utf8', newline='') as f:   
            thewriter = writer(f)
            header = ['Data     ', 'Ora     ' , 'Echipa 1     ', 'Echipa 2     ', 'Cota 1     ', 'Cota X     ', 'Cota 2     ', 'Cota Peste 2.5     ', 'Cota Sub 2.5     ', 'GG/NG(DA)    ', 'GG/NG(NU)   ' ]
            thewriter.writerow(header)

def betano(root):
        # Use Selenium to make a request to the website
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.get(root)

        # Parse the HTML of the website
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        lists = soup.find_all('tr', 'events-list__grid__event')

        with open('test.csv', 'a', encoding='utf8', newline='') as f:
            thewriter = writer(f)
            

            for list in lists:
                info = []
                th = list.find('th', class_='events-list__grid__info')
                datadiv = th.find('div', class_='events-list__grid__info__datetime')
                listsData = datadiv.find_all('span')
                for listData in listsData:
                    info.append(listData.text.replace('\n', '').replace(' ', ''))
                
                listsTeam = th.find_all('span', class_='events-list__grid__info__main__participants__participant-name')
                for listTeam in listsTeam:
                    info.append(unidecode(listTeam.text.replace('\n', '').replace(' ', '')))
                    

                cote = list.find_all('span', class_='selections__selection__odd')
                for cota in cote:
                    info.append(cota.text.replace('\n', '').replace(' ', ''))
                    
                    
                thewriter.writerow(info)





        # Close the browser
        driver.quit()

if __name__ == "__main__":
    betano_tRO = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/romania/liga-1/17088/'))
    betano_tUK = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/anglia/premier-league/1/'))
    betano_tSP = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/spania/laliga/5/'))
    betano_tIT = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/italia/serie-a/1635/'))
    betano_tGE = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/germania/bundesliga/216/'))
    betano_tFR = threading.Thread(target=betano(root='https://ro.betano.com/sport/fotbal/franta/ligue-1/215/'))

    betano_tRO.start()
    betano_tUK.start()
    betano_tSP.start()
    betano_tIT.start()
    betano_tGE.start()
    betano_tFR.start()

    print("Done!")