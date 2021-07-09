from django.shortcuts import render

from .forms import StudentData

# Create your views here.
def home(request):
    if request.method =="POST":
        fm = StudentData(request.POST)
        if fm.is_valid():
          print("yes the data is successfull")
          name = fm.cleaned_data['name']
          email = fm.cleaned_data['email']
          print('Name',name)
          print('Email',email)
          fm = StudentData()
    else:
        
     fm = StudentData()
     print("yes get request ")


    fm = StudentData()
    return render(request, 'enroll/home.html',{'form':fm})