# -*- coding: utf-8 -*-
import twitter
from twitter import *
from SportsHubApp.models import Article
        
class Twitter :
        
    def __init__(self, sources, nb_infos):
        self.consumer_key = "zOo1wwQtLobXPbHJNsZBhmaG1"
        self.secret_key = "bsRzH8fCzHpoZbRotXFXwfEgGChLGD7uSHjWToPuKqpXZt2eL8"
        self.access_token = "2329271624-go4nwaEGuEE8WmOYQmbUd58c3Pz6xqTwjlN0yMj"
        self.access_token_secret = "yw2BFs7xEXjUT7jo5w48r2Jyefe0ShYOQjW4g2SFD9AE3"
        self.get_infos(sources, nb_infos)
        
    def get_infos(self, sources, nb_infos):
    
        api = twitter.Api(consumer_key=self.consumer_key,
                          consumer_secret=self.secret_key,
                          access_token_key=self.access_token,
                          access_token_secret=self.access_token_secret)

        tweets = api.GetHomeTimeline()

        for tweet in tweets:
            try:
                if str(tweet._user._name) in sources:
                    origin = tweet._user._name
                    title = tweet._text
                    lien = tweet.urls[0].url
                    bdd_article = Article(titre=title,
                                          origine=origin,
                                          lien=lien,
                                          type="Twitter")
                    bdd_article.save()
            except Exception as e:
                print "ERROR: " + str(e)

                
        
