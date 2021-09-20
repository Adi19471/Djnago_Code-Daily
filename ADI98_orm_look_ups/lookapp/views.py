from django.shortcuts import render

from datetime import date,time
# Create your views here.
from .models import Student
def look_views(request):
    # student_data = Student.objects.all()
    #student_data = Student.objects.filter(name__exact="chinna")

    # student_data = Student.objects.filter(name__iexact="chinna")

    # student_data = Student.objects.filter(name__exact="hima")


    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__contains='c')
    # student_data = Student.objects.filter(name__contains='U')
    # student_data = Student.objects.filter(marks__in=[95])

    # student_data = Student.objects.filter(marks__gt=95)
    # student_data = Student.objects.filter(marks__gte=80)
    # student_data = Student.objects.filter(marks__lt = 80)
    # student_data = Student.objects.filter(marks__lte = 80)
    # student_data = Student.objects.filter(name__startswith ='c')
    # student_data = Student.objects.filter(name__istartswith ='s')
    # student_data = Student.objects.filter(name__endswith ='C')
    # student_data = Student.objects.filter(name__iendswith ='C')
    # student_data = Student.objects.filter(passdate__range=('2021-09-04','2021-09-19'))
    # student_data = Student.objects.filter(admdatetime__date=date(2021,9,20))
    # student_data = Student.objects.filter(admdatetime__date__gte=date(2021,9,20))
    # student_data = Student.objects.filter(admdatetime__date__lte=date(2021,9,20))
    # student_data = Student.objects.filter(passdate__year__gte=2021)
    # student_data = Student.objects.filter(passdate__year__gt=2021)
    # student_data = Student.objects.filter(passdate__year__lte= 2021)
    # student_data = Student.objects.filter(passdate__week__gte= 14)
    # student_data = Student.objects.filter(passdate__day__lte= 14)
    # student_data = Student.objects.filter(passdate__week__gt= 14)
    # student_data = Student.objects.filter(admdatetime__time__gt=time(1,24))
    # student_data = Student.objects.filter(admdatetime__minute=20)
    # student_data = Student.objects.filter(admdatetime__second__lte=60)
    student_data = Student.objects.all()
    student_dataa = Student.objects.all().count()










    
    





    print("Return",student_data)
    print()
    print("SQL Query:",student_data.query)

    context = {
        'student_data':student_data,
        'student_dataa':student_dataa
    }
    return render(request,'look/lok.html',context)

   