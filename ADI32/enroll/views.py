from django.shortcuts import render

from .forms import StudentData

# Create your views here.
def home(request):
    f = StudentData()
    return render(request, 'enroll/home.html',{"f":f})