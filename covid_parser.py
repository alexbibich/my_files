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
        sick = sp.find_all("div",{"class":"cv-countdown__item-value _accent"})[1].text
        recovered = sp.find_all("div",{"class":"cv-countdown__item-value _accent-green"})[0].text
        print("Случаев за последние сутки: {}\nВыздоровело: {}".format(sick,recovered))

news = "https://xn--80aesfpebagmfblc0a.xn--p1ai/"
now = Scraper(news)
now.scrape()