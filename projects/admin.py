from django.contrib import admin

from .models import Project, Comment, Category

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Category)