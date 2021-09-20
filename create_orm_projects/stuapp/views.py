from django.shortcuts import render

from datetime import datetime
from .models import Student
# Create your views here.
def orm_view(request):

    # student_data = Student.objects.all()
    student_data = Student.objects.in_bulk([1,2,3])
    print("THIS SQL DATA",student_data)
    return render(request,'orm.html',{'top':student_data})