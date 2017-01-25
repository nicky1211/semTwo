import requests
import re
from bs4 import BeautifulSoup
source_code = requests.get('https://en.wikipedia.org/wiki/Category:Diseases_and_disorders')
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")
linkList = []

def getaTags(soup):
    for link in soup.findAll('a'):
        l =  link.get('href')
        linkList.append(l)
    return linkList

def getDiseaseCategoryLinks(aTags):
    linkDict = {}
    for href in aTags[44:77]:
    	cateGory = re.findall(r'/(\w+)', href)[1]
        href = "https://en.wikipedia.org"+ href
        linkDict[cateGory] = href
    return linkDict

aTags = getaTags(soup) 
links = getDiseaseCategoryLinks(aTags)
