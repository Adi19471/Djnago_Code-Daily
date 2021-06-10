from django.shortcuts import render

from datetime import datetime

# Create your views here.
# def learn_django(request):
#     return render(request, 'course/one.html',{'nm':'djnago'})


# def learn_django(request):
#     name ='ADI NARAYANA REDDY'
#     pro = 'DJANGO DEVELOPER'
#     cour = 'DJANGO'
#     dur = '45days'
#     django_learn ={'n':name,'p':pro,'c':cour,'d':dur}
    
#     return render(request, 'course/one.html',context=django_learn)

# def learn_django(request):
#     d = datetime.now()
#     return render(request, 'course\one.html',{'dt':d})


# def learn_django(request):
#     a='14225.33255252'
#     b='00000.25231242110'
#     c='124540.0540011414'
#     abc={'aa':a,'bb':b,'cc':c}

#     return render(request, 'course\one.html',{'p':20352523.5524})


# def learn_django(request):
#     dd=datetime.now()
#     return render(request, 'course/one.html',{'dd':dd,'nm':'dj' ,'st':'django'})

    
# def learn_django(request):
   
#     return render(request, 'course/one.html',{'dj':'2' ,'st':'django'})

# def learn_django(request):
#     student = {'ADI':['Developer','Rajesh','TECH MAHENDRA']}
   
#     return render(request, 'course/one.html',student)


def learn_django(request):
    # stu = {'stu1': {'name':'Developer','roll':'2020'},
    #          'stu2' : {'name':'chinna','roll':'1010'},
    #         }
    # students =  {'student':stu}

    data = {'name':'ADI','no':102}
    return render(request, 'course/one.html',{'data':data})