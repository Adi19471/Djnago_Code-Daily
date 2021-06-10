from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("LEARN DJANGO")

def learn_html(request):
    return HttpResponse("LEARN HTML")

