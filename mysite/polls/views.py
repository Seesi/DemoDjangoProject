from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, word. You're at teh polls index.")

# Create your views here.
