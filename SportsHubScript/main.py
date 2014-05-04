# -*- coding: utf-8 -*-
import os, sys

sys.path.append('/home/alexis/Desktop/workspace/SportsHub/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings-sh")

from SportsHubScript.Twitter import Twitter
from SportsHubScript.Facebook import Facebook
from Articles.lequipe import Lequipe
from Articles.sports import Sports
from Articles.yahoo import YahooSport
from Articles.eurosport import Eurosport

GLOBAL_nb_infos = 3

#ARTICLES
print "DEBUT Article"
lequipe = Lequipe(GLOBAL_nb_infos)
sports = Sports(GLOBAL_nb_infos)
yahoo = YahooSport(GLOBAL_nb_infos)
eurosport = Eurosport(GLOBAL_nb_infos)

#FB
print "DEBUT Facebook"
sources = {"beIN SPORTS France": 301300799953924,
           "Intersport": 10151773703860786,
           "Decathlon": 165823830131654,
           "Sport2000": 221584158041000,
           "Equipe de France de Football": 186982054657561,
           "Equipe de France de Basketball": 10151630582241174,
           "Equipe de France de Handball": 113556715321615}

for source, ident in sources.items() :
    print "Facebook: "+source
    o_facebook = Facebook("http://www.facebook.com/feeds/page.php?format=rss20&id="+str(ident), source, GLOBAL_nb_infos)

#TWITTER
print "DEBUT Twitter"
sources = ["Gael_Monfils",
           "airlavillenie",
           "julienbenneteau",
           "nicolas88batum",
           "MATUIDIBlaise",
           "JrmeFernandez",
           "sebchabal",
           "NKARABATIC"]
o_twitter = Twitter(sources, GLOBAL_nb_infos)
    
