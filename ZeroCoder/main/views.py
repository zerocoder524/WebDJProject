from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'caption':"CatDjango"})


def new(request):
    return render(request, 'main/new.html')
