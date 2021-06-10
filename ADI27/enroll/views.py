from django.shortcuts import render


from enroll.models import Student

# Create your views here.
def Studentinfo(request):

    # stud = Student.objects.get(pk=6)
    stud = Student.objects.all()
    print('my output',stud)
    return render(request,'enroll/studentinfo.html',{'stud':stud})