from django.shortcuts import render


# Create your views here.
from .forms import StudentRegistration



def show(request):
    f = StudentRegistration(auto_id=True,label_suffix='::',initial={'name':'chinna','email':'chinna@gmail.com'})
    return render(request, 'enroll/show.html',{'f':f})
