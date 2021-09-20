from django.shortcuts import render

# Create your views here.
from .models import Student,Techer
from django.db.models import Q

# all data
    # student_data = Student.objects.all()

# only marks
   # student_data = Student.objects.filter(marks = 80)
    
# Exclude no data remaining part print
   # student_data = Student.objects.exclude(marks = 80)

#Oder_by using all are assending


    # student_data = Student.objects.order_by('id')
    # student_data = Student.objects.order_by("name")
    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by("city")
    # student_data = Student.objects.order_by("pass_date")


# order data formart reverse method format.> id reverse only
    # student_data = Student.objects.order_by('id').reverse()[:]


# value dispaly 
    # student_data = Student.objects.values('name','marks','city')

# value_list 
    # student_data = Student.objects.values_list()

    # student_data = Student.objects.values_list('id','name')
    # student_data = Student.objects.values_list('id','name',named=True)

    # student_data = Student.objects.order_by('roll').reverse()

    # print(student_data.order_by('id').reverse()[0:6])

    # student_data = Student.objects.using('default')
# data filed 
    # student_data = Student.objects.dates('pass_date' ,"year")
    # student_data = Student.objects.dates('pass_date','year')
    


    # print(student_data.query)
    # get_id_4 = Student.objects.get(id=4)


    # print("Total Querty:",student_data)
    # print()
    # print("TotalCount",student_data)
    # print()
    # print("Sql Query only id-4",get_id_4)
    # print()
    # print("SQL only Query",student_data.query)
    # print()

    # print("marks only",student_data )
def home_view(request):
    # q1 = Student.objects.values_list('id','name',named=True)
    # q2 = Techer.objects.values_list('id','name',named=True)
    
    # student_data = q1.union(q2)

    # q1 = Techer.objects.values_list('id','name',named=True)
    # q2 = Techer.objects.values_list('id','name',named=True)
    
    # student_data = q1.union(q2,all=True)

    # q2 = Student.objects.values_list('id','name',named=True)
    # q1 = Techer.objects.values_list('id','name',named=True)

    # student_date = q2.difference(q1)

    # print(q1)
    # print(q2)
    # # student_data = Student.objects.union()




    student_data = Student.objects.filter(id=6,city="hyderabad") | Student.objects.filter(id=4,city='Tadipatri')
    student_data = Student.objects.filter(Q(id=6) | Q(id=1))

    student_data = Student.objects.all()
    print(student_data.query)
    context = {
        'student_data':student_data
    }


    return render(request,'query/home.html',context)

################################################### TECHER MODEL PRINT#####################################