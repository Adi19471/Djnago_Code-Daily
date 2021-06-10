from django.shortcuts import render

# Create your views here.
def learn_django(request):
    name : "chinna"
    age :"25"
    designation:"Django developer"

    context ={'name':'name','aa':'age','designation':'designation'}
    return render(request,'course/one.html',context)

def learn_python(request):
    
    cname = "adi"
    age ="24 age"
    jobrole = "developer"
    context = {'na':cname,'ag':age,'job':jobrole}
    return render(request, 'course/two.html',context)
        
        