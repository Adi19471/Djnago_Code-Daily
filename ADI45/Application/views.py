from django.shortcuts import render
from django.http import HttpResponse

from .forms import Tata

# Create your views here.
def home(request):
    if request.method =='POST':
     fm = Tata(request.POST)
     if fm.is_valid():
         print('store the data here')
         print('Name:', fm.cleaned_data['name'])
         print('Email:', fm.cleaned_data['email'])
         print('Password:', fm.cleaned_data['password'])
         print('RPassword:', fm.cleaned_data['rpassword'])

    else:
     fm =Tata()

    return render(request, 'Application/index.html',{'form':fm})