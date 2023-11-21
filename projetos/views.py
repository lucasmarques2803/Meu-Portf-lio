from multiprocessing import context
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from .temp_data import projeto_data

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
        projeto_name = request.POST['name']
        projeto_release_date = request.POST['release_date']
        projeto_url = request.POST['projeto_url']
        projeto_description = request.POST['description']
        projeto = Post(name=projeto_name,
                       release_date=projeto_release_date,
                       projeto_url=projeto_url,
                       description=projeto_description)
        projeto.save()
        return HttpResponseRedirect(
            reverse('projetos:detail', args=(projeto.id, )))
    else:
        return render(request, 'projetos/create.html', {})
    
def update_projeto(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)

    if request.method == 'POST':
        projeto.name = request.POST['name']
        projeto.release_date = request.POST['release_date']
        projeto.projeto_url = request.POST['projeto_url']
        projeto.description = request.POST['description']
        projeto.save()
        return HttpResponseRedirect(
            reverse('projetos:detail', args=(projeto.id, )))
    
    context = {'projeto': projeto}
    return render(request, 'projetos/update.html', context)
    
def delete_projeto(request, projeto_id):
    projeto = get_object_or_404(Post, pk=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        return HttpResponseRedirect(reverse('projetos:index'))
    
    context = {'projeto': projeto}
    return render(request, 'projetos/delete.html', context)