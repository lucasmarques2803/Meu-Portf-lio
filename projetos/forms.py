from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'release_date',
            'projeto_url',
            'description',
        ]
        labels = {
            'name': 'Título',
            'release_date': 'Data de Lançamento',
            'projeto_url': 'URL do Projeto',
            'description': 'Descrição',
        }

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