from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def ale(request):
    return render(request,"tps.html")

def about(request):
    return render(request,"about.html")

def galeria(request):
    return render(request,"galeria.html")

def propuesta(request):
    return render(request,"propuesta.html")