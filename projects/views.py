from multiprocessing import context
from typing import Any
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Project, Comment, Category
from .forms import ProjectForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get(self, request, *args, **kwargs):
        if 'last_projects' not in request.session:
            request.session['last_projects'] = []
        if self.get_object().id in request.session['last_projects']:
            request.session["last_projects"].remove(self.get_object().id)
        request.session['last_projects'] = [self.get_object().id] + request.session['last_projects']
        if len(request.session['last_projects']) > 5:
            request.session['last_projects'] = request.session['last_projects'][:-1]
        return super().get(request, *args, **kwargs)

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        if "last_projects" in self.request.session:
            context['last_projects'] = []
            for project_id in self.request.session['last_projects']:
                context['last_projects'].append(get_object_or_404(Project, pk=project_id))
        
        return context

class ProjectCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Project
    template_name = 'projects/create.html'
    form_class = ProjectForm
    permission_required = 'projects.add_project'

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
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().form_valid(form)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'projects/categories.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        if "last_categories" in self.request.session:
            context['last_categories'] = []
            for category_id in self.request.session['last_categories']:
                context['last_categories'].append(get_object_or_404(Category, pk=category_id))
        
        return context

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'projects/category.html'

    def get(self, request, *args, **kwargs):
        if 'last_categories' not in request.session:
            request.session['last_categories'] = []
        if self.get_object().id in request.session['last_categories']:
            request.session["last_categories"].remove(self.get_object().id)
        request.session['last_categories'] = [self.get_object().id] + request.session['last_categories']
        if len(request.session['last_categories']) > 5:
            request.session['last_categories'] = request.session['last_categories'][:-1]
        return super().get(request, *args, **kwargs)