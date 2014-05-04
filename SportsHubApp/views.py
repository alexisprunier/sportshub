from django.shortcuts import render
from SportsHubApp.models import Article
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def accueil(request):
    
    if Article.objects.count() >= 1:
        if Article.objects.count() < 30:
            quantity = Article.objects.count()
        else:
            quantity = 30
        last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-quantity:])
    else:
        last_articles = None
    last_id = last_articles[0].id
    last_articles = reversed(last_articles)
    
    return render(request, 'accueil.html', locals())

@csrf_exempt
def refresh(request):
    
    filters = json.loads(request.POST.get('filters', False))
    sources = []
    for _, src in filters.items():
        sources += src.split(";")
    sources.append(None)
    nb_new_article = Article.objects.filter(id__gt=int(request.POST.get('last_id', False)),
                                          type__in=filters.keys(),
                                          sport__in=filters["Sports"].split(";"),
                                          origine__in=sources).count()
    sended_text = str(nb_new_article) + " Nouvelles Actus !"
    if nb_new_article != 0:
        return HttpResponse(sended_text, True)
    else:
        return HttpResponse(sended_text, False)

@csrf_exempt
def get_news(request):
    
    filters = json.loads(request.POST.get('filters', False))
    sources = []
    for _, src in filters.items():
        sources += src.split(";")
    sources.append(None)
    new_articles = Article.objects.filter(id__gt=int(request.POST.get('last_id', False)),
                                          type__in=filters.keys(),
                                          sport__in=filters["Sports"].split(";"),
                                          origine__in=sources)
    new_articles = reversed(new_articles)
    content = ''
    print new_articles
    for article in new_articles:
        if article.type == "Articles":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title-new'>" + unicode(article.titre) + "</div>\
                    <div class='origine-new'><div class='origine-name'>" + unicode(article.origine) + "</div><img class='favicon' src='" + unicode(request.POST.get('static_url', False)) + "favicon/" + unicode(article.origine) + ".png'/></div>\
                    <div class='date-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-bar " + unicode(article.sport)+ "'></div>\
                    <img class='img-new' src='" + unicode(article.image) + "'/>\
                </div>"
        
        if article.type == "Twitter":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='twitter-img' src='" + unicode(request.POST.get('static_url', False)) + "twitter.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-tw-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-tw-bar " + unicode(article.sport)+ "'></div>\
                </div>"
        
        if article.type == "Facebook":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='facebook-img' src='" + unicode(request.POST.get('static_url', False)) + "facebook.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-fb-new " + unicode(article.sport)+ "'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-fb-bar'></div>\
                </div>"
    
    return HttpResponse(content)

@csrf_exempt
def apply_news(request):
    
    filters = json.loads(request.POST.get('filters', False))
    sources = []
    for _, src in filters.items():
        sources += src.split(";")
    sources.append(None)
    new_articles = Article.objects.filter(type__in=filters.keys(),
                                          sport__in=filters["Sports"].split(";"),
                                          origine__in=sources)
    new_articles = reversed(new_articles)
    content = ''
    print new_articles
    for article in new_articles:
        if article.type == "Articles":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title-new'>" + unicode(article.titre) + "</div>\
                    <div class='origine-new'><div class='origine-name'>" + unicode(article.origine) + "</div><img class='favicon' src='" + unicode(request.POST.get('static_url', False)) + "favicon/" + unicode(article.origine) + ".png'/></div>\
                    <div class='date-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-bar " + unicode(article.sport)+ "'></div>\
                    <img class='img-new' src='" + unicode(article.image) + "'/>\
                </div>"
        
        if article.type == "Twitter":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='twitter-img' src='" + unicode(request.POST.get('static_url', False)) + "twitter.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-tw-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-tw-bar " + unicode(article.sport)+ "'></div>\
                </div>"
        
        if article.type == "Facebook":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='facebook-img' src='" + unicode(request.POST.get('static_url', False)) + "facebook.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-fb-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-fb-bar " + unicode(article.sport)+ "'></div>\
                </div>"
    
    return HttpResponse(content)
