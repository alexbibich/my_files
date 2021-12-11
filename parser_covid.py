import urllib.request
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self, site):
		self.site = site

	def scrape(self):
		stat = list()
		r = urllib.request.urlopen(self.site)
		html = r.read()
		parser = "html.parser"
		sp = BeautifulSoup(html, parser)
		for tag in sp.find_all("div",{"class":"cv-countdown__item-value _accent"}):
			url = tag
			if url is None:
				print("No")
				continue
			else:
				stat.append(str(url.text))
		print("Случаев за последние сутки: {}\nВыявлено случаев: {}".format(stat[1],stat[0]))

news = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
now = Scraper(news)
now.scrape()