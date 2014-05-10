# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from SportsHubApp.models import Article
import urllib

class Facebook:
    
    def __init__(self,url,source,nb_infos):
        self.url = url
        self.source = source
        self.get_infos(nb_infos)
        
    def get_infos(self, nb_infos):
        
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
        
        list_art = page_web.find_all("item", limit=nb_infos)
        
        for article in list_art:
            try:
                title = (article.find("title")).text\
                            .replace("&#xe8;", u"è")\
                            .replace("&#xe7;", u"ç")\
                            .replace("&#xe9;", u"é")\
                            .replace("&#039;", u"'")\
                            .replace("&#x20ac;", u"€")\
                            .replace("&#xe0;", u"à")
                news_link = article.find("link").text
                bdd_article = Article(titre=title,
                                     origine=self.source,
                                     type="Facebook",
                                     lien=news_link,
                                     sport="")
                bdd_article.save()
            except Exception as e:
                print "ERROR: " + str(e)