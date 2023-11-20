from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .temp_data import projeto_data

def detail_projeto(request, projeto_id):
    context = {'projeto': projeto_data[projeto_id - 1]}
    return render(request, 'projetos/detail.html', context)

def list_projetos(request):
    context = {"projeto_list": projeto_data}
    return render(request, 'projetos/index.html', context)

def create_projeto(request):
    if request.method == 'POST':
        projeto_data.append({
            'name': request.POST['name'],
            'release_date': request.POST['release_date'],
            'projeto_url': request.POST['projeto_url'],
            'description': request.POST['description'],
        })
        return HttpResponseRedirect(
            reverse('projetos:detail', args=(len(projeto_data), )))
    else:
        return render(request, 'projetos/create.html', {})