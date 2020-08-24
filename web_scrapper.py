# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:36:07 2020

@author: surface
"""

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

def find_in_page(href) :
    page = urllib.request.urlopen("https://pastebin.com" + href)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # On cherche le tableau de résulats
    results = soup.find(string="push_back")
    if(results != None):
        print(href)

# URL, peut etre un tableau avec plusieurs pages et du multitaches
urlpage = 'https://pastebin.com/archive'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')


# On cherche le tableau de résulats
table = soup.find('table', attrs={'class': 'maintable'})
results = table.find_all('tr')
print('Number of results', len(results))


subjects = [];

# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    else : 
        hrefs = data[0].find_all('a')
        link = hrefs[0].get('href')
        find_in_page(link)
        
        

        