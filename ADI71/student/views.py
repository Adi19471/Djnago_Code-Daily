from django.shortcuts import render




def setsession(request):
    request.session['name'] = 'Adi'
    request.session['lname'] = 'JHA'
  
    return render(request, 'student/setsession.html')




def getsession(request):
    name = request.session.get('name')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age','26')

    return render(request, 'student/getsession.html',{'name':name,'keys':keys,'items':items,'age':age})


def delsession(request):
    

    return render(request, 'student/delsession.html')