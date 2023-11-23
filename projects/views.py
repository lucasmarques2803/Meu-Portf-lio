from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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

def create_comment(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            project=project)
            comment.save()
            return HttpResponseRedirect(
                reverse('projects:detail', args=(project_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'project': project}
    return render(request, 'projects/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'projects/categories.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'projects/category.html'