from django.shortcuts import render
from .forms import StudentData
# Create your views here.
def formss(request):

    # f = StudentData(label_suffix="::",initial={'name':'Enter Your name','email':'Enter Your Email'})
    f = StudentData()
    f.order_fields(field_order=['email','email'])
    return render (request,'enroll/formss.html',{'f':f})