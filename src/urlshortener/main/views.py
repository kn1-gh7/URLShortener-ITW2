from django.shortcuts import render, redirect
from .models import ShortURLS
import random

def shortener():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(letters) for _ in range(8))

def redirect_to_url(request, user_input):
    url_object = ShortURLS.objects.get(short_url=user_input)
    return redirect(url_object.long_url)

def shorten_url(request):
    short_url = None
    check = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        check = ShortURLS.objects.filter(long_url=user_input).exists()
        if check == False:
            short_url = shortener()
            ShortURLS.objects.create(short_url=short_url, long_url=user_input)
        else:
            url_object = ShortURLS.objects.get(long_url=user_input)
            short_url = url_object.short_url
    return render(request, 'index.html', {'short_url':short_url, 'check':check})

def display_all(request):
    urls = ShortURLS.objects.all()
    return render(request, 'display.html', {'urls':urls})
