from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.admin.views.decorators import staff_member_required

from .models import NewsArticle
from .forms import NewsArticleForm

def view(request, id):
    article = get_object_or_404(NewsArticle, id=id)
    return render(request, 'homepage/news_article_view.html', locals())

@staff_member_required
def new(request):
    form = NewsArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form_ok = True
        news_article = form.save(commit=False)
        news_article.user = request.user
        try:
            news_article.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('homepage:news_article_view', kwargs={"id": news_article.id}), permanent=True)
        else:
            return redirect(reverse('homepage:home') + '?new=ko', permanent=True)

    model_name = "news_article"
    return render(request, 'object_new.html', locals())

@staff_member_required
def edit(request, id):
    news_article = get_object_or_404(NewsArticle, id=id)
    form = NewsArticleForm(request.POST or None, request.FILES or None, instance=news_article)
    if form.is_valid():
        form_ok = True
        newnews_article = form.save(commit=False)
        news_article = newnews_article
        news_article.user = request.user
        try:
            news_article.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('homepage:news_article_view', kwargs={"id": news_article.id}), permanent=True)
        else:
            return redirect(reverse('homepage:home') + '?edit=ko', permanent=True)

    model_name = "news_article"
    model_id = news_article.id
    return render(request, 'object_edit.html', locals())

@staff_member_required
def remove(request, id):
    news_article = get_object_or_404(NewsArticle, id=id)
    news_article.delete()

    return redirect(reverse('homepage:home') + "?delete=ok", permanent=True)


