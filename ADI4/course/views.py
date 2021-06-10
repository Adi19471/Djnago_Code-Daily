from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    a="hello chinna"
    return HttpResponse(a)

def learn_python(request):
    a=20
    b=14
    c=a+b
    d="hello:",c
    return HttpResponse(d)