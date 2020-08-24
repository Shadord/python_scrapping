# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:07:21 2020

@author: surface
"""

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import asyncio

url_visited = []
gifi_words = ["vector"]
sema = asyncio.BoundedSemaphore(3)

def find_gifi_words(soup) :
    counter = 0
    # On cherche le tableau de résulats
    for word in gifi_words:
        results = soup.find(string=word)
        if(results != None):
            counter += 1
    return counter



async def open_page(url):
    with (await sema):
        try:
            resp = await urllib.request.urlopen("https://pastebin.com" + url)
        except:
            raise ValueError
        finally:
            await resp.release()
    print(resp)
    return resp



async def recursive_fcn(urlpage):
    global url_visited
    global sem
    # Ouverture de la page
    page = open_page(urlpage)

    # parsing de la page
    soup = BeautifulSoup(page, 'html.parser')
    # Trouve tous les a
    counter = find_gifi_words(soup)
    if(counter > 0):
        print('Number of results in', urlpage, " is ", counter)
    else:
        print("No results found for ", urlpage)
    url_visited.append(urlpage)
    print("Progress : ", len(url_visited))
    a_results = soup.find_all('a');
    for result in a_results:
        href = result.get('href')
        if(url_visited.count(href) == 0):
            recursive_fcn(href)

first_page = '/archive'
#recursive_fcn(first_page)

loop = asyncio.get_event_loop()
loop.run_until_complete(recursive_fcn(first_page))
print("All Workers Completed")
loop.close()
        