from django.http import HttpResponse
from django.shortcuts import render

def home(request):#prend une requette est retourne une reponse
    return render(request, 'index.html')

def about(request):#quand la fonction est exécuté j'affiche le template 'pages/about.html'
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

