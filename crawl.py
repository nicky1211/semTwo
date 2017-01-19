import requests
from bs4 import BeautifulSoup

class Spider:

	def __init__(self,url):
		self.source_code = requests.get(url)
		self.plain_text = self.source_code.text

	def subcategory_spider(self):
		self.subcategory_crawl_list = []
		soup = BeautifulSoup(self.plain_text,"lxml")
		for link in soup.findAll('a',{'class':'CategoryTreeLabel'}):
			href = link.get('href')
			href = "https://en.wikipedia.org"+href
			self.subcategory_crawl_list.append(href)
		assert(len(self.subcategory_crawl_list) == 32)
		return self.subcategory_crawl_list

	def category_spider(self):
		self.category_crawl_list = []
		soup = BeautifulSoup(self.plain_text,"lxml")
		cat_class = soup.findAll('div', attrs={'class' : 'mw-category-group'})
		for each in cat_class:
			href = each.find('a')['href']
			href = "https://en.wikipedia.org"+href
			self.category_crawl_list.append(href)
		assert(len(self.category_crawl_list) == 33)
		return self.category_crawl_list

class CrawlL1:

	def maincrawler(self,url):
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"lxml")
		for link in soup.findAll('a',{'class':'CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory'}):
			href = link.get('href')
			href = "https://en.wikipedia.org"+href
			print href




if __name__ == '__main__':

	url = 'https://en.wikipedia.org/wiki/Category:Diseases_and_disorders'
	spider = Spider(url)
	list1 = spider.subcategory_spider()
	list2 = spider.category_spider()
	crawl = CrawlL1()
	for each in list1:
		crawl.maincrawler(each)