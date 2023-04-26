from urllib.request import Request
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
         characters.extend('!@#$%^&*()_+-="№;:?*')
    if request.GET.get('numbers'):
         characters.extend('1234567890')
    
    lenght = int(request.GET.get('length', 12))
    
    thepassword = ''
    for i in range(lenght):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')