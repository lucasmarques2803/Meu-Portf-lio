from re import T
from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateTimeField(null=True)
    projeto_url = models.URLField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.release_date})'