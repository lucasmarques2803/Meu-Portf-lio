from multiprocessing import context
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Project, Comment, Category
from .forms import ProjectForm, CommentForm

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

class ProjectCreateView(generic.CreateView):
    model = Project
    template_name = 'projects/create.html'
    form_class = ProjectForm

    def get_success_url(self) -> str:
        return reverse('projects:detail', args=(self.object.id, ))
    
class ProjectUpdateView(generic.UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForm

    def get_success_url(self) -> str:
        return reverse('projects:detail', args=(self.object.id, ))

class ProjectDeleteView(generic.DeleteView):
    model = Project
    template_name = 'projects/delete.html'

    def get_success_url(self) -> str:
        return reverse('projects:index')
    
class CommentCreateView(generic.CreateView):
    model = Comment
    template_name = 'projects/comment.html'
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse('projects:detail', args=(self.object.project.id, ))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'projects/categories.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'projects/category.html'