# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:11:07 2020

@author: surface
"""
import aiohttp
import asyncio
import urllib.request
from bs4 import BeautifulSoup

def first_magnet(page):
    soup = BeautifulSoup(page)    
    a_results = soup.find_all('a');
    return a_results

@asyncio.coroutine
def print_magnet(query):
    page = yield from urllib.request.urlopen("https://pastebin.com" + query)
    magnet = first_magnet(page)
    print(magnet)
    

loop = asyncio.get_event_loop()
f = asyncio.wait(print_magnet('/archive'))
loop.run_until_complete(f)