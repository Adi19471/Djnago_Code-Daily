from django.shortcuts import render

# Create your views here.
from .models import Student
def Home(request):
    # student_data = Student.objects.order_by('name').first()
    # student_data = Student.objects.all()
    # student_data = Student.objects.order_by('name').last()

    student_data = Student.objects.create(name="Keyybord",scale_type="jksdnfksdh",scale_price="54543")
    student_data.save()

    print("THE DJANGO",student_data)
    
    context = {
        'student_data':student_data
    }
    return render(request,'orm/home.html',context)



