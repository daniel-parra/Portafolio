from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'servidores/home.html')

def home_servidores(request):
    return render(request, 'servidores/home.html')
