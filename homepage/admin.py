from django.contrib import admin

from .models import NewsArticle

class NewsArticleAdmin(admin.ModelAdmin):
    list_display   = ('title', 'content', 'date', 'user')
    list_filter    = ('user', )
    ordering       = ('title', 'content', 'date', 'user')
    search_fields  = ('title', 'content', 'user')

admin.site.register(NewsArticle, NewsArticleAdmin)

