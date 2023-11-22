from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'projetos/detail.html'

class PostListView(generic.ListView):
    model = Post
    template_name = 'projetos/index.html'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'projetos/create.html'
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('projetos:detail', args=(self.object.id, ))
    
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'projetos/update.html'
    form_class = PostForm

    def get_success_url(self) -> str:
        return reverse('projetos:detail', args=(self.object.id, ))

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'projetos/delete.html'

    def get_success_url(self) -> str:
        return reverse('projetos:index')

def create_comment(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            projeto=projeto)
            comment.save()
            return HttpResponseRedirect(
                reverse('projetos:detail', args=(projeto_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'projeto': projeto}
    return render(request, 'projetos/comment.html', context)