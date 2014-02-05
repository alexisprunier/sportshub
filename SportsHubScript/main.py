# -*- coding: utf-8 -*-
import os, sys
from SportsHubScript import Facebook

sys.path.append('/home/alexis/workspace/SportsHub/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

GLOBAL_nb_infos = 2

#FB
print "DEBUT Facebook"
sources = {"Materiel.net":320776853364, 
          "LDLC":121548574526465, 
          "Rue du Commerce":119794289202,
          "Top Achat":123427650425,
          "GrosBill": 312422015254,
          }

for source,id in sources.items() :
    print "Facebook: "+source
    o_facebook = Facebook("http://www.facebook.com/feeds/page.php?format=rss20&id="+str(id), source, GLOBAL_nb_infos)

#TWITTER
print "DEBUT Twitter"
sources = ["fleurpellerin",
           "..."]
#o_twitter = Twitter(sources, GLOBAL_nb_infos)
    