from re import T
from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateTimeField(null=True,)
    projeto_url = models.URLField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.release_date})'
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    projeto = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'