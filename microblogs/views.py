from django.shortcuts import render
from django.http import HttpResponse, response

def home(request):
    return render(request, 'home.html')

