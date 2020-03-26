from django.contrib.auth import views as auth_views
from django.urls import path

from . import views, news_article_views

app_name = "homepage"

login_view = auth_views.LoginView.as_view(template_name="login_form.html")
logout_view = auth_views.LogoutView.as_view()

urlpatterns = [
    path('',                      views.home,                 name='home'),
    path('login',                 login_view,                 name='login'),
    path('logout',                logout_view,                name='logout'),

    path('news/<int:id>',         news_article_views.view,    name='news_article_view'),
    path('news/new',              news_article_views.new,     name='news_article_new'),
    path('news/edit/<int:id>',    news_article_views.edit,    name='news_article_edit'),
    path('news/remove/<int:id>',  news_article_views.remove,  name='news_article_remove'),
]

