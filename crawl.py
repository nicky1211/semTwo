import requests
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
    hrefList = []
    for each in aTags[43:77]:
        each = "https://en.wikipedia.org"+each
        hrefList.append(each)
    return hrefList

aTags = getaTags(soup) 
links = getDiseaseCategoryLinks(aTags)
print links