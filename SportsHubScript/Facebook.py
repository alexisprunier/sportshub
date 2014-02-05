# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
from SportsHubApp import models

class Facebook:
    def __init__(self,url,source,nb_infos):
        self.url = url
        self.source = source
        try:
            self.get_infos(nb_infos)
        except : pass
        
    def get_infos(self, nb_infos):
        
        html = urllib.urlopen(self.url).read()
        page_web = BeautifulSoup(html)
                
        list_art = page_web.find_all("item", limit=nb_infos)
        for article in list_art:
            try:
                title = (article.find("title")).text
                content = article.find("description").text
                news_link = article.find("link").text
                typeArt = "facebook"

                #BDD
                bdd_article = models.Article(
                                             titre=title,
                                             origine=self.source,
                                             contenu=content,
                                             type=typeArt,
                                             lien=news_link)
                bdd_article.save()
            except:
                pass