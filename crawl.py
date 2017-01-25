import requests
import re
import os
import subprocess

from bs4 import BeautifulSoup
source_code = requests.get('https://en.wikipedia.org/wiki/Category:Diseases_and_disorders')
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")
linkList = []
docBasePath = '/home/manick/projectDocuments'

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

def deepCrawl(path,cat,url):

	path = path+"/"+cat
	fileName = path+"/"+cat+".html"
	if not os.path.exists(path):
		os.makedirs(path)
		subprocess.call(["curl", "-#" ,"-o", "%s"%fileName, "%s"%url])
aTags = getaTags(soup) 
links = getDiseaseCategoryLinks(aTags)

for key, value in links.iteritems():
	print key,value
	deepCrawl('/home/manick/proData',key,value)