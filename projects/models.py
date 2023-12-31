from re import T
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField(null=True,)
    project_url = models.URLField(max_length=200, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.release_date})'
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date',]

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return f'{self.name}'