from django.urls import path

from . import views

app_name = 'projetos'
urlpatterns = [
    path('', views.list_projetos, name='index'),
    path('create/', views.create_projeto, name='create'),
    path('<int:projeto_id>/', views.detail_projeto, name='detail'),
]