import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self, site):
		self.site = site

	def scrape(self):
		r = urllib.request.urlopen(self.site)
		html = r.read()
		parser = "html.parser"
		sp = BeautifulSoup(html, parser)
		# lis=sp.select('div[class="cv-countdown__item-value _accent"]')
		# for p in lis:
		# 	print(p)
		for tag in sp.find_all("div",{"class":"cv-countdown__item-value _accent"}):
			url = tag
			if url is None:
				print("No")
				continue
			else:
				print("\n" + str(url.text))
				#f.write(url.text + "\n")
				

f = open("kek.txt","w")

news = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
now = Scraper(news)
now.scrape()


