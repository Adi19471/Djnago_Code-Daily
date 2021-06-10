from django.shortcuts import render

# Create your views here.
def learn_djcourse(request):
    return render(request,'courseone.html')

def learn_djfees(request):
    return render(request,'coursetwo.html')