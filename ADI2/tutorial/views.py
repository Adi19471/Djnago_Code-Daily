from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


# def home(request):
#     a="hello raja"
#     return HttpResponse(a)

def math(request):
    a=110
    b=15
    c=a+b
    d="your lcukky number raj totally ur frow HIMA"
    fa=d
    return HttpResponse(fa)
