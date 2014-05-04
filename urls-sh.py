from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'SportsHubApp.views.accueil', name=''),
    url(r'refresh', 'SportsHubApp.views.refresh'),
    url(r'get_news', 'SportsHubApp.views.get_news'),
    url(r'apply_news', 'SportsHubApp.views.apply_news'),
    url(r'^admin/', include(admin.site.urls)),
)
