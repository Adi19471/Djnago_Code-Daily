from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'core/base.html')

def home(request):
    return render(request, 'core/home.html',{'d':'django'})


def about(request):
    return render(request, 'core/about.html')