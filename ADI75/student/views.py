from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def setsession(request):
    request.session['name'] = 'Adi'
   
  
    return render(request, 'student/setsession.html')




def getsession(request):
    if 'name' in request.session:
        # request.request.session['name']
        # name = request.session.get('name')
        now = datetime.now()
        return render(request, 'student/getsession.html',{'name':name,'now':now})
    else:
        return HttpResponse("Your session has expired.........")

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')