from django.shortcuts import render
from SportsHubApp.models import Article
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def accueil(request):
    
    if Article.objects.count() >= 1:
        last_articles = list(Article.objects.all().order_by("id")[Article.objects.all().count()-Article.objects.count():])
    else:
        last_articles = None
    
    last_articles += last_articles
    last_articles += last_articles
    last_articles += last_articles
    
    last_id = last_articles[0].id;
    
    last_articles = reversed(last_articles)
    
    return render(request, 'accueil.html', locals())

@csrf_exempt
def refresh(request):
    
    nb_new_article = Article.objects.filter(id__gt=int(request.POST.get('last_id', False))).count()
    sended_text = str(nb_new_article) + " Nouvelles Actus !"
    if nb_new_article != 0:
        return HttpResponse(sended_text)

@csrf_exempt
def get_news(request):
    
    new_articles = Article.objects.filter(id__gt=int(request.POST.get('last_id', False)))
    new_articles = reversed(new_articles)
    
    content = ''
    
    for article in new_articles:
        if article.type == "article":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title-new'>" + unicode(article.titre) + "</div>\
                    <div class='origine-new'><div class='origine-name'>" + unicode(article.origine) + "</div><img class='favicon' src='" + unicode(request.POST.get('static_url', False)) + "favicon/" + unicode(article.origine) + ".png'/></div>\
                    <div class='date-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-bar'></div>\
                    <img class='img-new' src='" + unicode(article.image) + "'/>\
                </div>"
        
        if article.type == "twitter":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='twitter-img' src='" + unicode(request.POST.get('static_url', False)) + "twitter.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-tw-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-tw-bar'></div>\
                </div>"
        
        if article.type == "facebook":
            content += "\
                <div class='new' id='" + unicode(article.id) + "' style='display: none'>\
                    <div class='title'>" + unicode(article.titre) +"</div>\
                    <div class='origine'>" + unicode(article.origine) + "</div>\
                    <img class='facebook-img' src='" + unicode(request.POST.get('static_url', False)) + "facebook.png'/>\
                    <img class='open-quote' src='" + unicode(request.POST.get('static_url', False)) + "open-quote.png'/>\
                    <img class='close-quote' src='" + unicode(request.POST.get('static_url', False)) + "close-quote.png'/>\
                    <div class='date-fb-new'>" + unicode(article.date.strftime('%H:%M')) + "</div>\
                    <div class='bottom-fb-bar'></div>\
                </div>"
    
    return HttpResponse(content)
