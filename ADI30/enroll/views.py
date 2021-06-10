from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .forms import StudentRegistration



def show(request):
    #f = StudentRegistration(auto_id=True,label_suffix='::',initial={'name':'chinna','email':'chinna@gmail.com'})
    f = StudentRegistration()
   
    f.order_fields(field_order=['email','first_name'])
    print(f.as_p)
    # return HttpResponse("okay")
    return render(request, 'enroll/s.html',{'fm':f})
