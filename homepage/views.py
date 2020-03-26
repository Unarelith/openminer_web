from django.shortcuts import render

from .models import NewsArticle

def home(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'homepage/home.html', locals())

