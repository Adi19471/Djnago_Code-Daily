from django.http.response import HttpResponse
from django.shortcuts import render

from django.shortcuts import HttpResponse
def home_view(request):
    return HttpResponse("DJANGO")


def back_view(request):
    return render(request,'site/back.html')