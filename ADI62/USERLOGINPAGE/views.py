from django.shortcuts import render
from .forms import UserCreationForm
from django.contrib import messages 
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
      fm = UserCreationForm(request.POST)
      if fm.is_valid():
        fm.save()
        messages.info(request,'succesfull complted the work')
    else:
     fm = UserCreationForm()
    return render(request, 'USERLOGINPAGE/sign_up.html',{'form':fm}) 