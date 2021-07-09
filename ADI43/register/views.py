from django.shortcuts import render

from .forms import Reg

# Create your views here.
def home(request):
    if request.method == "POST":
        fm = Reg(request.POST)
        if fm.is_valid():
         print('Form.Validated')
         print('name:',fm.cleaned_data['name'])
         print('email:',fm.cleaned_data['email'])
         print('PASSWORD',fm.cleaned_data['password'])
    else:
     fm = Reg()

    return render(request, 'register/home.html',{'form':fm})