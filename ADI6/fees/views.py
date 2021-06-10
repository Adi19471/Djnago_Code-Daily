from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_python(request):
    return HttpResponse("learn Python that will give job")

def learn_django(request):
    return HttpResponse("learn Django that will give django job ")