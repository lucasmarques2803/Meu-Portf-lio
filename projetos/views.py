from multiprocessing import context
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def detail_projeto(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)
    context = {'projeto': projeto}
    return render(request, 'projetos/detail.html', context)

def list_projetos(request):
    projeto_list = Post.objects.all()
    context = {"projeto_list": projeto_list}
    return render(request, 'projetos/index.html', context)

def create_projeto(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            projeto_name = form.cleaned_data['name']
            projeto_release_date = form.cleaned_data['release_date']
            projeto_url = form.cleaned_data['projeto_url']
            projeto_description = form.cleaned_data['description']
            projeto = Post(name=projeto_name,
                          release_date=projeto_release_date,
                          projeto_url=projeto_url,
                          description=projeto_description)
            projeto.save()
            return HttpResponseRedirect(
                reverse('projetos:detail', args=(projeto.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'projetos/create.html', context)
    
def update_projeto(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            projeto.name = form.cleaned_data['name']
            projeto.release_date = form.cleaned_data['release_date']
            projeto.projeto_url = form.cleaned_data['projeto_url']
            projeto.description = form.cleaned_data['description']
            projeto.save()
            return HttpResponseRedirect(
                reverse('projetos:detail', args=(projeto.id, )))
    else:
        form = PostForm(
            initial={
                'name': projeto.name,
                'release_date': projeto.release_date,
                'projeto_url': projeto.projeto_url,
                'description': projeto.description,
            })

    context = {'projeto': projeto, 'form': form}
    return render(request, 'projetos/update.html', context)
    
def delete_projeto(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        return HttpResponseRedirect(reverse('projetos:index'))
    
    context = {'projeto': projeto}
    return render(request, 'projetos/delete.html', context)