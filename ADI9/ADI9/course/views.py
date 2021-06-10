from django.shortcuts import render
from django.http import HttpResponse



def learn_django(request):
    return HttpResponse("<h1>DJANGO course Tutorial</h1>")


def learn_python(request):
    return HttpResponse("<h2>PYTHON course Tutorial</h2>")

