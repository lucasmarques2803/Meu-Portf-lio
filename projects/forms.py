from django import forms
from django.forms import ModelForm
from .models import Project, Comment

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'release_date',
            'project_url',
            'description',
        ]
        labels = {
            'name': 'Título',
            'release_date': 'Data de Lançamento',
            'project_url': 'URL do Projeto',
            'description': 'Descrição',
        }
        widgets = {'release_date': forms.DateInput(attrs={'type':'date'})}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }