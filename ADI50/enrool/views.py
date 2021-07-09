from django.shortcuts import render

from .forms import Apply

from .models import User
# Create your views here.
def home_view(request):
    if request.method == 'POST':
     fm = Apply(request.POST)
     if fm.is_valid():
       na = fm.cleaned_data['name']
       em = fm.cleaned_data['email']
       pa = fm.cleaned_data['password']
       print(na)
       print(em)
       print(pa)
    else:
     fm = Apply()

    return render(request, 'enrool/home_view.html',{'form':fm})