from django.shortcuts import render
from django.contrib import messages

from .forms import StudentRegistration

# Create your views here.
def messages_page(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         fm.save()
         messages.add_message(request, messages.SUCCESS,'your account is opened')
         messages.info(request,"django database stored")
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/message.htm',{'form':fm})