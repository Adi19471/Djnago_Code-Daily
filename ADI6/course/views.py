from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Html(request):
    return HttpResponse(200)

def css(request):
    return HttpResponse(105)