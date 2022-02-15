from bs4 import BeautifulSoup
import time
from pip import main
import requests
import pandas as pd
import urllib3
from datetime import datetime
from random import randrange

#https security warning with every request --> disable
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#use your header DevTools-->Network-->HTTP Request
header = {}

# Scrape TOP 10 cheapest offers for url 
products = pd.read_csv(r'C:\*\ordercode2id_clean.csv', sep=';')
list = list(products["GH_id"])

#define Dataframe
df = pd.DataFrame(columns=["GH_id", "Platz", "Anbieter", "Preis", "URL","Datetime"])

counter = 0
for i in list:
    counter+=1
    url = 'https://geizhals.de/'+str(i)
    req = requests.get(url, verify=False, headers=header)
    soup = BeautifulSoup(req.content, 'html.parser')

    #catch den Banhammer

    #Searching TOP 10 Offers
    ranger = range(0,10)
    for l in ranger:
        #Get Offer
        offer_id = "offer__" + str(l)
        li = soup.find('div', {'id': offer_id})

        #if number of search results <10 break loop
        if li is None: 
            break

        #TODO: add error handling (Timeout->Stop)

        #Get Name
        merch = li.find('span',{'class': 'merchant__logo-caption'})
        name = merch.find('span',{'class': 'notrans'}).string.strip()

        #Get Price
        price = li.find('div',{'class': 'offer__price'})
        pricer = price.find('span',{'class': 'gh_price'}).string.replace('€ ', '')

        #Get Link
        liver = li.find('div', {'class': 'cell offer__merchant'})
        redirectURL = liver.find('a').get('href')
        finalURL = "https://www.geizhals.de"+redirectURL

        #Get Time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        #fill data into df
        newRow = pd.DataFrame(
                {
                  "GH_id": [i],
                  "Platz": [l+1],
                  "Anbieter": [name],
                  "Preis": [pricer],
                  "URL": [finalURL],
                  "Datetime": [dt_string]
                })

        frame = [df, newRow]
        df = pd.concat(frame, ignore_index=True)

    random = randrange(3)       
    time.sleep(random)

#define name by current daytime and save to .csv
now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H%M")
df_name = 'online_prices' + dt_string + '.csv'
df.to_csv(df_name)