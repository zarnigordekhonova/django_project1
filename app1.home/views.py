from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_info(request):
    return HttpResponse('<h1>Hello Dekhonova Zarnigor<hr/>')

def get_university_info(request):
    return HttpResponse('<h1>UzJMCU, International Relations freshman<hr/>')
