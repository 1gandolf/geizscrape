from bs4 import BeautifulSoup
import time
import requests
import pandas as pd
import csv
import random


#some user agents for http requests

user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
] 

#use your header DevTools-->Network-->HTTP Request
header = {}

#Get all Product numbers from .csv
products = pd.read_csv(r'C:\*\products.csv', sep=';')
list = list(products["Material"])


#define Dataframe
#Searchterm - Geizhals ID - Name
df = pd.DataFrame(columns=["Ordercode", "GH_id", "Name"])
counter = 0



#Search for Ordercode in Geizhals and extract ID 
for i in list:
    ordercode = i.replace(":","%3A")
    url = 'https://geizhals.de/?fs='+i
    
    #switch between different user agents
    ua = random.choice(user_agents)
    req = requests.get(url, verify=False, headers=header)

    #get id from link to first searchresult
    soup = BeautifulSoup(req.content, 'html.parser')
    li = soup.find('h3', {'class': 'listview__name'})
    final = li.find('a').get('href')
    id = str(final)[-12:-5]

    # TODO: Catch non classified products with different link structure

    #also save the text
    name = li.find('a').text

    #add data to dataframe
    newRow = pd.DataFrame(
                {
                "Ordercode": [i], 
                "GH_id": [id],
                "Name": [name]
                })
    frame = [df, newRow]
    df = pd.concat(frame, ignore_index=True)

    #sleep to not get rate limited
    time.sleep(5)

#export to csv to work with id's
df.to_csv('ordercode2id.csv')
