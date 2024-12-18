from django.shortcuts import render, get_object_or_404, redirect
from .models import Dogs
from .forms import DogsForm
from django.http import HttpResponse

# Home/Index 
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
