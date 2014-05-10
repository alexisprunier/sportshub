# -*- coding: utf-8 -*-
import os, sys

sys.path.append('/home/alexis/Desktop/workspace/SportsHub/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings-sh")

from SportsHubScript.Twitter import Twitter
from SportsHubScript.Facebook import Facebook
from Articles.ArticleGetter import Eurosport 
from Articles.ArticleGetter import Sports 
from Articles.ArticleGetter import YahooSport 
from Articles.ArticleGetter import Sport365 
from Articles.ArticleGetter import Lequipe 
from Articles.ArticleGetter import BasketUSA
from Articles.ArticleGetter import BasketSession
from Articles.ArticleGetter import FranceFootball
from Articles.ArticleGetter import FootMercato

GLOBAL_nb_infos = 3

#ARTICLES
print "DEBUT Article"
lequipe = Lequipe(GLOBAL_nb_infos)
sports = Sports(GLOBAL_nb_infos)
yahoo = YahooSport(GLOBAL_nb_infos)
eurosport = Eurosport(GLOBAL_nb_infos)
sport365 = Sport365(GLOBAL_nb_infos)
franceFootball = FranceFootball(GLOBAL_nb_infos)
footMercato = FootMercato(GLOBAL_nb_infos)
basketUsa = BasketUSA(GLOBAL_nb_infos)
basketSession = BasketSession(GLOBAL_nb_infos)

#FB
print "DEBUT Facebook"
sources = {"beIN SPORTS France": 301300799953924,
           "Intersport": 43767900785,
           "Decathlon": 122695097770591,
           "Sport2000": 122191497979866,
           "Equipe de France de Football": 112215632152510,
           "Equipe de France de Basketball": 123564846173,
           "Equipe de France de Handball": 69895790042}

for source, ident in sources.items() :
    print "Facebook: "+source
    o_facebook = Facebook("http://www.facebook.com/feeds/page.php?format=rss20&id="+str(ident), source, GLOBAL_nb_infos)

#TWITTER
print "DEBUT Twitter"
sources = ["Gael Monfils",
           "Renaud Lavillenie",
           "julien benneteau",
           "Nicolas Batum",
           "Blaise MATUIDI",
           "Jérôme Fernandez",
           "Sébastien Chabal",
           "NIKOLA KARABATIC",]
o_twitter = Twitter(sources, GLOBAL_nb_infos)
    
