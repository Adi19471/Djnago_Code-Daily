from django.shortcuts import render

from .forms import StudentData

# Create your views here.
def home(request):
    StudentData()
    return render(request, 'enroll/home.html',{'StudentData':StudentData})