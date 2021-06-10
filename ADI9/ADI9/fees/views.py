from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def django_fees(request):
    return HttpResponse("<h1>200</h1>")


def python_fees(request):
    return HttpResponse("<h1>200</h1>")