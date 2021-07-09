from django.shortcuts import render

# forms to import Apply views
from.forms import Apply
# models import views
from.models import User



# Create your views here.
def home_view(request):
    if request.method == 'POST':
     fm = Apply(request.POST)
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pa = fm.cleaned_data['password']

      #reg = User(id = 1 ,name=nm,email=em,password=pa)

    # data save backend
      #reg.save()
     reg = User(id=2)
     reg.delete()
    else:
     fm = Apply()
    return render(request,'data/home_view.html',{'form':fm})