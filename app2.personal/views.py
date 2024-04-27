from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_interests(request):
    return HttpResponse('<h1>Actually, I\'m so interested in playing musical instruments\n and travelling<hr/>')


def get_hobbies(request):
    return HttpResponse('<h1>My favorite hobby is watching sci-fi movies<hr/>')