from django.shortcuts import render

# Create your views here.
from .models import Student,Techer

def home_view(request,id):
    return render
    student_data = Student.objects.get(name="adi")

   
    context = {
        'student_data':student_data
    }


    return render(request,'query/home.html',context)

################################################### TECHER MODEL PRINT#####################################