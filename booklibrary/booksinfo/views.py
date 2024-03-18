from django.shortcuts import render, redirect, HttpResponse
from booksinfo import models

# Create your views here.
def index(request):
    return HttpResponse("This is index page.")