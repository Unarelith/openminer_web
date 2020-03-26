from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="news_articles", null=True)

    class Meta:
        verbose_name = "News article"
        ordering = ['date']

    def __str__(self):
        return self.title

