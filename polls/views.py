from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def something(request):
    return HttpResponse("hi there this is a test ")

def anotherSomething(request):
    return HttpResponse(
        "bla bla blaaa"
    )
