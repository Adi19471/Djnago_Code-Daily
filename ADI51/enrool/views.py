from django.shortcuts import render

from .forms import Apply

from .models import User
# Create your views here.
def home_view(request):
    if request.method == 'POST':
      pi = User.objects.get(pk=1)
      fm = Apply(request.POST, instance=pi)
      if fm.is_valid():
       fm.save()
      #  na = fm.cleaned_data['name']
      # #  em = fm.cleaned_data['email']
      # #  pa = fm.cleaned_data['password']
      #  reg = User(name=na)
      #  reg.save()
       
    else:
     fm = Apply()

    return render(request, 'enrool/home_view.html',{'form':fm})