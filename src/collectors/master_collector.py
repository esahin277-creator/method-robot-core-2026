import feedparser
import yfinance as yf
from GoogleNews import GoogleNews

class MasterCollector:
    def __init__(self):
        self.gn = GoogleNews(lang='tr')

    def collect_all(self, query):
        pool = {}
        # 1. Google News Taraması
        self.gn.search(query)
        pool['news'] = self.gn.result()
        
        # 2. Ekonomi Verileri
        pool['finance'] = yf.Ticker("USDTRY=X").history(period="1d")
        
        # 3. RSS Akışları (Örn: Reuters, BBC, Yerel)
        rss_urls = ["http://feeds.reuters.com/reuters/topNews"]
        pool['rss'] = [feedparser.parse(url).entries for url in rss_urls]
        
        return pool
