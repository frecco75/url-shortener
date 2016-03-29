# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from forms import ShortUrlForm
from models import ShortURL


def home(request):
    shortURLList = ShortURL.objects.order_by('-nb_acces')
    return render(request, 'url_shortener/home.html', {'shortURLList' : shortURLList})

def go_to_home(request):
    return redirect(home)
    
def read(request, token):
    try:
        shortUrl = ShortURL.objects.get(code=token)
        shortUrl.nb_acces += 1
        shortUrl.save()
        return redirect(shortUrl.url, permanent=True)
    except ShortURL.DoesNotExist:
        return go_to_home(request)

def add(request):
    if request.method == 'POST':
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return go_to_home(request)
    else:
        form = ShortUrlForm()

    return render(request, 'url_shortener/add.html', {'form': form})