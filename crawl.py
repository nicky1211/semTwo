import requests
import re
import os
import subprocess
import configfile
from bs4 import BeautifulSoup


source_code = requests.get(configfile.basecrawlurl)
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
        href = configfile.website+href
        linkDict[cateGory] = href
    return linkDict

def deepCrawl(path,cat,url):

	path = path+"/"+cat
	fileName = path+"/"+cat+".html"
	if not os.path.exists(path):
		os.makedirs(path)
		subprocess.call(["curl", "-s" ,"-o", "%s"%fileName, "%s"%url])


aTags = getaTags(soup) 
links = getDiseaseCategoryLinks(aTags)

for key, value in links.iteritems():
	# print key,value
	deepCrawl(configfile.docBasePath,key,value)