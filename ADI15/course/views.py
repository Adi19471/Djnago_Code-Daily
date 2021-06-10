from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request, 'course/courseone.html',{'name':'DJANGO','des':'developer'})

def python(request):
    return render(request, 'course/coursetwo.html')