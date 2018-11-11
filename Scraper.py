
"""File takes an inputted Amazon business account link, scrapes the website for the products
on the website, then returns a json file with the product names, the price, and the links"""

# library imports
import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests
from lxml import html
from time import sleep
import amazonparser
import json

def Scrape(url):
    print("check")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    # businessPage is the html from URL
    businessPage = requests.get(url, headers = headers)
    # soup is the parsed version of BusinessPage using BeautifulSoup
    soup = BeautifulSoup(businessPage.content, "lxml")
    title = soup.find('span', {'class':'a-color-state a-text-bold'}).get_text()
    i = 0
    # products is the data for the product
    products = []
    for links in soup.find_all('li'):
        try:
            print("check2")
            a = links.find('a')
            if (i <= 21):
                print("check3")
                urlLink = a.get('href')
                temp = amazonparser.AmzonParser(urlLink, title)
                products.append(temp)
                i = i + 1
        except:
            pass
    try:
        with open('data.json') as infile:
            data = json.load(infile)
        data.append(products)
        print("check4")
    except:
        data = products
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    try:
        nextPage = soup.find('a', {'title':'Next Page'})
        print("Passed")
        # products.append(Scrape('https://www.amazon.com' + nextPage.get('href')))
        Scrape('https://www.amazon.com' + nextPage.get('href'))
    except:
        pass
    # return products

# Using example URL for now, will have inputted URL functionality later
URL = 'https://www.amazon.com/s?marketplaceID=ATVPDKIKX0DER&me=A18SZPI9B4RMW5&merchant=A18SZPI9B4RMW5'
Scrape(URL)
