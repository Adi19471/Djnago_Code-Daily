from django.shortcuts import render




def setsession(request):
    request.session['name'] = 'Adi'
    request.session['lname'] = 'DJANGO'
    return render(request, 'student/setsession.html')




def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
   
    return render(request, 'student/getsession.html',{'name':name,'lname':lname})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']

    return render(request, 'student/delsession.html')