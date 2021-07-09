from django.shortcuts import render
from django.http import HttpResponse

from.forms import StudentRegistration

# Create your views here.
def home(request):
    if request.method == 'POSR':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         print("hello django adi:",['name'])
         print('Name:',fm.cleaned_data['name'])
         print('email:',fm.cleaned_data['email'])
        
           
    else:
      fm = StudentRegistration()
   
    return render(request, 'yes/home.html',{'form':fm})