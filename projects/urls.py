from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category'),
]