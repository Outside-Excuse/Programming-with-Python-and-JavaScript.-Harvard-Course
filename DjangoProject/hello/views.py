from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
    #return HttpResponse("Hello, Alejandro Hidalgo Badillo!")

def Tomasa(request):
    return HttpResponse("Hello, Tomasa!")

def Daniel(request):
    return HttpResponse("Hello, Daniel Hidalgo!")

def greet(request, name):
    #return HttpResponse(f"hello! {name.capitalize()}")
    return render(request,"hello/greet.html", {
        "name": name.capitalize()
    })