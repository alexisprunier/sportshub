# -*- coding: utf-8 -*-
from SportsHubApp.models import Article
from bs4 import BeautifulSoup
import urllib

class ArticleGetter:

    @staticmethod
    def get_infos(source, nb_infos, sport, url):
        
        print source + ": " + sport
        
        try:
            xml = urllib.urlopen(url).read()
            parser = BeautifulSoup(xml)
            list_art = parser.find_all("item", limit=nb_infos)
    
            for article in list_art :
                title = article.find("title").text
                link = article.find("link").text
                image = ""
                if article.find("enclosure"):
                    image = article.find("enclosure").get("url")
                article = Article(titre=title, 
                                  origine=source,
                                  type="Articles",
                                  lien=link,
                                  image=image,
                                  sport=sport)
                article.save()
        except Exception as e: 
            print "ERROR:" + str(e)
            
class Eurosport():
    
    def __init__(self, nb_infos):
        self.source = "Eurosport"
        self.urls = {'Football': 'http://www.eurosport.fr/football/rss-flash.xml',
                     "Ski": 'http://www.eurosport.fr/hiver/rss.xml',
                     'Golf': 'http://www.eurosport.fr/golf/rss.xml',
                     'Basketball': 'http://www.eurosport.fr/basketball/rss.xml',
                     'Tennis': 'http://www.eurosport.fr/tennis/rss.xml',
                     'Cyclisme': 'http://www.eurosport.fr/cyclisme/rss.xml',
                     'Auto-Moto': 'http://www.eurosport.fr/auto-moto/rss.xml',
                     'Athlétisme': 'http://www.eurosport.fr/athletisme/rss.xml',
                     'Boxe': 'http://www.eurosport.fr/boxe/rss.xml',
                     'Handball': 'http://www.eurosport.fr/handball/rss.xml',
                     'Natation': 'http://www.eurosport.fr/natation/rss.xml',
                     'Volley-ball': 'http://www.eurosport.fr/volleyball/rss.xml',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class Lequipe():
    
    def __init__(self, nb_infos):
        self.source = "L'équipe"
        self.urls = {'Football': 'http://www.lequipe.fr/rss/actu_rss_Football.xml',
                     'Auto-Moto': 'http://www.lequipe.fr/rss/actu_rss_Auto-Moto.xml',
                     'Tennis': 'http://www.lequipe.fr/rss/actu_rss_Tennis.xml',
                     'Rugby': 'http://www.lequipe.fr/rss/actu_rss_Rugby.xml',
                     'Basketball': 'http://www.lequipe.fr/rss/actu_rss_Basket.xml',
                     'Handball': 'http://www.lequipe.fr/rss/actu_rss_Hand.xml',
                     'Judo': 'http://www.lequipe.fr/rss/actu_rss_Judo.xml',
                     'Ski': 'http://www.lequipe.fr/rss/actu_rss_Ski.xml',
                     'Athlétisme': 'http://www.lequipe.fr/rss/actu_rss_Athletisme.xml',
                     'Natation': 'http://www.lequipe.fr/rss/actu_rss_Natation.xml',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class Sports():
    
    def __init__(self, nb_infos):
        self.source = "Sports.fr"
        self.urls = {'Football': 'http://sports.feedsportal.com/c/282/f/3667/index.rss',
                     'Basketball': 'http://sports.feedsportal.com/c/282/f/3663/index.rss',
                    'Athlétisme': 'http://sports.feedsportal.com/c/282/f/3661/index.rss',
                    'Auto-Moto': 'http://sports.feedsportal.com/c/282/f/3662/index.rss',
                    'Boxe': 'http://sports.feedsportal.com/c/282/f/3665/index.rss',
                    'Cyclisme': 'http://sports.feedsportal.com/c/282/f/3666/index.rss',
                    'Basketball': 'http://sports.feedsportal.com/c/282/f/3663/index.rss',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class YahooSport():
    
    def __init__(self, nb_infos):
        self.source = "Yahoo Sport"
        self.urls = {'Football': 'https://fr.news.yahoo.com/rss/football',
                     'Auto-Moto': 'https://fr.news.yahoo.com/rss/formule-1',
                     'Cyclisme': 'https://fr.news.yahoo.com/rss/cyclisme',
                     'Rugby': 'https://fr.news.yahoo.com/rss/rugby',
                     'Tennis': 'https://fr.news.yahoo.com/rss/tennis',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class Sport365():
    
    def __init__(self, nb_infos):
        self.source = "Sport365"
        self.urls = {'Tennis': 'http://sport365.feedsportal.com/c/356/f/599900/index.rss',
                     'Auto-Moto': 'http://sport365.feedsportal.com/c/356/f/599888/index.rss',
                     'Basketball': 'http://sport365.feedsportal.com/c/356/f/599889/index.rss',
                     'Volley-ball': 'http://sport365.feedsportal.com/c/356/f/599885/index.rss',
                     'Handball': 'http://sport365.feedsportal.com/c/356/f/599877/index.rss',
                     'Judo': 'http://sport365.feedsportal.com/c/356/f/618211/index.rss',
                     'Natation': 'http://sport365.feedsportal.com/c/356/f/599896/index.rss',
                     'Boxe': 'http://sport365.feedsportal.com/c/356/f/599890/index.rss',
                     'Cyclisme': 'http://sport365.feedsportal.com/c/356/f/599891/index.rss',
                     'Athlétisme': 'http://sport365.feedsportal.com/c/356/f/599887/index.rss'}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class FranceFootball():
    
    def __init__(self, nb_infos):
        self.source = "France Football"
        self.urls = {'Football': 'http://www.francefootball.fr/rss/feed.xml',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class FootMercato():
    
    def __init__(self, nb_infos):
        self.source = "Foot Mercato"
        self.urls = {'Football': 'http://www.footmercato.net/flux-rss',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class BasketUSA():
    
    def __init__(self, nb_infos):
        self.source = "Basket USA"
        self.urls = {'Basketball': 'http://www.basketusa.com/feed/',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
class BasketSession():
    
    def __init__(self, nb_infos):
        self.source = "Basket Session"
        self.urls = {'Basketball': ' http://www.basketsession.com/feed/',}
        
        for sport, url in self.urls.iteritems():
            ArticleGetter.get_infos(self.source, nb_infos, sport, url)
            
            
            
            
            
           