from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def tps(request):
    return render(request,"tps.html")