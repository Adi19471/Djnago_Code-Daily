from django.shortcuts import render
from .forms import HeroForm  
from  .models import Hero
# Create your views here.
def home(request):
  
    fm = HeroForm()   
    return render(request,'home.html',{'form':fm})