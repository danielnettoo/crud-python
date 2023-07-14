from django.shortcuts import render, redirect
from app.forms import PersonagensForm
from app.models import Personagens
from django.core.paginator import Paginator


def home(request):
    data = {}
    all = Personagens.objects.all()
    paginator = Paginator(all, 3)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    search = request.GET.get('search')
    if search:
        data['db'] = Personagens.objects.filter(personagem__icontains=search)
    else:
        data['db'] = Personagens.objects.all()
    return render(request, 'index.html', data)


def form(request):
    return render(request, 'form.html')


def form(request):
    data={}
    data['form'] = PersonagensForm
    return render(request, 'form.html', data)


def create(request):
    form = PersonagensForm(request.POST or None)
    if form.is_valid():
           form.save()
           return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Personagens.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Personagens.objects.get(pk=pk)
    data['form'] = PersonagensForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Personagens.objects.get(pk=pk)
    form = PersonagensForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Personagens.objects.get(pk=pk)
    db.delete()
    return redirect('home')