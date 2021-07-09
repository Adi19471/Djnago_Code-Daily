from django.shortcuts import render
from .forms import StudentRegister

# Create your views here.
def student(request):
    fm = StudentRegister()
    return render(request, 'enrolldata/student_page.html',{'form':fm})